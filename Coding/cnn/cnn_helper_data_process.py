# retrieve one attribute for two categorical training
def cnnAttr(df, attrs):
  return keras.utils.to_categorical(np.asarray((df[attrs]+1)/2), 2)

df_attr = pd.read_csv('dataset/list_attr_celeba.csv') # 40 attributes
y=cnnAttr(df_attr, 'Wearing_Lipstick')
# check
y.shape

# save Sequential model and its History object
def cnnSave(model, history, root, name):
    rn=root+'/'+name
    model.save(rn+'.h5')
    df=pd.DataFrame.from_dict(history.history)
    df.to_pickle(rn+'.pkl')
    df['model']=name.title() # or name.capitalize()
    df.to_csv(rn+'.csv', index_label='index')
# load model and History object as DataFrame
def cnnLoad(root, name):
    rn=root+'/'+name
    model=keras.models.load_model(rn+'.h5')
    history=pd.read_pickle(rn+'.pkl')
    return model, history
# examples
model=keras.Sequential([...], 'model_name')
history=model.fit(x, y, batch_size=batch_size, epochs=epochs, validation_split=0.1)
## root to save
root_model_save='Coding/data/model/lipstick'
# save it
cnnSave(model, history, root_model_save, 'lipstick_dropout')
# delete the objects
del model, history
# load for future use
model,history=cnnLoad(root_model_save, 'lipstick_dropout')
