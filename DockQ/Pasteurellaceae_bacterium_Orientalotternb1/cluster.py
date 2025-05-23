import networkx as nx
import pandas as pd

# Load the DockQ data
df = pd.read_csv("Master_results_DockQ_new.txt", sep="\t", header=None, names=["Model", "Reference", "DockQ"])

# Convert DockQ to float
df["DockQ"] = pd.to_numeric(df["DockQ"], errors="coerce")

# Drop NaN values
df = df.dropna(subset=["DockQ"])

# Filter for only DockQ ≥ 0.490
df_filtered = df[df["DockQ"] >= 0.490]

# Create an undirected graph
G = nx.Graph()
for _, row in df_filtered.iterrows():
    G.add_edge(row["Model"], row["Reference"])

# Find all maximal cliques in the graph
cliques = list(nx.find_cliques(G))

# Sort cliques in descending order of size to prioritize larger cliques
cliques_sorted = sorted(cliques, key=lambda x: len(x), reverse=True)

# Assign each node to the first clique it appears in (to avoid overlaps)
clusters = []
assigned_nodes = set()

for clique in cliques_sorted:
    # Consider only nodes not yet assigned
    current_clique = [node for node in clique if node not in assigned_nodes]
    if current_clique:
        clusters.append(set(current_clique))
        assigned_nodes.update(current_clique)

# Ensure any remaining nodes in G are added as singleton clusters
all_nodes_in_G = set(G.nodes())
unassigned_in_G = all_nodes_in_G - assigned_nodes
if unassigned_in_G:
    for node in unassigned_in_G:
        clusters.append({node})

# Function to check if all pairs in a cluster have DockQ ≥ 0.490
def is_valid_cluster(cluster, df_filtered):
    cluster_list = list(cluster)
    for i in range(len(cluster_list)):
        for j in range(i + 1, len(cluster_list)):
            m = cluster_list[i]
            r = cluster_list[j]
            # Check if there is an edge (DockQ ≥ 0.490) between m and r
            if not df_filtered[((df_filtered["Model"] == m) & (df_filtered["Reference"] == r)) |
                              ((df_filtered["Model"] == r) & (df_filtered["Reference"] == m))].shape[0] > 0:
                return False
    return True

# Merge clusters iteratively
merged = True
while merged:
    merged = False
    new_clusters = []
    visited = set()

    for i, cluster1 in enumerate(clusters):
        if i in visited:
            continue
        merged_cluster = set(cluster1)

        for j in range(i + 1, len(clusters)):
            if j in visited:
                continue

            # Temporarily merge cluster1 and cluster2
            temp_cluster = merged_cluster.union(clusters[j])

            # Check if all pairs in the merged cluster have DockQ ≥ 0.490
            if is_valid_cluster(temp_cluster, df_filtered):
                merged_cluster = temp_cluster
                visited.add(j)
                merged = True  # Mark that a merge occurred

        new_clusters.append(merged_cluster)
        visited.add(i)

    clusters = new_clusters  # Update the list of clusters

# Filter out singleton clusters and move them to not_assigned
final_clusters = []
not_assigned = set()

for cluster in clusters:
    if len(cluster) >= 2:
        final_clusters.append(cluster)
    else:
        not_assigned.update(cluster)

# Save final merged clusters to files
clustered_models = set()
for i, community in enumerate(final_clusters, start=1):
    cluster_file = f"cluster_{i}.txt"
    with open(cluster_file, "w") as f:
        for node in sorted(community):
            f.write(f"{node}\n")
            clustered_models.add(node)
    print(f"Saved cluster {i} to {cluster_file}")

# Save unassigned models (from original data) as separate files
all_models = set(df["Model"]).union(set(df["Reference"]))
unassigned_models = all_models - clustered_models

# Add singleton clusters to not_assigned
unassigned_models.update(not_assigned)

for idx, model in enumerate(sorted(unassigned_models), start=1):
    not_assigned_file = f"not_assigned_{idx}.txt"
    with open(not_assigned_file, "w") as f:
        f.write(f"{model}\n")
    print(f"Saved unassigned model to {not_assigned_file}")