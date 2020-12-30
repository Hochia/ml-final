def plotImages(img_file_names, nrow, ncol):
    k = [(i,j) for i in range(0,nrow) for j in range(0,ncol)]
    fig, ax = plt.subplots(nrow,ncol,figsize=(10,10),constrained_layout=True)
    for i in range(0,nrow*ncol):
        ax[k[i]].imshow(imread(img_file_names[i]))
        ax[k[i]].axis("tight")
        ax[k[i]].axis('off')
    plt.subplots_adjust(wspace=0,hspace=0)
    plt.show()
    plt.clf()

plotImages(img_index,4,10)

def showPretreatImage(imgs, nrow, ncol):
    k = [(i,j) for i in range(0,nrow) for j in range(0,ncol)]
    fig, ax = plt.subplots(nrow,ncol,figsize=(10,10),constrained_layout=True)
    for i in range(0,nrow*ncol):
        ax[k[i]].imshow(imgs[i,:,:,:])
        ax[k[i]].axis('off')
    plt.subplots_adjust(wspace=0,hspace=0)
    plt.show()

def pretreatImage(imgs, target_size):
    photos = list()
    for img in imgs:
        photo = load_img(img, target_size=target_size)
        photo = img_to_array(photo, dtype='uint8')
        photos.append(photo)
    return np.asarray(photos, dtype='uint8')/255

# photos=pretreatImage(img_index[0:40], (218,178))
# photos=pretreatImage(img_index[0:40], (32,26))
# showPretreatImage(photos,4,10)

x=pretreatImage(img_index, (36,26))
# np.save('Coding/data/img_x_36_26',x)
x=pretreatImage(img_index, (32,26))
# np.save('Coding/data/img_x_32_26',x)
