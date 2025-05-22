# Load libraries
library(dplyr)
library(tidyr)
library(reshape2)

# Set working directory (adjust this to your actual directory if needed)
setwd("/media/stian/hgst6tb/Coevolution/Seqkit")

# Define output FASTA file
output_fasta <- "extended_uss_sequences.fa"

# Initialize an empty character vector to store FASTA entries
fasta_entries <- c()

# List all input files matching the pattern "GC*txt"
input_files <- list.files(pattern = "^GC.*\\.txt$")

# Loop through each file
for (file in input_files) {
  # Extract the file prefix to use as the FASTA header
  file_prefix <- sub("\\.txt$", "", file)
  
  # Load data
  data <- read.delim(file, sep = "\t", header = TRUE)
  matched_sequences <- data$matched
  
  # Split sequences into individual nucleotides
  split_sequences <- strsplit(matched_sequences, "")
  sequence_df <- do.call(rbind, split_sequences) %>%
    as.data.frame()
  
  # Assign position numbers
  colnames(sequence_df) <- paste0("pos_", 1:ncol(sequence_df))
  
  # Calculate frequencies for each nucleotide at each position
  variable_long <- melt(sequence_df, id.vars = NULL, variable.name = "position", value.name = "nucleotide")
  
  frequencies <- variable_long %>%
    group_by(position, nucleotide) %>%
    summarise(count = n(), .groups = "drop_last") %>%
    group_by(position) %>%
    mutate(frequency = count / sum(count)) %>%
    ungroup()
  
  # Determine the consensus sequence by selecting the most frequent nucleotide at each position
  consensus_sequence <- frequencies %>%
    group_by(position) %>%
    slice_max(frequency, n = 1, with_ties = FALSE) %>%
    arrange(as.numeric(sub("pos_", "", position))) %>%
    pull(nucleotide) %>%
    paste0(collapse = "")
  
  # Add the consensus sequence to the FASTA entries
  fasta_entries <- c(fasta_entries, paste0(">", file_prefix), consensus_sequence)
}

# Write the FASTA entries to the output file
writeLines(fasta_entries, output_fasta)

cat("Consensus sequences have been written to:", output_fasta, "\n")
