def itrModel(itr, root, name, model, x, y, batch_size, epochs):
  for i in range(1, itr+1):
    history=model.fit(x, y, batch_size=batch_size, epochs=epochs, validation_split=0.1, verbose=0)
    root_itr=root+'/'+name+'/itr_'+str(i)
    cnnSave(model, history, root_itr, name)

# # examples
# # Load data
# x=np.load('Coding/data/img_x_36_26.npy')[0:100,:,:,:]
# y=cnnAttr(df_attr, 'Wearing_Lipstick')[0:100,:]
# # Common parameters
# batch_size=20
# epochs=20
# # Saving root
# root_model_save='Coding/data/model/lipstick'
# # Model
# img_hw=(36,26)
# input_shape=(*img_hw, 3)
# name = 'model_name'
# model=keras.Sequential([...], name)
# model.summary()
# model.compile(optimizer=keras.optimizers.SGD(),
#               loss=keras.losses.CategoricalCrossentropy(from_logits=True),
#               metrics=[keras.metrics.CategoricalAccuracy()])
# itrModel(20, root_model_save, name, model, x, y, batch_size, 2)
