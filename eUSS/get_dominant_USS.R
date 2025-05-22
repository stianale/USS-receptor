library(dplyr)

setwd("/media/stian/hgst6tb/Coevolution/Seqkit")

df <- read.delim("Traits_file_all_orthofinder_with_genome_size.txt", sep = '\t', header = TRUE)

df <- df %>% mutate(Dominant = case_when(Hin_USS > Apl_USS ~ "Hin-USS",
                                         Apl_USS > Hin_USS ~ "Apl-USS"))