# loading and checking raw data ----
# Folder and image files
root = 'dataset/'
img_folder = str_c(root, 'img_align_celeba/img_align_celeba')
img_index = str_c(img_folder, "/", dir(img_folder))

# CSV files
df_attr = read_csv('dataset/list_attr_celeba.csv') # 40 attributes
df_bbox = read_csv('dataset/list_bbox_celeba.csv') # bounding box cover the entire face
df_mark = read_csv('dataset/list_landmarks_align_celeba.csv') # feature locations


# Table of attributes
tb_attr = tibble(
  Index = 1:40,
  Attributes = names(df_attr)[-1],
)
kbl(tb_attr) %>% 
  kable_styling(bootstrap_options = c("striped", "hover", "condensed"))
