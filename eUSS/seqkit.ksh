#!/bin/ksh93

for file in $(cat hin_list.txt);
do
cat "${file}".fna | seqkit locate -r -p ".AAGTGCGGT......." > "${file}".txt
done

for file in $(cat apl_list.txt);
do
cat "${file}".fna | seqkit locate -r -p ".ACAAGCGGT......." > "${file}".txt
done
