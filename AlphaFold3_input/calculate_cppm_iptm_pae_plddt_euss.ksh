#!/bin/ksh93

for file in $(find USS_output/Native_vs_Scrambled/All_proteins_species/Extended_USS/ -name "summary_confidences.json");
do
conf_file=$(echo "${file}" | sed "s/summary_confidences/confidences/g")
model=$(echo "${file}" | sed "s/summary_confidences.json/model.cif/g")
pair_pae_min=$(grep -A 16 "chain_pair_pae_min" ${file} | sed -e '1d;2d;3d;6d;7d;9d;11d;12d;15d;16d;17d' | sed "s/,//g" | sed "s/   //g")
iptm=$(grep "\"iptm"\" ${file} | sed "s/.*: //g" | sed "s/,$//g")
pae_plddt=$(python /media/stian/hgst6tb/alphafold3/calculate_pae_plddt.py "${conf_file}"); 
# Calculate the sum of the numbers using awk
sum=$(echo "$pair_pae_min" | awk '{s+=$1} END {print s}')

# Count the number of lines (numbers)
count=$(echo "$pair_pae_min" | wc -l)

# Calculate the average
average=$(echo "scale=2; $sum / $count" | bc)

echo -e "${model}\t${average}\t${iptm}\t${pae_plddt}" >> cppm_iptm_pae_plddt_extended_uss_updated.txt
done