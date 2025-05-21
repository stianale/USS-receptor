#!/usr/bin/env python3

import requests
import time

string_api_url = "https://version-12-0.string-db.org/api"
output_format = "tsv-no-header"
method = "interaction_partners"

my_genes = ["AAC21683.1",
"AAC22416.1",
"AAC23068.1",
"AAC23320.1",
"AAC21697.1",
"AAC21721.1",
"AAC21783.1",
"AAC21941.1",
"AAC21942.1",
"AAC21960.1",
"AAC21961.1",
"AAC21963.1",
"AAC21969.1",
"AAC21977.1",
"AAC22000.1",
"AAC22028.1",
"AAC22054.1",
"AAC22094.1",
"AAC22096.1",
"AAC22097.1",
"AAC22111.1",
"AAC22126.1",
"AAC22165.1",
"AAC22168.1",
"AAC22380.1",
"AAC22476.1",
"AAC22499.1",
"AAC22514.1",
"AAC22570.1",
"AAC22602.1",
"AAC22604.1",
"AAC22605.1",
"AAC22613.1",
"AAC22629.1",
"AAC22645.1",
"AAC22694.1",
"AAC22730.1",
"AAC22806.1",
"AAC22823.1",
"AAC22856.1",
"AAC22859.1",
"AAC22893.1",
"AAC22908.1",
"AAC22918.2",
"AAC22943.1",
"AAC23002.1",
"AAC23041.1",
"AAC23074.1",
"AAC23083.1",
"AAC23100.1",
"AAC23106.1",
"AAC23259.1",
"AAC23272.1",
"AAC23290.1",
"AAC23300.1",
"AAC23327.1",
"AAC23370.1",
"AAC23375.1",
"AAC21685.1",
"AAC21688.1",
"AAC21692.1",
"AAC21693.1",
"AAC21707.1",
"AAC21710.1",
"AAC21714.1",
"AAC21718.1",
"AAC21735.1",
"AAC21739.1",
"AAC21744.1",
"AAC21747.1",
"AAC21750.1",
"AAC21753.1",
"AAC21755.1",
"AAC21760.1",
"AAC21778.1",
"AAC21781.1",
"AAC21782.1",
"AAC21785.1",
"AAC21789.1",
"AAC21795.1",
"AAC21801.1",
"AAC21810.1",
"AAC21821.1",
"AAC21822.1",
"AAC21828.1",
"AAC21846.1",
"AAC21847.1",
"AAC21855.1",
"AAC21866.1",
"AAC21879.1",
"AAC21882.1",
"AAC21887.1",
"AAC21896.1",
"AAC21897.1",
"AAC21901.1",
"AAC21905.1",
"AAC21922.1",
"AAC21927.1",
"AAC21928.1",
"AAC21929.1",
"AAC21943.1",
"AAC21962.1",
"AAC21965.1",
"AAC21992.1",
"AAC22003.1",
"AAC22022.1",
"AAC22024.1",
"AAC22025.1",
"AAC22036.1",
"AAC22039.1",
"AAC22047.1",
"AAC22059.1",
"AAC22060.1",
"AAC22065.1",
"AAC22068.1",
"AAC22082.1",
"AAC22090.1",
"AAC22093.1",
"AAC22098.1",
"AAC22099.1",
"AAC22109.1",
"AAC22110.1",
"AAC22119.1",
"AAC22141.1",
"AAC22154.1",
"AAC22179.1",
"AAC22182.1",
"AAC22201.1",
"AAC22225.1",
"AAC22227.1",
"AAC22242.1",
"AAC22244.1",
"AAC22248.1",
"AAC22257.1",
"AAC22270.1",
"AAC22279.1",
"AAC22282.1",
"AAC22294.1",
"AAC22295.1",
"AAC22298.1",
"AAC22302.1",
"AAC22305.1",
"AAC22319.1",
"AAC22324.1",
"AAC22326.1",
"AAC22343.1",
"AAC22348.1",
"AAC22353.1",
"AAC22357.1",
"AAC22363.1",
"AAC22368.1",
"AAC22369.1",
"AAC22375.1",
"AAC22378.1",
"AAC22383.1",
"AAC22389.1",
"AAC22408.1",
"AAC22410.1",
"AAC22412.1",
"AAC22413.1",
"AAC22415.1",
"AAC22420.1",
"AAC22428.1",
"AAC22475.1",
"AAC22496.1",
"AAC22500.1",
"AAC22502.1",
"AAC22504.1",
"AAC22513.1",
"AAC22546.1",
"AAC22558.1",
"AAC22561.1",
"AAC22563.1",
"AAC22569.1",
"AAC22572.1",
"AAC22574.1",
"AAC22575.1",
"AAC22585.1",
"AAC22590.1",
"AAC22599.1",
"AAC22601.1",
"AAC22628.1",
"AAC22633.1",
"AAC22642.1",
"AAC22651.1",
"AAC22656.1",
"AAC22657.1",
"AAC22659.1",
"AAC22665.1",
"AAC22666.1",
"AAC22669.1",
"AAC22672.1",
"AAC22673.1",
"AAC22693.1",
"AAC22698.1",
"AAC22706.1",
"AAC22728.1",
"AAC22729.1",
"AAC22750.1",
"AAC22752.1",
"AAC22771.1",
"AAC22773.1",
"AAC22787.1",
"AAC22804.1",
"AAC22817.1",
"AAC22819.1",
"AAC22834.1",
"AAC22848.1",
"AAC22862.1",
"AAC22865.1",
"AAC22869.1",
"AAC22870.1",
"AAC22882.1",
"AAC22883.1",
"AAC22886.1",
"AAC22888.1",
"AAC22889.1",
"AAC22899.1",
"AAC22904.1",
"AAC22906.1",
"AAC22907.1",
"AAC22909.1",
"AAC22911.1",
"AAC22913.1",
"AAC22915.1",
"AAC22917.1",
"AAC22923.1",
"AAC22931.1",
"AAC22934.1",
"AAC22948.1",
"AAC22970.1",
"AAC22971.1",
"AAC22975.1",
"AAC22976.1",
"AAC22979.1",
"AAC22993.1",
"AAC22995.1",
"AAC23013.1",
"AAC23015.1",
"AAC23024.1",
"AAC23029.1",
"AAC23046.1",
"AAC23051.1",
"AAC23055.1",
"AAC23056.1",
"AAC23057.1",
"AAC23079.1",
"AAC23085.1",
"AAC23108.1",
"AAC23112.1",
"AAC23122.1",
"AAC23133.1",
"AAC23142.1",
"AAC23146.1",
"AAC23148.1",
"AAC23149.1",
"AAC23151.1",
"AAC23155.1",
"AAC23156.1",
"AAC23157.1",
"AAC23170.1",
"AAC23191.1",
"AAC23210.1",
"AAC23211.1",
"AAC23213.1",
"AAC23214.1",
"AAC23228.1",
"AAC23239.1",
"AAC23251.1",
"AAC23258.1",
"AAC23262.1",
"AAC23275.1",
"AAC23282.1",
"AAC23283.1",
"AAC23297.1",
"AAC23299.1",
"AAC23302.1",
"AAC23314.1",
"AAC23331.1",
"AAC23333.1",
"AAC23342.1",
"AAC23347.1",
"AAC23348.1",
"AAC23351.1",
"AAC23362.1",
"AAC23368.1"]

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
