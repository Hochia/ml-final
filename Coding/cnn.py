# # define cnn model
# def define_model(in_shape=(128, 128, 3), out_shape=40):
#     model = Sequential()
#     model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same', input_shape=in_shape))
#     model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
#     model.add(MaxPooling2D((2, 2)))
#     model.add(Dropout(0.2))
#     model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
#     model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
#     model.add(MaxPooling2D((2, 2)))
#     model.add(Dropout(0.2))
#     model.add(Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
#     model.add(Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
#     model.add(MaxPooling2D((2, 2)))
#     model.add(Dropout(0.2))
#     model.add(Flatten())
#     model.add(Dense(128, activation='relu', kernel_initializer='he_uniform'))
#     model.add(Dropout(0.5))
#     model.add(Dense(out_shape, activation='sigmoid'))
#     # compile model
#     opt = SGD(lr=0.01, momentum=0.9)
#     model.compile(optimizer=opt, loss='binary_crossentropy', metrics='acc')
#     return model
# 
# model = define_model()
# 
# 
# from sklearn.model_selection import train_test_split
# trainX, testX, trainY, testY = train_test_split(X, y, test_size=0.3, random_state=1)
# 
# from keras.preprocessing.image import ImageDataGenerator
# datagen = ImageDataGenerator(rescale=1.0/255.0)
# train_it = datagen.flow(trainX[0:1000,:,:], trainY[0:1000,:], batch_size=20)
# test_it = datagen.flow(testX[1000:2000,:,:], testY[1000:2000,:], batch_size=20)
# 
# # from tensorflow.keras import backend
# 
# history = model.fit(train_it, steps_per_epoch=len(train_it),
#     validation_data=test_it, validation_steps=len(test_it), epochs=30)
# 
# def summarize_diagnostics(history):
#     # plot loss
#     plt.subplot(211)
#     plt.title('Cross Entropy Loss')
#     plt.plot(history.history['loss'], color='blue', label='train')
#     plt.plot(history.history['val_loss'], color='orange', label='test')
#     # plot accuracy
#     plt.subplot(212)
#     plt.title('Fbeta')
#     plt.plot(history.history['acc'], color='blue', label='train')
#     plt.plot(history.history['val_acc'], color='orange', label='test')
#     plt.show()
# 
# summarize_diagnostics(history)
# 


from sklearn.model_selection import train_test_split
trainX, testX, trainY, testY = train_test_split(X, y, test_size=0.3, random_state=1)

from keras.preprocessing.image import ImageDataGenerator
datagen = ImageDataGenerator(rescale=1.0/255.0)
train_it = datagen.flow(trainX[0:1000,:,:], trainY[0:1000,:], batch_size=20)
test_it = datagen.flow(testX[1000:2000,:,:], testY[1000:2000,:], batch_size=20)

# load saved data
df_attr = pd.read_csv('dataset/list_attr_celeba.csv') # 40 attributes
X=np.load('Coding/data/img_x.npy')[0:100,:,:]/255
y=keras.utils.to_categorical(np.asarray((df_attr["Wearing_Lipstick"]+1)/2)[0:10000], 2)
# check
X.shape
y.shape

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
], "Lipstick")
model.summary()
model.compile(optimizer=keras.optimizers.SGD(),
              loss=keras.losses.BinaryCrossentropy(from_logits=True),
              metrics=[keras.metrics.BinaryAccuracy()])
model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=["mae", "acc"])
batch_size=50
epochs=3
history=model.fit(X, y, batch_size=batch_size, epochs=epochs, validation_split=0.1)
# history=model.fit(X[1:100,:,:,:], y[1:100,:], batch_size=batch_size, epochs=epochs, validation_split=0.1)

# model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
model.fit(X, y, batch_size=batch_size, epochs=epochs, validation_split=0.1)

# practice
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
input_shape = (128, 128, 3)

model = keras.Sequential([
    layers.Dense(2, activation="relu", name="layer"),
    layers.Dense(3, activation="relu", name="layer222"),
    layers.Dense(4, name="layer3"),
])
x = tf.ones((3, 3))
y = model(x)
len(model.weights)
model.weights[2]
model.weights[3]
model.weights[4]
model.weights[5]
model.summary()

layers.Dense(4, name="layer3").weights
model = Sequential


inner_model = keras.Sequential(
    [
        keras.Input(shape=(3,)),
        keras.layers.Dense(3, activation="relu"),
        keras.layers.Dense(3, activation="relu"),
    ]
)

model = keras.Sequential(
    [keras.Input(shape=(3,)), keras.layers.Dense(3, activation="relu"), inner_model, keras.layers.Dense(3, activation="sigmoid"),]
)

model.trainable = True
inner_model.trainable = False

model.trainable = False  # Freeze the outer model
model.summary()
inner_model.summary()
model.layers[0].trainable
model.layers[1].trainable
model.layers[2].trainable
assert inner_model.trainable == False  # All layers in `model` are now frozen
assert inner_model.layers[0].trainable == False  # `trainable` is propagated recursively




