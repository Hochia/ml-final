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
