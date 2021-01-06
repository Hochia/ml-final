CP <- FactoMineR::PCA(df_attr[, -1], scale.unit = TRUE, ncp = 10, graph = TRUE)
cp_eig = as_tibble(CP$eig, rownames = "dim") %>% 
  mutate(dim = as.numeric(str_replace(dim, "comp ", "")))
names(cp_eig) <- c("dim", "egv", "var", "cum")
# Correlations between variables and dimensions
cp_vc = as_tibble(CP$var$cor, rownames = "rowname")
cp_vc
cp_ct = as_tibble(CP$var$contrib, rownames = "rowname")
cp_ct
# 翠取出 10 個因素，表示 10 個購物籃。
# 因素負荷量(-1~1)，因素特徵值(表示購物籃產品間的關聯程度)
# 因素特徵值最高的購物籃，最佳產品組合
CB = cp_vc %>% 
  # 篩選絕對值大於 0.4 的負荷量
  mutate_at(vars(starts_with("Dim")), ~ case_when(abs(.) > 0.45 ~ ., TRUE ~ NA_real_))
View(CB)
# PCA 反而比較難挑選出適當的變數研究
# Basket
BK = function(.data, bk, index) {
  .df = data.frame(
    cat = .data[[1]][index],
    cor = .data[[bk + 1]][index]
  ) %>%
    arrange(desc(cor))
  ang = match(.df[[1]], .data[[1]])
  list(.df, ang)
}
# Basket 1
BK1 <- BK(CB, 1, c(2, 3, 8, 19, 21, 25, 37))
BK1
# Basket 2
BK2 <- BK(CB, 2, c(14, 15, 20, 22, 32, 40))
BK2
# Basket 3
BK3 <- BK(CB, 3, c(17, 31))
BK3

# 圖 特徵值與解釋變異程度
ggplot(cp_eig[1:10,], aes(dim, cum)) +
  geom_point() +
  geom_line() +
  geom_text(aes(label = round(cum,2)), color = "purple", size = 3, vjust = .5, hjust = -.5) +
  geom_text(aes(label = round(egv,2)), color = "orange", size = 3, vjust = -1, hjust = .5) +
  scale_x_continuous(breaks = 1:10) +
  labs(x = "因素", y = "累積解釋變異程度") +
  theme_classic()
# 圖 購物籃
net_BK <- function(.list) {
  # browser()
  n <- length(.list)
  .data <- tibble(bk = character(), cat = character())
  for(i in 1:(n/2)) {
    .data <- .data %>%
      bind_rows(list(
        bk = rep(paste0(i), length(.list[[-1+i*2]][[1]])), 
        cat = .list[[-1+i*2]][[1]]))
  }
  .data
}
# Net
Net <- net_BK(c(BK1,BK2,BK3))
network <- graph_from_data_frame(Net, FALSE)
CLR <- c(rep("#FCA636FF", 3), rep("#BD3786FF", 16))
plot(network, 
     layout=layout.fruchterman.reingold,
     edge.width=E(network)$Correlation*2,
     vertex.color = CLR,
     vertex.label.color="white",
     vertex.label.cex=.9,
     vertex.label.dist = 0,
     vertex.frame.color="transparent",
)



# PCA table
CP <- FactoMineR::PCA(df_attr[, -1], scale.unit = TRUE, ncp = 10, graph = TRUE)
cp_eig = as_tibble(CP$eig, rownames = "dim") %>% 
  mutate(dim = as.numeric(str_replace(dim, "comp ", "")))
names(cp_eig) <- c("dim", "egv", "var", "cum")

PCAtable_var = cp_eig %>% 
  mutate(egv_cum = str_c(round(egv, 3), " (", round(cum, 2), "%)")) %>% 
  select(dim, egv_cum)

PCAtable = as_tibble(CP$var$cor) %>% 
  mutate(Attribute = str_replace_all(rownames(CP$var$cor), "_", " ")) %>% 
  select(Attribute, everything())

PCAtable_explain = PCAtable %>% 
  pivot_longer(-Attribute, names_to = "PC", values_to = "Loading") %>% 
  mutate(PC = as.double(str_replace(PC, "Dim.", ""))) %>% 
  filter(
    (PC == 1 & abs(Loading) > 0.50) |
    (PC == 2 & abs(Loading) > 0.45) |
    (PC == 3 & abs(Loading) > 0.45) |
    (PC == 4 & abs(Loading) > 0.30)
  ) %>% 
  arrange(PC, desc(abs(Loading))) %>% 
  mutate(Factor = case_when(
    PC == 1 ~ "Feminine",
    PC == 2 ~ "Smiling",
    PC == 3 ~ "Bearded",
    PC == 4 ~ "Masculine",
    TRUE ~ ""
  )) %>% 
  left_join(PCAtable_var, c(PC = "dim")) %>% 
  select(PC, Factor, Attribute, Loading, egv_cum)

PCAtable_explain
# write_csv(PCAtable_explain, file = "table/PCA_loading.csv")

PCAtable_explain %>% 
  kbl(digits = 2, align = c('l', 'r', 'r', 'l', 'l'), col.names = c("Attribute", "PC", "Loading", ""))

# Loading plot
plot_PCALoading = function(PCALoading, PC) {
  PCALoading %>% 
    filter(PC == !!PC) %>% 
    arrange(abs(Loading)) %>% 
    mutate(Attribute = factor(Attribute, .$Attribute)) %>% 
    ggplot(aes(Attribute, abs(Loading), color = pn, fill = pn)) +
    geom_col() +
    scale_fill_manual(
      name = NULL,
      breaks = c("a", "b"),
      labels = c("Positive", "Negative"), 
      values = c("#D6BEFA", "#F5E3C9")
    ) +
    scale_color_manual(
      name = NULL,
      breaks = c("a", "b"),
      labels = c("Positive", "Negative"),
      values = c("#6504BA", "#FF8800")
    ) +
    scale_y_continuous(
      breaks = seq(0, 1, 0.2),
      limits = c(0, 1)
    ) +
    coord_flip() +
    labs(x = NULL, y = NULL, title = str_c("PC ", PC)) +
    theme_test() +
    theme(legend.position="right")
}

PCALoading = PCAtable %>% 
  pivot_longer(-Attribute, names_to = "PC", values_to = "Loading") %>% 
  mutate(PC = as.double(str_replace(PC, "Dim.", "")), pn = case_when(Loading > 0 ~ "a", TRUE ~ "b"))

loading = map(1:4, ~ plot_PCALoading(PCALoading, .x))
plt = loading[[1]] + loading[[2]] + loading[[3]] + loading[[4]] + plot_layout(ncol = 2, guides = "collect")
ggsave("plot/pca_loading_plot.png", plt, width = 30, height = 25, units = "cm")

# Deprecated
sum(CP$var$cor[,1])
sum(CP$ind$cor[,1])
pp = sweep(CP$var$coord,2,sqrt(CP$eig[1:ncol(CP$var$coord),1]),FUN="/")
typeof(pp)
class(pp)
as_tibble(pp) %>% 
  summarise_all(sum)
