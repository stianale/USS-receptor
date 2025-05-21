#!/usr/bin/env python3

import requests
import time

string_api_url = "https://version-12-0.string-db.org/api"
output_format = "tsv-no-header"
method = "interaction_partners"

my_genes = [
"AAC22416.1"
]

# Construct the request
request_url = f"{string_api_url}/{output_format}/{method}"

# Set parameters
params = {
    "identifiers": "\n".join(my_genes),  # Properly format identifiers
    "species": 712,  # NCBI/STRING taxon identifier 
    "limit": 1,  # Limit to top 1 partner
    "caller_identity": "www.awesome_app.org"  # Your app name
}

# Call STRING API
response = requests.post(request_url, data=params)

if not response.ok:
    print(f"Error: STRING API request failed with status code {response.status_code}")
    exit(1)

# Output file for partner interactions
output_file = "string_partners_output.tsv"

with open(output_file, "w") as out:  # Overwrite instead of append
    out.write("Query_Protein\tQuery_Name\tPartner_Protein\tPartner_Name\tCombined_Score\n")

for line in response.text.strip().split("\n"):
    l = line.strip().split("\t")
    if len(l) < 6:
        print(f"Skipping malformed line: {line}")
        continue

    query_ensp, partner_ensp, query_name, partner_name, combined_score = l[0], l[1], l[2], l[3], l[5]

    # Save results
    with open(output_file, "a") as out:
        out.write(f"{query_ensp}\t{query_name}\t{partner_ensp}\t{partner_name}\t{combined_score}\n")
    print("\t".join([query_ensp, query_name, partner_ensp, partner_name, combined_score]))

time.sleep(1)  # Prevent API rate limit issues

# ========== SECOND STEP: Get Annotations ==========

# STRING API details
method = "functional_annotation"
request_url = f"{string_api_url}/{output_format}/{method}"

# Read interactions from output file
input_file = "string_partners_output.tsv"
interactions = []

query_proteins = set()
partner_proteins = set()

with open(input_file, "r") as f:
    next(f)  # Skip header
    for line in f:
        parts = line.strip().split("\t")
        if len(parts) >= 4:
            query, query_name, partner, partner_name = parts[:4]
            interactions.append((query, query_name, partner, partner_name))
            query_proteins.add(query)
            partner_proteins.add(partner)

# Combine query and partner proteins for annotation lookup
all_proteins = query_proteins.union(partner_proteins)

# Set parameters
params = {
    "identifiers": "\n".join(all_proteins),
    "species": 712,  # NCBI taxon ID
    "caller_identity": "www.awesome_app.org",
    "allow_pubmed": 1  # Include PubMed annotations
}

response = requests.post(request_url, data=params)

if not response.ok:
    print(f"Error: STRING API annotation request failed with status code {response.status_code}")
    exit(1)

annotations = {}

for line in response.text.strip().split("\n"):
    l = line.strip().split("\t")
    if len(l) < 8:  # Ensure enough columns are present
        print(f"Skipping malformed line: {line}")
        continue

    input_genes = l[5].split(',')  # Split comma-separated list of input genes
    description = l[7].strip()     # Description is in the 4th column (index 3)

    for gene in input_genes:
        gene = gene.strip()
        # Handle combined annotations (shared pathways or multiple annotations)
        if gene in annotations:
            # Append new description segments if not already present
            existing_descriptions = annotations[gene].split('. ')
            if description not in existing_descriptions:
                annotations[gene] += ". " + description
        else:
            annotations[gene] = description
        print(f"Gene: {gene}, Description: {annotations[gene]}")

# Output the results
output_file = "annotated_interactions.tsv"

with open(output_file, "w") as out:  # Overwrite instead of append
    out.write("Query_Protein\tQuery_Name\tQuery_Description\tPartner_Protein\tPartner_Name\tPartner_Description\n")
    for query, query_name, partner, partner_name in interactions:
        query_desc = annotations.get(query, "No description available")
        partner_desc = annotations.get(partner, "No description available")
        out.write(f"{query}\t{query_name}\t{query_desc}\t{partner}\t{partner_name}\t{partner_desc}\n")

print(f"Results saved to {output_file}")
