corr_kbl = tibble(
  Baskets = rep(c(1, 2, 3), c(7, 3, 2)),
  Attributes = names(df_attr[, -1])[c(37, 19, 21, 25, 1, 31, 17, 20, 32, 22, 14, 15)],
)
corr_kbl
pca_kbl = tibble(
  Baskets = rep(c(1, 2, 3), c(7, 6, 2)),
  Attributes = names(df_attr[, -1])[c(8, 37, 3, 2, 21, 19, 25, 20, 32, 22, 40, 15, 14, 31, 17)]
)
pca_kbl
