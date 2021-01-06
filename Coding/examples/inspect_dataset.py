# https://www.kaggle.com/danmoller/inspecting-the-celeba-dataset-face-landmarks
# displays for a batch of images as a numpy array basic statistics
def inspect(x, name):
    print(name + ": ", 
          'shape:', x.shape, 
          'min:', x.min(), 
          'max:',x.max(),
          'mean:',x.mean(), 
          'std:', x.std())
# plots the passed images side by side
def plotImages(*images, minVal =0, maxVal = 1):
    fig, ax = plt.subplots(1, len(images), figsize=(13, 4))
    
    for i,image in enumerate(images):
        ax[i].imshow(image,vmin = minVal, vmax=maxVal)
    
    plt.show()

# Creating a batch generator ----
class Reader():
    # creates the generator taking the raw data and a batch size
    def __init__(self, images, attr, bbox, mark, batchSize):
        assert len(images)==len(attr)==len(bbox)==len(mark)
        
        quotient, remainder = divmod(len(images), batchSize)
        self.length = quotient + (1 if remainder > 0 else 0)
        self.batchSize = batchSize
        self.lastSize = remainder if remainder > 0 else batchSize
        self.images = images
        self.attr = (np.array(attr)[:,1:] + 1)/2.
        self.bbox = np.array(bbox)[:,1:]
        self.mark = np.array(mark)[:,1:]
    
    # number of batches
    def __len__(self):
        return self.length
    
    # each batch
    def __getitem__(self, i):
        batch = self.batchSize if i + 1 < len(self) else self.lastSize
        start = i * self.batchSize
        end = start + batch
        
        imgs = list()
        for im in self.images[start:end]:
            imgs.append(np.array(Image.open(im), dtype=np.float64)/255.)
        imgs = np.stack(imgs, axis=0)
        masks = np.zeros(imgs.shape[:3]+(6,))
        
        self.addFaceMasks(self.bbox[start:end], masks)
        self.addMark(self.mark[start:end], masks)
        
        return imgs, masks, self.attr[start:end]
        
    #processes the face bounding boxes into mask images   
    def addFaceMasks(self, bbox, addTo):
        
        #for each face in the batch
        for i, face in enumerate(bbox):
            x, y, w, h = face #gets coordinates and sizes
            
            addTo[i,y:y+h, x:x+w,0] = 1. #updates the masks    
    
    #processes the other coordinates into mask images   
    def addMark(self, mark, addTo):
        
        #for each face in the batch
        for i, locs in enumerate(mark):
            locs = locs.reshape((-1,2))    #reshapes into pairs of coords
            
            #for each pair of coords
            for ch, (posX, posY) in enumerate(locs):
                #20x20 bounding boxes for this coord pair 
                x = posX - 10
                y = posY - 10
                x2 = x + 20
                y2 = y + 20
                if x < 0: x = 0
                if y < 0: y = 0
                    
                addTo[i,y:y2, x:x2,ch+1] = 1.

# Getting batches and visualizing the data ----
generator = Reader(img_index, df_attr, df_bbox, df_mark, 32)

#test 20 batches
for i in range(20):
    imgs, masks, atts = generator[i]
    
    #print the batch shape:
    if i == 0:
        print("image batch shape:", imgs.shape)
        print("masks batch shape:", masks.shape)

    #takes four faded images from the batch (we fade them to add with the masks)
    n = 2 #plotting n images per batch
    imgs = imgs[:n]/2.
    #plotImages(*imgs)
    #gets the face bounding boxes (first channel in the masks array)
    faceM = np.array(masks[:n,:,:,:3]) #we keep 3 channels for compatibility
    faceM[:,:,:,1:] = 0      #we make the non related channels 0
    #gets the other bounding boxes, summing two groups of 3 channels
    #each channel is one feature (remove the face boxes that are above)
    otherM = masks[:n,:,:,:3] + masks[:n,:,:,3:] - faceM
    #pairs of images:
        #bbox + face bounding box
        #bbox + other features bounding boxes
    faceBxs = np.clip(imgs + faceM , 0,1)
    otherBxs = np.clip(imgs + otherM, 0, 1)
    #putting pairs side by side
    imgs = np.stack([faceBxs,otherBxs], axis=1)
    shp = imgs.shape
    imgs = imgs.reshape((-1,) + shp[2:])
    #plotting
    plotImages(*imgs)

