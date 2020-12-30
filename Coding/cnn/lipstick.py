import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
input_shape=(128, 128, 3)
model=keras.Sequential([
    keras.Input(shape=input_shape),
    layers.Conv2D(32, (3,3), activation='relu', padding='same', name='cv1'),
    layers.MaxPool2D((2,2), name='mp1'),
    layers.Conv2D(64, (3,3), activation='relu', padding='same', name='cv2'),
    layers.MaxPool2D((2,2), name='mp2'),
    layers.Conv2D(128, (3,3), activation='relu', padding='same', name='cv3'),
    layers.MaxPool2D((2,2), name='mp3'),
    layers.Conv2D(128, (3,3), activation='relu', padding='same', name='cv4'),
    layers.MaxPool2D((2,2), name='mp4'),
    layers.Flatten(name='ft'),
    layers.Dense(512, activation='relu', name='d1'),
    layers.Dense(2, activation='sigmoid', name='d2'),
], 'Lipstick')
model.summary()
model.compile(optimizer=keras.optimizers.SGD(),
              loss=keras.losses.BinaryCrossentropy(from_logits=True),
              metrics=[keras.metrics.BinaryAccuracy()])
model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['mae', 'acc'])
model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['mae', 'acc'])
batch_size=128
epochs=3
history=model.fit(X, y, batch_size=batch_size, epochs=epochs, validation_split=0.1)

# Model: With dropout layers
del x
x=np.load('Coding/data/img_x_36_26.npy')
y=cnn_load_data(df_attr, 'Wearing_Lipstick')
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
# model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['mae', 'acc'])
batch_size=128
epochs=20
history=model.fit(x, y, batch_size=batch_size, epochs=epochs, validation_split=0.1)


root_model_save='Coding/data/model/lipstick'
cnnSave(model, history, root_model_save, 'lipstick_dropout')
del model, history
model,history=cnnLoad(root_model_save, 'lipstick_dropout')


# TODO:
def plotHistory(dfHistory):
    cn=list(dfHistory.columns)
    plt.plot(dfHistory[cn[0]])
    plt.plot(dfHistory[cn[2]])
    plt.ylabel(cn[0])
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.plot(dfHistory[cn[1]])
    plt.plot(dfHistory[cn[3]])
    plt.ylabel(cn[1])
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()

plt.clf()
plotHistory(history)

list(history_lipstick.columns)
loss
categorical_accuracy
val_loss
val_categorical_accuracy 
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

acc = history2['acc']
val_acc = history2['val_acc']
loss = history2['loss']
val_loss = history2['val_loss']
epochs = range(1, len() + 1)
plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.legend()
plt.figure()
plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.legend()
plt.show()


history2
list(history2)
history2.items()
loss = history2['loss']
acc = history2['accuracy']
val_loss = history2['val_loss']
val_acc = history2['val_accuracy']

epochs = range(1, len(acc)+1)
plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.legend()
plt.show()
plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation losss')
plt.legend()
plt.show()
plt.clf()
