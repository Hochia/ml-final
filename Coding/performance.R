best_performance = function(df) {
  df %>% 
    filter(index == 19) %>% 
    arrange(desc(val_categorical_accuracy)) %>% 
    select(model, categorical_accuracy, val_categorical_accuracy)
}
list_performance = function(df) {
  df %>% 
    pivot_longer(contains(c("accuracy", "loss"))) %>% 
    mutate(
      perform = case_when(str_detect(name, "accuracy") ~ "accuracy", str_detect(name, "loss") ~ "loss", TRUE ~ ""),
      setting = case_when(str_detect(name, "val") ~ "validation", TRUE ~ "training"),
    )
}
plot_performance = function(df) {
  ggplot(df, aes(index, value)) +
    geom_line(aes(color = setting)) +
    facet_grid(vars(perform), vars(model), scales = "free_y") +
    guides(color = guide_legend(title = NULL)) +
    labs(x = "epochs", y = NULL) +
    theme_test() +
    theme(legend.position = "top")
}
save_performance = function(file, name, save_root = "performance/population") {
  csvs = dir(files, pattern = ".csv", full.names = TRUE, recursive = TRUE)
  df = tibble(bind_rows(map(csvs, read.csv)))
  # best performance
  df_best_performance = best_performance(df)
  # list performance
  df_list_performance = list_performance(df)
  # top 5 performance
  df_top5_performance = df_list_performance %>% 
    filter(model %in% df_best_performance$model[1:5])
  ## all models plot
  plt = plot_performance(df_list_performance)
  ggsave(str_c(save_root, paste0(name, ".png"), sep = "/"), plt, width = 100, height = 10, units = "cm")
  ## top 5 models plot
  plt = plot_performance(df_top5_performance)
  ggsave(str_c(save_root, paste0(name, "_top5.png"), sep = "/"), plt, width = 15, height = 10, units = "cm")
  df
}

root = "Coding/data/model"
files = dir(root, full.names = TRUE)
save_root = "performance/population"
save_performance(files[2], name = "Wearing_Lipstick", save_root)

root = "Coding/data/model_sampling"
files = dir(root, full.names = TRUE)
save_root = "performance/sampling"
save_performance(files[2], name = "Wearing_Lipstick", save_root)




root = "Coding/data/model"
files = dir(root, full.names = TRUE)
files[2]
dir(files[2])

models = dir(files[2])
ls = list()
a = c()
for (i in seq_along(models[1:5])) {
  for (j in seq_along(models[1:5])) {
    a[(i - 1) * length(models[1:5]) + j] = (i - 1) * length(models[1:5]) + j
  }
}

models = dir(files[2])
ls = vector("list", length = 25)
for (i in seq_along(models[1:5])) {
  for (j in seq_along(models[1:5])) {
    x = sample(1:100, 10)
    y = sample(1:100, 10)
    ls[[(i - 1) * length(models[1:5]) + j]] = 
      tibble(
        model_x = models[i], 
        model_y = models[j], 
        pvalue = t.test(x, y, alternative = "greater")$p.value,
      )
  }
}
bind_rows(ls) %>% 
  arrange(pvalue) %>% 
  top_n(5, model_x) %>% 
  pull(model_x)


samples = list(
  sample(1:100, 10),
  sample(1:100, 10),
  sample(1:100, 10),
  sample(1:100, 10),
  sample(1:100, 10)
)
models = dir(files[2])
ls = vector("list", length = 5)
for (i in seq_along(models[1:5])) {
  pvalue = c()
  x = samples[[i]]
  for (j in seq_along(models[1:5])) {
    y = samples[[j]]
    pvalue[j] = t.test(x, y, alternative = "greater")$p.value
  }
  ls[[i]] = tibble(!!models[i] := pvalue)
}

df_pvalue = bind_cols(ls) %>% 
  mutate(model = models[1:5], .before = 1) %>% 
  group_by(model) %>% 
  mutate_at(vars(-group_cols()), ~ .x < 0.5) %>% 
  ungroup()

df_top = df_pvalue %>% 
  select(-model) %>% 
  summarise_all(sum) %>% 
  pivot_longer(everything(), names_to = "model", values_to = "top") %>% 
  mutate(top = top + 1) %>% 
  arrange(top)



csvs = dir(files[2], pattern = ".csv", full.names = TRUE, recursive = TRUE)
df = tibble(bind_rows(map(csvs, read.csv)))
df %>% 
  filter(index == 19)


?t.test
t.test(c(1:10), c(11:20), "greater")
t.test(c(1:10), c(11:20), "less")


df2 = tibble(
  x = c(1:10),
  y = c(11:20),
)
df3 = df2 %>% 
  pivot_longer(c("x", "y")) %>% 
  mutate(name = factor(name))
t.test(value ~ name, data = df3, alternative = "less")

x = c(1:10)
y = c(11:20)-5
(x-y)>0
t.test(x, y, data = df3, alternative = "greater") # p-value, smaller better
t.test(y, x, data = df3, alternative = "greater")

tibble(x = "model1", y = "model2", pvalue = )
t.test(x, y, alternative = "greater")$p.value

m = matrix(c(1:9), 3)
idx = which(m == 8, arr.ind = TRUE)
# row
idx[1]
# col
idx[2]
typeof(idx)
class(idx)
m

(x-y)>0

df2 = tibble(
  x = c(11:20),
  y = c(1:10),
)
df3 = df2 %>% 
  pivot_longer(c("x", "y")) %>% 
  mutate(name = factor(name))
ttest = t.test(value ~ name, data = df3, alternative = "less")
ttest$

t.test(name ~ value, data = df3)
t.test(x ~ y, data = df2)
sleep

