# plot correlation matrix
ggcorr(df_attr[, -1], palette = "RdYlBu", name = NULL, label_size = 1, size = 3, hjust = 1, angle = 0, nbreaks = 10, layout.exp = 11, limits = FALSE) + 
  guides(fill = guide_legend(reverse=T))

CR = cor(df_attr[,-1])
CR[lower.tri(CR, TRUE)] = NA
CTB <- 
  CR %>% 
  as_tibble(rownames = "Base") %>% 
  pivot_longer(-Base, 
               names_to = "Category", 
               values_to = "Correlation") %>% 
  filter(is.na(Correlation) != TRUE) %>% 
  arrange(desc(abs(Correlation)), Base, Category)

# network of top 10 correlation
network <- graph_from_data_frame(CTB[1:10,], FALSE)
# network <- graph_from_data_frame(CTB[c(8),], FALSE)
# network <- graph_from_data_frame(CTB[c(3, 7),], FALSE)
# network <- graph_from_data_frame(CTB[c(1, 2, 4, 5, 6, 9, 10),], FALSE)
par(bg="grey13", mar=c(0,0,0,0))
plot(network, 
     layout=layout.fruchterman.reingold,
     edge.width=abs(E(network)$Correlation)*2,
     vertex.color = "#1A8A6C",
     vertex.label.color="white",
     vertex.label.cex=.9,
     vertex.label.dist = 0,
     vertex.frame.color="transparent"
)

# network table
CTB[1:10,] %>% 
  mutate(Base = case_when(Base == CTB[[1]][9] ~ "5 o'Clock Shadow",
                          TRUE ~ str_replace_all(Base, "_", " ")),
         Category = str_replace_all(Category, "_", " ")) %>% 
  kbl(digits = 2) %>% 
  kable_classic(full_width = F, html_font = "Cambria")
  

# (df_attr[, -1] + 1) / 2
# brewer.pal(n = 8, name = 'RdYlBu')
