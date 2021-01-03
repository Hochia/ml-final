# # Load data
# attrs=['5_o_Clock_Shadow','Arched_Eyebrows','Attractive','Bags_Under_Eyes','Bald','Bangs','Big_Lips','Big_Nose','Black_Hair','Blond_Hair','Blurry','Brown_Hair','Bushy_Eyebrows','Chubby','Double_Chin','Eyeglasses','Goatee','Gray_Hair','Heavy_Makeup','High_Cheekbones','Male','Mouth_Slightly_Open','Mustache','Narrow_Eyes','No_Beard','Oval_Face','Pale_Skin','Pointy_Nose','Receding_Hairline','Rosy_Cheeks','Sideburns','Smiling','Straight_Hair','Wavy_Hair','Wearing_Earrings','Wearing_Hat','Wearing_Lipstick','Wearing_Necklace','Wearing_Necktie','Young']
# x=np.load('Coding/data/img_x_36_26.npy')
# Common parameters
iteration=1
batch_size=20
epochs=20
# Set parameters
img_hw=(36,26)
input_shape=(*img_hw, 3)
# Load models
del candidateModels
candidateModels=[getModels(getattr(CnnLys, layers[0]), getattr(DnnLys, layers[1]), OpLy.lydSfm, name, input_shape) for layers,name in zip([(i,j) for i in cnnMethods for j in dnnMethods], nameModel)]
# Model fit
attr=attrs[1]
# Saving root
root_model_save='Coding/data/model/'+attr+'_36_26'
# Load data
y=cnnAttr(df_attr, attr)
for model, name in zip(candidateModels, nameModel):
    model.compile(
        optimizer=keras.optimizers.SGD(),
        loss=keras.losses.CategoricalCrossentropy(from_logits=True),
        metrics=[keras.metrics.CategoricalAccuracy()]
    )
    itrModel(iteration, root_model_save, name, model, x, y, batch_size, epochs)
    gc.collect()
    gc.garbage


