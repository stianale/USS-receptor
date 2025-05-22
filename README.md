# USS-receptor

Firstly, clone this repo. Install NCBI datasets following instructions here: https://github.com/ncbi/datasets. Then, move to the Genomes/ directory and download the genomes listed in genomes.txt

```cd Genomes```

```datasets download genome accession --inputfile genomes.txt --include genome```

```unzip ncbi_dataset.zip```

```rm -rf md5sum.txt ncbi_dataset.zip README.md```

```find . -name "*.fna" -exec mv {} . \;```

```rm -rf ncbi_dataset/```

```cd ..```

Proceed to the steps below.

### STRING ###

The STRING scripts are based on the STRING documentation (https://string-db.org/help/api/). To obtain a comprehensive STRING table of functional annotations:

```cd STRING```

```python string_script_use_partner_to_get_annotations_batch.py```

```python string_script_get_link.py```

```cd ..```

The first script will generate the files string_partners_output.tsv (lists queries, their top predicted partner by STRING and the STRING score) and annotated_interactions.tsv (lists queries, top predicted partners and all retrieved functional annotation for both). The second script will list queries and URL links to the STRING predictions for the queries.

### Genome clustering and selection ###

For the genome clustering and selection of genomes from fastANI results (you can replicate the fastANI results by using the many-to-many approach in https://github.com/ParBLiSS/FastANI on the genomes in Genomes/), run this:

```cd Genome_clustering```

```python reduce_genome_redundancy.py fastANI_output_whole_genomes.out 98```

```cd ..```

This reduces redundancy (many highly similar genomes) by using a graph-edge network method to select one representative genome from clusters of genomes that have >= 98% ANI.

### USS counting ###

To obtain the USS counts for selected Pasteurellaceae genomes:

```cd 9_mer_USS```

``` ksh93 USS_counting.ksh ```

```cd ..```

This will generate a file USS_counts.txt that lists the genome, species name, USS dialect nucleotide sequence, USS dialect name, raw counts and the genome size (bp). A file USS_count_per_MB.txt will also be generated, which lists the genome, species name, USS dialect nucleotide sequence, USS dialect name and genome size corrected counts (per MB).

### eUSS ###

To generate an alignment of calculated eUSS for all genomes:

```cd eUSS```

```Rscript get_dominant_USS.R```

```Rscript get_majority_vote.R```

```ksh93 seqkit.ksh```

```cd ..```
