# USS-receptor

### STRING ###

The STRING scripts are based on the STRING documentation (https://string-db.org/help/api/). First, run the STRING scripts as follow:

```python string_script_use_partner_to_get_annotations_batch.py```

```python string_script_get_link.py```

The first script will generate the files string_partners_output.tsv (lists queries, their top predicted partner by STRING and the STRING score) and annotated_interactions.tsv (lists queries, top predicted partners and all retrieved functional annotation for both). The second script will list queries and URL links to the STRING predictions for the queries.

### Genome clustering and selection ###

For the genome clustering and selection on fastANI results, run this:

```python reduce_genome_redundancy.py fastANI_output_whole_genomes.out 98```

This reduces redundancy (many highly similar genomes) by using a graph-edge network method to select one representative genome from clusters of genomes that have >= 98% ANI.
