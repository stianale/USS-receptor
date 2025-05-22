#!/bin/ksh93

for acc in $(cat Pasteurellaceae_bacterium_Orientalotternb1.txt);
do 
mkdir -p All_species_proteins/Pasteurellaceae_bacterium_Orientalotternb1
mkdir -p All_species_proteins/Pasteurellaceae_bacterium_Orientalotternb1/"${acc}"
cd All_species_proteins/Pasteurellaceae_bacterium_Orientalotternb1/"${acc}"
seqkit grep -p "${acc}" ../../Proteome_BLAST_db/Master_Past.faa > "${acc}".fa
biolib run --local 'DTU/DeepTMHMM:1.0.24' --fasta "${acc}".fa
cd ../..
done

for acc in $(cat Actinobacillus_equuli_subsp_haemolyticus_strain_3524_chromosome.txt);
do 
mkdir -p All_species_proteins/Actinobacillus_equuli_subsp_haemolyticus_strain_3524_chromosome
mkdir -p All_species_proteins/Actinobacillus_equuli_subsp_haemolyticus_strain_3524_chromosome/"${acc}"
cd All_species_proteins/Actinobacillus_equuli_subsp_haemolyticus_strain_3524_chromosome/"${acc}"
seqkit grep -p "${acc}" ../../Proteome_BLAST_db/Master_Past.faa > "${acc}".fa
biolib run --local 'DTU/DeepTMHMM:1.0.24' --fasta "${acc}".fa
cd ../..
done

for acc in $(cat Mannheimia_bovis_strain_39324S_11_chromosome.txt);
do 
mkdir -p All_species_proteins/Mannheimia_bovis_strain_39324S-11_chromosome
mkdir -p All_species_proteins/Mannheimia_bovis_strain_39324S-11_chromosome/"${acc}"
cd All_species_proteins/Mannheimia_bovis_strain_39324S-11_chromosome/"${acc}"
seqkit grep -p "${acc}" ../../Proteome_BLAST_db/Master_Past.faa > "${acc}".fa
biolib run --local 'DTU/DeepTMHMM:1.0.24' --fasta "${acc}".fa
cd ../..
done

for acc in $(cat Mannheimia_succiniciproducens_MBEL55E.txt);
do 
mkdir -p All_species_proteins/Mannheimia_succiniciproducens_MBEL55E
mkdir -p All_species_proteins/Mannheimia_succiniciproducens_MBEL55E/"${acc}"
cd All_species_proteins/Mannheimia_succiniciproducens_MBEL55E/"${acc}"
seqkit grep -p "${acc}" ../../Proteome_BLAST_db/Master_Past.faa > "${acc}".fa
biolib run --local 'DTU/DeepTMHMM:1.0.24' --fasta "${acc}".fa
cd ../..
done

for acc in $(cat Frederiksenia_canicola_strain_HPA_21_chromosome.txt);
do 
mkdir -p All_species_proteins/Frederiksenia_canicola_strain_HPA_21_chromosome
mkdir -p All_species_proteins/Frederiksenia_canicola_strain_HPA_21_chromosome/"${acc}"
cd All_species_proteins/Frederiksenia_canicola_strain_HPA_21_chromosome/"${acc}"
seqkit grep -p "${acc}" ../../Proteome_BLAST_db/Master_Past.faa > "${acc}".fa
biolib run --local 'DTU/DeepTMHMM:1.0.24' --fasta "${acc}".fa
cd ../..
done

for acc in $(cat Aggregatibacter_sp_oral_taxon_513_strain_W11186_chromosome.txt);
do 
mkdir -p All_species_proteins/Aggregatibacter_sp_oral_taxon_513_strain_W11186_chromosome
mkdir -p All_species_proteins/Aggregatibacter_sp_oral_taxon_513_strain_W11186_chromosome/"${acc}"
cd All_species_proteins/Aggregatibacter_sp_oral_taxon_513_strain_W11186_chromosome/"${acc}"
seqkit grep -p "${acc}" ../../Proteome_BLAST_db/Master_Past.faa > "${acc}".fa
biolib run --local 'DTU/DeepTMHMM:1.0.24' --fasta "${acc}".fa
cd ../..
done

for acc in $(cat Aggregatibacter_actinomycetemcomitans_strain_31S_chromosome.txt);
do 
mkdir -p All_species_proteins/Aggregatibacter_actinomycetemcomitans_strain_31S_chromosome
mkdir -p All_species_proteins/Aggregatibacter_actinomycetemcomitans_strain_31S_chromosome/"${acc}"
cd All_species_proteins/Aggregatibacter_actinomycetemcomitans_strain_31S_chromosome/"${acc}"
seqkit grep -p "${acc}" ../../Proteome_BLAST_db/Master_Past.faa > "${acc}".fa
biolib run --local 'DTU/DeepTMHMM:1.0.24' --fasta "${acc}".fa
cd ../..
done

for acc in $(cat Actinobacillus_lignieresii_strain_NCTC4189_whole_genome_shotgun_sequence.txt);
do 
mkdir -p All_species_proteins/Actinobacillus_lignieresii_strain_NCTC4189_whole_genome_shotgun_sequence
mkdir -p All_species_proteins/Actinobacillus_lignieresii_strain_NCTC4189_whole_genome_shotgun_sequence/"${acc}"
cd All_species_proteins/Actinobacillus_lignieresii_strain_NCTC4189_whole_genome_shotgun_sequence/"${acc}"
seqkit grep -p "${acc}" ../../Proteome_BLAST_db/Master_Past.faa > "${acc}".fa
biolib run --local 'DTU/DeepTMHMM:1.0.24' --fasta "${acc}".fa
cd ../..
done

for acc in $(cat Pasteurella_multocida_strain_NCTC8282_chromosome_1.txt);
do 
mkdir -p All_species_proteins/Pasteurella_multocida_strain_NCTC8282_chromosome_1
mkdir -p All_species_proteins/Pasteurella_multocida_strain_NCTC8282_chromosome_1/"${acc}"
cd All_species_proteins/Pasteurella_multocida_strain_NCTC8282_chromosome_1/"${acc}"
seqkit grep -p "${acc}" ../../Proteome_BLAST_db/Master_Past.faa > "${acc}".fa
biolib run --local 'DTU/DeepTMHMM:1.0.24' --fasta "${acc}".fa
cd ../..
done

for acc in $(cat Haemophilus_influenzae_Rd_KW20_chromosome.txt);
do 
mkdir -p All_species_proteins/Haemophilus_influenzae_Rd_KW20_chromosome
mkdir -p All_species_proteins/Haemophilus_influenzae_Rd_KW20_chromosome/"${acc}"
cd All_species_proteins/Haemophilus_influenzae_Rd_KW20_chromosome/"${acc}"
seqkit grep -p "${acc}" ../../Proteome_BLAST_db/Master_Past.faa > "${acc}".fa
biolib run --local 'DTU/DeepTMHMM:1.0.24' --fasta "${acc}".fa
cd ../..
done
