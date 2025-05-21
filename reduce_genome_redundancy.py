import sys
import networkx as nx

def reduce_redundancy(file_path, ani_cutoff):
    ani_cutoff = float(ani_cutoff)
    # Step 1: Initialize a graph for genome pairs with ANI >= cutoff
    graph = nx.Graph()
    all_genomes = set()

    # Read input file and construct the graph
    with open(file_path, "r") as f:
        for line in f:
            genome1, genome2, ani, *_ = line.strip().split()
            ani = float(ani)
            all_genomes.update([genome1, genome2])  # Keep track of all genomes
            # Exclude self-same genome comparisons and ANI < cutoff
            if genome1 != genome2 and ani >= ani_cutoff:
                graph.add_edge(genome1, genome2)

    # Step 2: Identify connected components (groups of similar genomes)
    connected_components = list(nx.connected_components(graph))

    # Step 3: Select representatives for each component
    representatives = []
    redundant_genomes = []

    for component in connected_components:
        component_list = list(component)

        # If GCA_000027305.1_ASM2730v1_genomic.fna is in the component, select it as representative
        if "GCA_000027305.1_ASM2730v1_genomic.fna" in component_list:
            representative = "GCA_000027305.1_ASM2730v1_genomic.fna"
        else:
            # Otherwise, choose the genome with the most connections, excluding GCA_020892835.1_ASM2089283v1_genomic.fna
            filtered_component = [
                genome for genome in component_list
                if genome != "GCA_020892835.1_ASM2089283v1_genomic.fna"
            ]
            representative = max(
                filtered_component, key=lambda genome: graph.degree[genome]
            ) if filtered_component else None

        if representative:
            representatives.append(representative)
            redundant_genomes.extend(
                genome for genome in component_list if genome != representative
            )

    # Step 4: Include genomes that have no pairings (not in any connected component)
    paired_genomes = set(graph.nodes())
    unpaired_genomes = all_genomes - paired_genomes
    unpaired_genomes = {
        genome for genome in unpaired_genomes
        if genome != "GCA_020892835.1_ASM2089283v1_genomic.fna"
    }
    representatives.extend(unpaired_genomes)

    # Step 5: Write results to files
    with open("genomes_to_keep.txt", "w") as keep_file:
        keep_file.write("\n".join(sorted(representatives)) + "\n")

    with open("genomes_to_remove.txt", "w") as remove_file:
        remove_file.write("\n".join(sorted(redundant_genomes)) + "\n")

    print(f"Genomes to keep: {len(representatives)}")
    print(f"Genomes to remove: {len(redundant_genomes)}")

if __name__ == "__main__":
    # Ensure the script is run with the required file argument
    if len(sys.argv) != 3:
        print("Usage: python script.py <fastANI_output_file> <ani_cutoff>")
        sys.exit(1)

    reduce_redundancy(sys.argv[1], sys.argv[2])
