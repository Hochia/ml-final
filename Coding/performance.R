choose_model = function(df, model) {
  df %>% 
    filter(model == !!model) %>% 
    pull(val_categorical_accuracy)
}
compare_performance = function(file) {
  models = dir(file)
  csvs = dir(file, pattern = ".csv", full.names = TRUE, recursive = TRUE)
  df = best_performance(tibble(bind_rows(map(csvs, read.csv))))
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
    mutate_at(vars(-group_cols()), ~ .x < 0.5) %>% 
    ungroup() %>%  
    select(-model) %>% 
    summarise_all(sum) %>% 
    pivot_longer(everything(), names_to = "model", values_to = "top") %>% 
    mutate(top = n() - top) %>% 
    arrange(top)
  
  list(df_top, df_pvalue)
}
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
  csvs = dir(file, pattern = ".csv", full.names = TRUE, recursive = TRUE)
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
plot_sampling_performance = function(df) {
  ggplot(df, aes(index, value)) +
    geom_line(aes(color = setting)) +
    facet_grid(vars(perform), vars(model), scales = "free_y") +
    guides(color = guide_legend(title = NULL)) +
    labs(x = "iteration", y = NULL) +
    theme_test() +
    theme(legend.position = "top")
}
save_sampling_performance = function(file, name, save_root = "performance/population") {
  browser()
  csvs = dir(file, pattern = ".csv", full.names = TRUE, recursive = TRUE)
  df = tibble(bind_rows(map(csvs, read.csv))) %>% 
    filter(index == 19) %>% 
    select(model, everything()) %>% 
    group_by(model) %>% 
    arrange(val_categorical_accuracy) %>% 
    mutate(index = row_number()) %>% 
    ungroup()
  # best performance
  ls_best_performance = compare_performance(file)
  # list performance
  df_list_performance = list_performance(df)
  # top 5 performance
  df_top5_performance = df_list_performance %>% 
    filter(model %in% ls_best_performance[[1]]$model[1:5])
  ## all models plot
  plt = plot_sampling_performance(df_list_performance)
  ggsave(str_c(save_root, paste0(name, ".png"), sep = "/"), plt, width = 100, height = 10, units = "cm")
  ## top 5 models plot
  plt = plot_sampling_performance(df_top5_performance)
  ggsave(str_c(save_root, paste0(name, "_top5.png"), sep = "/"), plt, width = 15, height = 10, units = "cm")
  ls_best_performance
}

root = "Coding/data/model"
files = dir(root, full.names = TRUE)
save_root = "performance/population"
save_performance(
  files[str_detect(files, 'Wearing_Lipstick')],
  name = "Wearing_Lipstick",
  save_root
)

root = "Coding/data/model_sampling"
files = dir(root, full.names = TRUE)
save_root = "performance/sampling"
save_sampling_performance(
  files[str_detect(files, 'Wearing_Lipstick')],
  name = "Wearing_Lipstick",
  save_root
)
compare_performance(files[str_detect(files, 'Wearing_Lipstick')])
