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
attr=attrs[36]
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

# Validate sampling
# Common parameters
sampling_size=2000
iteration=20
batch_size=20
epochs=20
# Set parameters
img_hw=(36,26)
input_shape=(*img_hw, 3)
# Load models
del candidateModels
candidateModels=[getModels(getattr(CnnLys, layers[0]), getattr(DnnLys, layers[1]), OpLy.lydSfm, name, input_shape) for layers,name in zip([(i,j) for i in cnnMethods for j in dnnMethods], nameModel)]
# Model fit
attr=attrs[36]
# Saving root
root_model_save='Coding/data/model_sampling/'+attr+'_36_26'
# Load data
y=cnnAttr(df_attr, attr)
for model, name in zip(candidateModels, nameModel):
    model.compile(
        optimizer=keras.optimizers.SGD(),
        loss=keras.losses.CategoricalCrossentropy(from_logits=True),
        metrics=[keras.metrics.CategoricalAccuracy()]
    )
    itrSamplingModel(iteration, root_model_save, name, model, x, y, sampling_size, batch_size, epochs)
    gc.collect()
    gc.garbage






## Deprecated ---------------------------------------------


# Case 1: image size is 36x26
# Load data
del x
x=np.load('Coding/data/img_x_36_26.npy')
y=cnnAttr(df_attr, 'Wearing_Lipstick')
# Common parameters
batch_size=128
epochs=20
# Saving root
root_model_save='Coding/data/model/lipstick'

# Model: 
# Model name: Lipstick_3626_c3d4d0
# Input shape: 36,26
# Layer description:
#     CNN: 3
#     Dense: 4
#     Dropout: 0
img_hw=(36,26)
input_shape=(*img_hw, 3)
model=keras.Sequential([
    keras.Input(shape=input_shape),
    layers.Conv2D(32, (3,3), (2,2), activation='relu', padding='same', name='cv1'),
    layers.MaxPool2D((2,2), name='mp1'),
    layers.Conv2D(64, (2,2), activation='relu', padding='same', name='cv2'),
    layers.MaxPool2D((2,2), name='mp2'),
    layers.Conv2D(64, (3,3), activation='relu', padding='same', name='cv3'),
    layers.MaxPool2D((2,2), name='mp3'),
    layers.Flatten(name='ft'),
    layers.Dense(32, activation='relu', name='ds1'),
    layers.Dense(16, activation='relu', name='ds2'),
    layers.Dense(8, activation='relu', name='ds3'),
    layers.Dense(2, activation='softmax', name='ds4'),
], 'Lipstick_original')
model.summary()
model.compile(optimizer=keras.optimizers.SGD(),
              loss=keras.losses.CategoricalCrossentropy(from_logits=True),
              metrics=[keras.metrics.CategoricalAccuracy()])
history=model.fit(x, y, batch_size=batch_size, epochs=epochs, validation_split=0.1)

cnnSave(model, history, root_model_save, 'lipstick_original_36_26')
del model, history
# model,history=cnnLoad(root_model_save, 'lipstick_original_36_26')

# Model: With dropout layers
img_hw=(36,26)
input_shape=(*img_hw, 3)
model=keras.Sequential([
    keras.Input(shape=input_shape),
    layers.Conv2D(32, (3,3), (2,2), activation='relu', padding='same', name='cv1'),
    layers.MaxPool2D((2,2), name='mp1'),
    layers.Conv2D(64, (2,2), activation='relu', padding='same', name='cv2'),
    layers.MaxPool2D((2,2), name='mp2'),
    layers.Conv2D(64, (3,3), activation='relu', padding='same', name='cv3'),
    layers.MaxPool2D((2,2), name='mp3'),
    layers.Flatten(name='ft'),
    layers.Dropout(0.5, name='dp1'),
    layers.Dense(32, activation='relu', name='ds1'),
    layers.Dropout(0.5, name='dp2'),
    layers.Dense(16, activation='relu', name='ds2'),
    layers.Dropout(0.3, name='dp3'),
    layers.Dense(8, activation='relu', name='ds3'),
    layers.Dropout(0.2, name='dp4'),
    layers.Dense(2, activation='softmax', name='ds4'),
], 'Lipstick_dropout')
model.summary()
model.compile(optimizer=keras.optimizers.SGD(),
              loss=keras.losses.CategoricalCrossentropy(from_logits=True),
              metrics=[keras.metrics.CategoricalAccuracy()])
history=model.fit(x, y, batch_size=batch_size, epochs=epochs, validation_split=0.1)

root_model_save='Coding/data/model/lipstick'
cnnSave(model, history, root_model_save, 'lipstick_dropout_36_26')
del model, history
# model,history=cnnLoad(root_model_save, 'lipstick_dropout_36_26')

# Model: No dropout layers, rectangel kernel
img_hw=(36,26)
input_shape=(*img_hw, 3)
model=keras.Sequential([
    keras.Input(shape=input_shape),
    layers.Conv2D(32, (3,2), (2,2), activation='relu', padding='same', name='cv1'),
    layers.MaxPool2D((2,2), name='mp1'),
    layers.Conv2D(64, (3,2), activation='relu', padding='same', name='cv2'),
    layers.MaxPool2D((2,2), name='mp2'),
    layers.Conv2D(64, (2,3), activation='relu', padding='same', name='cv3'),
    layers.MaxPool2D((2,2), name='mp3'),
    layers.Flatten(name='ft'),
    layers.Dense(32, activation='relu', name='ds1'),
    layers.Dense(16, activation='relu', name='ds2'),
    layers.Dense(8, activation='relu', name='ds3'),
    layers.Dense(2, activation='softmax', name='ds4'),
], 'Lipstick_noDropoutRectangle')
model.summary()
model.compile(optimizer=keras.optimizers.SGD(),
              loss=keras.losses.CategoricalCrossentropy(from_logits=True),
              metrics=[keras.metrics.CategoricalAccuracy()])
history=model.fit(x, y, batch_size=batch_size, epochs=epochs, validation_split=0.1)

cnnSave(model, history, root_model_save, 'lipstick_noDropoutRectangle_36_26')
del model, history
# model,history=cnnLoad(root_model_save, 'lipstick_noDropoutRectangle_36_26')

# Model: With dropout layers, rectangle kernel
del x
img_hw=(36,26)
input_shape=(*img_hw, 3)
model=keras.Sequential([
    keras.Input(shape=input_shape),
    layers.Conv2D(32, (3,2), (2,2), activation='relu', padding='same', name='cv1'),
    layers.MaxPool2D((2,2), name='mp1'),
    layers.Conv2D(64, (3,2), activation='relu', padding='same', name='cv2'),
    layers.MaxPool2D((2,2), name='mp2'),
    layers.Conv2D(64, (2,3), activation='relu', padding='same', name='cv3'),
    layers.MaxPool2D((2,2), name='mp3'),
    layers.Flatten(name='ft'),
    layers.Dropout(0.5, name='dp1'),
    layers.Dense(32, activation='relu', name='ds1'),
    layers.Dropout(0.5, name='dp2'),
    layers.Dense(16, activation='relu', name='ds2'),
    layers.Dropout(0.3, name='dp3'),
    layers.Dense(8, activation='relu', name='ds3'),
    layers.Dropout(0.2, name='dp4'),
    layers.Dense(2, activation='softmax', name='ds4'),
], 'Lipstick_dropoutRectangle')
model.summary()
model.compile(optimizer=keras.optimizers.SGD(),
              loss=keras.losses.CategoricalCrossentropy(from_logits=True),
              metrics=[keras.metrics.CategoricalAccuracy()])
history=model.fit(x, y, batch_size=batch_size, epochs=epochs, validation_split=0.1)

root_model_save='Coding/data/model/lipstick'
cnnSave(model, history, root_model_save, 'lipstick_dropoutRectangle_36_26')
del model, history
# model,history=cnnLoad(root_model_save, 'lipstick_dropoutRectangle_36_26')

# Model: Deeper, dropout layers, rectangel kernel
img_hw=(36,26)
input_shape=(*img_hw, 3)
model=keras.Sequential([
    keras.Input(shape=input_shape),
    layers.Conv2D(32, (3,2), (2,2), activation='relu', padding='same', name='cv1'),
    layers.MaxPool2D((2,2), name='mp1'),
    layers.Conv2D(64, (3,2), activation='relu', padding='same', name='cv2'),
    layers.MaxPool2D((2,2), name='mp2'),
    layers.Conv2D(64, (2,3), activation='relu', padding='same', name='cv3'),
    layers.MaxPool2D((2,2), name='mp3'),
    layers.Flatten(name='ft'),
    layers.Dropout(0.5, name='dp1'),
    layers.Dense(32, activation='relu', name='ds1'),
    layers.Dropout(0.5, name='dp2'),
    layers.Dense(28, activation='relu', name='ds2'),
    layers.Dropout(0.25, name='dp3'),
    layers.Dense(24, activation='relu', name='ds3'),
    layers.Dropout(0.25, name='dp4'),
    layers.Dense(16, activation='relu', name='ds4'),
    layers.Dropout(0.2, name='dp5'),
    layers.Dense(8, activation='relu', name='ds5'),
    layers.Dense(2, activation='softmax', name='ds6'),
], 'Lipstick_deeperDropoutRectangle')
model.summary()
model.compile(optimizer=keras.optimizers.SGD(),
              loss=keras.losses.CategoricalCrossentropy(from_logits=True),
              metrics=[keras.metrics.CategoricalAccuracy()])
history=model.fit(x, y, batch_size=batch_size, epochs=epochs, validation_split=0.1)

root_model_save='Coding/data/model/lipstick'
cnnSave(model, history, root_model_save, 'lipstick_deeperDropoutRectangle_36_26')
del model, history
# model,history=cnnLoad(root_model_save, 'lipstick_noDropoutRectangle_36_26')

# Model: With dropout layers, rectangle kernel
del x
img_hw=(36,26)
input_shape=(*img_hw, 3)
model=keras.Sequential([
    keras.Input(shape=input_shape),
    layers.Conv2D(32, (3,2), (2,2), activation='relu', padding='same', name='cv1'),
    layers.MaxPool2D((2,2), name='mp1'),
    layers.Conv2D(64, (3,2), activation='relu', padding='same', name='cv2'),
    layers.MaxPool2D((2,2), name='mp2'),
    layers.Conv2D(64, (2,3), activation='relu', padding='same', name='cv3'),
    layers.MaxPool2D((2,2), name='mp3'),
    layers.Flatten(name='ft'),
    layers.Dropout(0.5, name='dp1'),
    layers.Dense(32, activation='relu', name='ds1'),
    layers.Dropout(0.5, name='dp2'),
    layers.Dense(16, activation='relu', name='ds2'),
    layers.Dropout(0.3, name='dp3'),
    layers.Dense(8, activation='relu', name='ds3'),
    layers.Dropout(0.2, name='dp4'),
    layers.Dense(2, activation='softmax', name='ds4'),
], 'Lipstick_dropoutRectangle')
model.summary()
model.compile(optimizer=keras.optimizers.SGD(),
              loss=keras.losses.CategoricalCrossentropy(from_logits=True),
              metrics=[keras.metrics.CategoricalAccuracy()])
history=model.fit(x, y, batch_size=batch_size, epochs=epochs, validation_split=0.1)

cnnSave(model, history, root_model_save, 'lipstick_dropoutRectangle_36_26')
del model, history
# model,history=cnnLoad(root_model_save, 'lipstick_dropoutRectangle_36_26')





# # TODO:
# def plotHistory(dfHistory):
#     cn=list(dfHistory.columns)
#     plt.plot(dfHistory[cn[0]])
#     plt.plot(dfHistory[cn[2]])
#     plt.ylabel(cn[0])
#     plt.xlabel('epoch')
#     plt.legend(['train', 'test'], loc='upper left')
#     plt.plot(dfHistory[cn[1]])
#     plt.plot(dfHistory[cn[3]])
#     plt.ylabel(cn[1])
#     plt.xlabel('epoch')
#     plt.legend(['train', 'test'], loc='upper left')
#     plt.show()
# 
# plt.clf()
# plotHistory(history)
# 
# list(history_lipstick.columns)
# loss
# categorical_accuracy
# val_loss
# val_categorical_accuracy 
# plt.plot(history.history['accuracy'])
# plt.plot(history.history['val_accuracy'])
# plt.title('model accuracy')
# plt.ylabel('accuracy')
# plt.xlabel('epoch')
# plt.legend(['train', 'test'], loc='upper left')
# plt.show()
# # summarize history for loss
# plt.plot(history.history['loss'])
# plt.plot(history.history['val_loss'])
# plt.title('model loss')
# plt.ylabel('loss')
# plt.xlabel('epoch')
# plt.legend(['train', 'test'], loc='upper left')
# plt.show()
# 
# acc = history2['acc']
# val_acc = history2['val_acc']
# loss = history2['loss']
# val_loss = history2['val_loss']
# epochs = range(1, len() + 1)
# plt.plot(epochs, acc, 'bo', label='Training acc')
# plt.plot(epochs, val_acc, 'b', label='Validation acc')
# plt.title('Training and validation accuracy')
# plt.legend()
# plt.figure()
# plt.plot(epochs, loss, 'bo', label='Training loss')
# plt.plot(epochs, val_loss, 'b', label='Validation loss')
# plt.title('Training and validation loss')
# plt.legend()
# plt.show()
# 
# 
# history2
# list(history2)
# history2.items()
# loss = history2['loss']
# acc = history2['accuracy']
# val_loss = history2['val_loss']
# val_acc = history2['val_accuracy']
# 
# epochs = range(1, len(acc)+1)
# plt.plot(epochs, acc, 'bo', label='Training acc')
# plt.plot(epochs, val_acc, 'b', label='Validation acc')
# plt.title('Training and validation accuracy')
# plt.legend()
# plt.show()
# plt.plot(epochs, loss, 'bo', label='Training loss')
# plt.plot(epochs, val_loss, 'b', label='Validation loss')
# plt.title('Training and validation losss')
# plt.legend()
# plt.show()
# plt.clf()
