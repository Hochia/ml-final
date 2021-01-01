df_attr %>% 
  select(-image_id) %>% 
  mutate_if(is.double, ~ (.x + 1) / 2) %>% 
  summarise_all(list(min, max))
  summarise_all(list(match = sum, not_match = n))

attr_smy = df_attr %>% 
  select(-image_id) %>% 
  mutate_if(is.double, ~ (.x + 1) / 2) %>% 
  pivot_longer(cols = everything(), names_to = "Attributes", values_to = "Match") %>% 
  group_by(Attributes) %>% 
  summarise(
    match = sum(Match),
    not_match = n() - match,
    ratio = mean(Match),
    nratio = 1 - mean(Match),
    .groups = "drop"
  ) %>% 
  mutate(Attributes = factor(Attributes, levels = arrange(., ratio)))

attr_smy

kbl(attr_smy) %>% 
  kable_styling(bootstrap_options = c("striped", "hover", "condensed"))


attr_ratio = attr_smy %>% 
  arrange(ratio) %>% 
  mutate(Attributes = factor(Attributes, levels = .$Attributes), y = ratio) %>% 
  pivot_longer(ratio:nratio, names_to = "ratio", values_to = "value") %>% 
  group_by(Attributes) %>% 
  mutate(y = case_when(ratio == "nratio" ~ y + 0.03, TRUE ~ y))
  
attr_ratio

ggplot(attr_ratio, aes(Attributes, value, fill = ratio, color = ratio, width = .8)) +
  geom_col(position = "fill") +
  scale_fill_manual(
    name = NULL,
    breaks = c("ratio", "nratio"),
    labels = c("Match", "Not Match"), 
    values = c("#D6BEFA", "#F5E3C9")
  ) +
  scale_color_manual(
    name = NULL,
    breaks = c("ratio", "nratio"),
    labels = c("Match", "Not Match"),
    values = c("#6504BA", "#FF8800")
  ) +
  new_scale_color() +
  geom_text(aes(Attributes, y, label = label_percent(accuracy = 0.01)(value), color = rep(c("#41197D", "#B55700"), 40), hjust = 1.1, vjust = 0.5), size = 2.5) +
  scale_y_continuous(breaks = seq(0, 1, 0.2)) +
  scale_color_manual(
    name = NULL,
    breaks = c("#41197D", "#B55700"),
    values = c("#41197D", "#B55700"),
    guide = NULL
  ) +
  labs(x = NULL, y = NULL) +
  coord_flip() +
  theme_test() +
  theme(legend.position="top", legend.box = "horizontal")

