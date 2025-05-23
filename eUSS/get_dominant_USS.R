library(dplyr)

setwd("/media/stian/hgst6tb/Coevolution/Seqkit")

df <- read.delim("Traits_file_all_orthofinder_with_genome_size.txt", sep = '\t', header = TRUE)

df <- df %>% mutate(Dominant = case_when(Hin_USS > Apl_USS ~ "Hin-USS",
                                         Apl_USS > Hin_USS ~ "Apl-USS"))

hin_list <- df %>% filter(Dominant == "Hin-USS")

apl_list <- df %>% filter(Dominant == "Apl-USS")

hin_list <- hin_list %>% select(Genome)

apl_list <- apl_list %>% select(Genome)

write.table(hin_list, file = "hin_list.txt", col.names = FALSE, row.names = FALSE, quote = FALSE, sep = '\t')

write.table(apl_list, file = "apl_list.txt", col.names = FALSE, row.names = FALSE, quote = FALSE, sep = '\t')