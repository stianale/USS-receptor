#!/bin/ksh

# This first loop loops over all genomes in genomelist.txt and DUS dialects in DUS_dialects.txt and prints counts for all DUS dialects in all genomes to a new text file.
# We do not use the parameter -c for circular genomes, because  the 45 circular, complete genomes in the list do not have DUS occurrences overlapping in start and end coordinates.
# Hence, using the parameter -c could only potentially yield wrong counts for the linear sequences in the contig/scaffold genomes.

ls *.fna >> genomelist.txt

		for file in $(cat genomelist.txt);
		do
			while IFS=$'\t' read -r dialect name;
			do
			shortname=$(echo "${file}" | sed "s/.*GC/GC/g")
			species=$(head -n 1 "${file}" | sed "s/,.*//g" | sed 's/^[^ ]* //' | sed "s/\[//g" | sed "s/\]//g" | sed "s/\//_/g" | sed "s/chromosome//g" | sed "s/  / /g"  | sed "s/ /_/g" | sed "s/_$//g")
			genomesize=$(seqkit stats "${file}" | awk '{print $8}' | sed "1d" | sed "s/,//g")
			results=$(cat "${file}" | seqkit locate -i -p "${dialect}" | sed '1d' | sed '/${dialect}/d' | wc -l)
			echo -e "${shortname}\t${species}\t${dialect}\t${name}\t${results}\t${genomesize}" >> USS_counts.txt
			done < USS_dialects_names.txt
	    done

# This third loop loops over all lines in the input files fna_species_and_basepair_numbers_connected.txt and DUS_counts_final.txt, and prints the name of the DUS dialect,
# genome, species and the occurrences per MB.

while IFS=$'\t' read -r shortname species dialect name results genomesize;
do
CORRECTIONFACTOR=$(python -c "print( $results / float($genomesize / 1000000) )")
echo -e "${shortname}\t${species}\t${dialect}\t${name}\t${CORRECTIONFACTOR}" >> USS_count_per_MB.txt
done < USS_counts.txt