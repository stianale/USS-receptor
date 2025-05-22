# Getting started

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

This reduces redundancy (many highly similar genomes) by using a graph-edge network method to select one representative genome from clusters of genomes that have >= 98% ANI. This may produce different results across separate runs. Our resulting genomes to keep are the genomes listed in Genomes/OD_genomes.txt.

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

### DeepTMHMM ###

For prediction of cellular location of all proteins to be modeled in AlphaFold3 downstream, install the command-line version of DeepTMHMM v. 1.0.24 following instructions here: https://dtu.biolib.com/DeepTMHMM. You will also need to generate a local BLAST database of the proteomes of the accessions in Genomes/OD_genomes.txt. For this, you have to install the BLAST+ command-line suite (https://www.ncbi.nlm.nih.gov/books/NBK569861/). Then:

```mkdir Proteome_BLAST_db```

```cd Proteome_BLAST_db```

```datasets download genome accession --inputfile ../Genomes/OD_genomes.txt --include protein```

```unzip ncbi_dataset.zip```

```rm -rf md5sum.txt ncbi_dataset.zip README.md```

```find . -name "*.faa" -exec mv {} . \;```

```rm -rf ncbi_dataset/```

```cat *.faa >> Master_Past.faa```

```makeblastdb -in Master_Past.faa -parse_seqids -blastdb_version 5 -taxid_map test_map.txt -title "Master_Past" -dbtype prot```

```cd ..```

```cd DeepTMHMM```

```ksh93 DeepTMHMM_bulk_run.ksh```

```cd ..```

### AlphaFold3 ###

To run AlphaFold3 modeling, follow instructions here: https://github.com/google-deepmind/alphafold3. This includes obtaining a license to the AF3 model weights from Google.

We provide the input JSON configuration files that we used in the directory AlphaFold3_input/ in the format dialect/species/ncbi-accession/json-file. The native runs are named "accession.json", while the scrambled runs are named "accession_scrambled_seed#.json". Examples are AlphaFold3_input/Hin-USS/Mannheimia_succiniciproducens_MBEL55E/WP_011199217.1/WP_011199217.1.json (this file specifies to run 20 replicate seeds) and AlphaFold3_input/Hin-USS/Mannheimia_succiniciproducens_MBEL55E/WP_011199217.1/WP_011199217.1_scrambled_1.json. You can run modeling using AlphaFold3_input/Hin-USS/Mannheimia_succiniciproducens_MBEL55E/WP_011199217.1/WP_011199217.1.json in the following way (using Docker):

```mkdir AlphaFold3_output```


```
docker run -i \
    --volume /AlphaFold3_input/Hin-USS/Mannheimia_succiniciproducens_MBEL55E/WP_011199217.1/:/root/af_input \
    --volume /AlphaFold3_output/Hin-USS/Mannheimia_succiniciproducens_MBEL55E/WP_011199217.1/:/root/af_output \
    --volume /path/to/alphafold3_model_weights:/root/models \
    --volume /path/to/alphafold3_databases:/root/public_databases \
    --gpus all \
    alphafold3 \
    python run_alphafold.py \
    --input_dir=/root/af_input \
    --model_dir=/root/models \
    --db_dir=/root/public_databases \
    --output_dir=/root/af_output
```

We also provide the script used to scramble the USS (AlphaFold3_input/scramble_dna_string.py), which can be run as follows:

```python scramble_dna_string.py AAGTGCGGT```

An example console output would be:

"Original DNA: AAGTGCGGT
Scrambled DNA: GGTGATGCA."

You can use the scripts calculate_cppm_iptm_pae_plddt_uss.ksh and calculate_cppm_iptm_pae_plddt_euss.ksh to calculate ipTM, CPPM, PAE and pLDDT for all output models.
