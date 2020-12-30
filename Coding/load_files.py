# loading and checking raw data ----
# Folder and image files
root = 'dataset/'
img_folder = root + 'img_align_celeba/img_align_celeba'
img_index = [img_folder + "/" + f for f in sorted(os.listdir(img_folder))]

# CSV files 
df_attr = pd.read_csv(root + 'list_attr_celeba.csv') # 40 attributes
df_bbox = pd.read_csv(root + 'list_bbox_celeba.csv') # bounding box cover the entire face
df_mark = pd.read_csv(root + 'list_landmarks_align_celeba.csv') # feature locations

# (np.array(df_attr)[:,1:] + 1) / 2
# 
# # image information
# np.array(Image.open(img_index[0])).shape
# np.array(Image.open(img_index[0]), dtype=np.float64)/255.
