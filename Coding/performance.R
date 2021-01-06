# Use unpaired two sample t-test to compare the performance
# Save the plot of the performance

# choose the last epoch
best_performance = function(df) {
  df %>% 
    filter(index == max(.$index)) %>% 
    arrange(desc(val_categorical_accuracy)) %>% 
    select(model, categorical_accuracy, val_categorical_accuracy)
}
# transform the data for plot
list_performance = function(df) {
  df %>% 
    pivot_longer(contains(c("accuracy", "loss"))) %>% 
    mutate(
      perform = case_when(str_detect(name, "accuracy") ~ "accuracy", str_detect(name, "loss") ~ "loss", TRUE ~ ""),
      setting = case_when(str_detect(name, "val") ~ "validation", TRUE ~ "training"),
    )
}
choose_model = function(df, model) {
  df %>% 
    filter(model == !!model) %>% 
    pull(val_categorical_accuracy)
}
help_compare_load = function(file) {
  csvs = dir(file, pattern = ".csv", full.names = TRUE, recursive = TRUE)
  df = tibble(bind_rows(map(csvs, read.csv)))
}
help_compare_test = function(models, df) {
  ls = vector("list", length = length(models))
  
  for (i in seq_along(models)) {
    pvalue = c()
    x = choose_model(df, models[i])
    for (j in seq_along(models)) {
      y = choose_model(df, models[j])
      pvalue[j] = t.test(x, y, alternative = "greater")$p.value
    }
    ls[[i]] = tibble(!!models[i] := pvalue)
  }
  
  df_pvalue = bind_cols(ls) %>% 
    mutate(model = models, .before = 1)
  
  df_top = df_pvalue %>% 
    group_by(model) %>% 
    mutate_at(vars(-group_cols()), ~ .x < 0.05) %>% 
    ungroup() %>%  
    select(-model) %>% 
    summarise_all(sum) %>% 
    pivot_longer(everything(), names_to = "model", values_to = "top") %>% 
    mutate(top = as.integer(as.factor(n() - top))) %>% 
    arrange(top)
  
  list(df_top, df_pvalue)
}
compare_performance = function(file) {
  help_compare_test(dir(file), help_compare_load(file))
}
compare_sampling_performance = function(file) {
  help_compare_test(dir(file), best_performance(help_compare_load(file)))
}
plot_performance = function(df) {
  ggplot(df, aes(index, value)) +
    geom_line(aes(color = setting)) +
    scale_y_continuous(breaks = seq(0, 1, 0.2), limits = c(0, 1)) +
    facet_grid(vars(perform), vars(model)) +
    guides(color = guide_legend(title = NULL)) +
    labs(x = "epochs", y = NULL) +
    theme_test() +
    theme(legend.position = "top")
}
plot_sampling_performance = function(df) {
  ggplot(df, aes(index, value)) +
    geom_line(aes(color = setting)) +
    scale_y_continuous(breaks = seq(0, 1, 0.2), limits = c(0, 1)) +
    facet_grid(vars(perform), vars(model)) +
    guides(color = guide_legend(title = NULL)) +
    labs(x = "sampling process", y = NULL) +
    theme_test() +
    theme(legend.position = "top")
}
help_save_performance = function(df, file, name, save_root = "performance/population") {
  ls_best_performance = compare_performance(file)
  # list performance
  df_list_performance = list_performance(df) %>% 
    mutate(model = factor(model, ls_best_performance[[1]]$model))
  # top 5 performance
  df_top5_performance = df_list_performance %>% 
    filter(model %in% ls_best_performance[[1]]$model[1:5])
  list(df_list_performance, df_top5_performance, ls_best_performance)
}
save_performance = function(file, name, save_root = "performance/population") {
  csvs = dir(file, pattern = ".csv", full.names = TRUE, recursive = TRUE)
  ls = tibble(bind_rows(map(csvs, read.csv))) %>% 
    help_save_performance(file, name, save_root)
  ## all models plot
  plt = plot_performance(ls[[1]])
  ggsave(str_c(save_root, paste0(name, ".png"), sep = "/"), plt, width = 100, height = 10, units = "cm")
  ## top 5 models plot
  plt = plot_performance(ls[[2]])
  ggsave(str_c(save_root, paste0(name, "_top5.png"), sep = "/"), plt, width = 15, height = 10, units = "cm")
  ls[[3]]
}
save_sampling_performance = function(file, name, save_root = "performance/population") {
  csvs = dir(file, pattern = ".csv", full.names = TRUE, recursive = TRUE)
  ls = tibble(bind_rows(map(csvs, read.csv))) %>% 
    filter(index == max(.$index)) %>% 
    select(model, everything()) %>% 
    group_by(model) %>% 
    arrange(val_categorical_accuracy) %>% 
    mutate(index = row_number()) %>% 
    ungroup() %>% 
    help_save_performance(file, name, save_root)
  ## all models plot
  plt = plot_sampling_performance(ls[[1]])
  ggsave(str_c(save_root, paste0(name, ".png"), sep = "/"), plt, width = 100, height = 10, units = "cm")
  ## top 5 models plot
  plt = plot_sampling_performance(ls[[2]])
  ggsave(str_c(save_root, paste0(name, "_top5.png"), sep = "/"), plt, width = 15, height = 10, units = "cm")
  ls[[3]]
}

# plot of population
root = "Coding/data/model"
files = dir(root, full.names = TRUE)
save_root = "performance/population"
WL = save_performance(
  files[str_detect(files, "Wearing_Lipstick")],
  name = "Wearing_Lipstick",
  save_root
)
WL %>% 
  summarise_if(is.double, list(min, max)) %>% 
  pivot_longer(everything())
WL %>% 
  filter(index == 19) %>% 
  View()

# NB = save_performance(
#   files[str_detect(files, "No_Beard")],
#   name = "No_Beard",
#   save_root
# )
# NB %>% 
#   filter(index == 19) %>% 
#   View()
# NB %>% 
#   filter(index == 19) %>% 
#   .[,2:5] %>% 
#   summary()
# summary(NB[,2:5])
# NB %>% 
#   summarise_if(is.double, list(min, max)) %>% 
#   pivot_longer(everything())

file = files[str_detect(files, "Chubby_Adam")]
csvs = dir(file, pattern = ".csv", full.names = TRUE, recursive = TRUE)
df = tibble(bind_rows(map(csvs, read.csv)))
plt = df %>% 
  list_performance() %>% 
  plot_performance()
ggsave('performance/population/Chubby_Adam.png', plt, width = 100, height = 10, units = "cm")

file = files[str_detect(files, "Chubby_SGD")]
csvs = dir(file, pattern = ".csv", full.names = TRUE, recursive = TRUE)
df = tibble(bind_rows(map(csvs, read.csv)))
plt = df %>% 
  list_performance() %>% 
  plot_performance()
ggsave('performance/population/Chubby_SGD.png', plt, width = 100, height = 10, units = "cm")

# plot of sampling
root = "Coding/data/model_sampling"
files = dir(root, full.names = TRUE)
save_root = "performance/sampling"
sWL = save_sampling_performance(
  files[str_detect(files, "Wearing_Lipstick")],
  name = "Wearing_Lipstick",
  save_root
)
sNB = save_sampling_performance(
  files[str_detect(files, "No_Beard")],
  name = "No_Beard",
  save_root
)
sCh = save_sampling_performance(
  files[str_detect(files, "Chubby")],
  name = "Chubby",
  save_root
)

# rank
WL[[1]]
sWL[[1]]

tblWL = left_join(WL[[1]], sWL[[1]], "model")
names(tblWL) = c("model", "200K", "2K")
tblWL
View(tblWL)
ttblWL = as_tibble(cbind(nms = names(tblWL), t(tblWL)))
write.csv(ttblWL, file = "table/Lipstick.csv")
write.csv()
p=compare_performance(files[str_detect(files, "Wearing_Lipstick")])
View(p[[1]])
