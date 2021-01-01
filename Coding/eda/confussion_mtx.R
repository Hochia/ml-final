cM = function(pred, truth = pred) {
  pred = factor(pred)
  truth = factor(truth)
  confusionMatrix(pred, truth)
}
cM_cm = function(df) {
  if(ncol(df) != 1) stop("dataframe must be 1 column")
  cn = names(df)
  ow = "Otherwise"
  x = factor(case_when(df[[1]] == 1 ~ cn, TRUE ~ ow), c(cn, ow))
  confusionMatrix(x, x)
}
cM_list = function(df) {
  ls = list()
  for (i in names(df)) {
    ls[[i]] = cM_cm(df[, i])
  }
  ls
}

attr_cM = cM_list(df_attr[,-1])
attr_cM
attr_cM[[1]]
# 
# df_attr[,2]
# case_when(df_attr[,2])
# names(df_attr[,2])
# 
# mtxtbl(cM(df_attr$`5_o_Clock_Shadow`), colname_to = colnames(cM(df_attr$`5_o_Clock_Shadow`)))
# as.table(cM(df_attr$`5_o_Clock_Shadow`))
# factor(df_attr$`5_o_Clock_Shadow`)
# confusionMatrix(df_attr$`5_o_Clock_Shadow`, df_attr$`5_o_Clock_Shadow`)
# 
# as_tibble(as.table(attr_cM[[1]])) %>% 
#   pivot_longer(Prediction:Reference) %>% 
#   ggplot() +
#   geom_count(aes(name, ))
# 
# as.table(attr_cM[[1]])
# df = as_tibble(as.table(attr_cM[[1]]))
# df
# as_tibble(as.table(attr_cM[[1]])) %>% 
#   ggplot(aes(Prediction, Reference)) +
#   geom_point(aes(size = n, color = n)) +
#   geom_text(aes(label = n)) +
#   scale_x_discrete(position = "top") +
#   scale_color_viridis(option="magma") +
#   # scale_color_brewer(palette = "magma") +
#   # scale_color_continuous(type = "viridis") +
#   # scale_color_manual(
#   #   name = NULL,
#   #   breaks = c("ratio", "nratio"),
#   #   labels = c("Match", "Not Match"),
#   #   values = c("#6504BA", "#FF8800")
#   # ) +
#   facet_grid(vars(Reference), vars(Prediction), scales = "free", space = "free", switch="y") +
#   theme_test()
# 
# 
## 2 class example
lvs <- c("normal", "abnormal")
truth <- factor(rep(lvs, times = c(86, 258)),
                levels = rev(lvs))
pred <- factor(
  c(
    rep(lvs, times = c(54, 32)),
    rep(lvs, times = c(27, 231))),
  levels = rev(lvs))
xtab <- table(pred, truth)
results <- confusionMatrix(xtab)
as.table(results)
as.matrix(results)
as.matrix(results, what = "overall")
as.matrix(results, what = "classes")

as_tibble()
mtcars %>%
  as_tibble() %>%
  rownames_to_column("rname")
###################
## 3 class example
xtab <- confusionMatrix(iris$Species, sample(iris$Species))
as.matrix(xtab)
