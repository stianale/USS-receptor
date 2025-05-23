#!/bin/bash

echo -e "Model\tReference\tDockQ" > Master_results_DockQ_new.txt

# Read file names from file_list.txt into an array
mapfile -t files < Haemophilus_influenzae_Rd_KW20_chromosome_9_mer_iptm_0_8_or_above.txt

# Loop over each pair of files
for ((i = 0; i < ${#files[@]}; i++)); do
  for ((j = i + 1; j < ${#files[@]}; j++)); do
    file1=${files[$i]}
    file2=${files[$j]}
    
    # Run DockQ --mapping ABC:ABC command and capture results
    DockQ --mapping ABC:ABC "${file1}" "${file2}" > dockq_results.txt
    
    # Extract relevant information
    model=$(grep "Model  : " dockq_results.txt | sed "s/Model  : //g")
    native=$(grep "Native : " dockq_results.txt | sed "s/Native : //g")
    DockQ_score=$(grep -o "interfaces: .*with" dockq_results.txt | sed "s/.*: //g" | sed "s/ .*//g")
    
    # Append results to master file
    echo -e "${model}\t${native}\t${DockQ_score}" >> Master_results_DockQ_new.txt
    
    # Clean up temporary file
    rm -rf dockq_results.txt
  done
done
