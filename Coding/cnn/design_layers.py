class CnnLys:
  # C11
  def ly_c11c21():
    return keras.Sequential([
      layers.Conv2D(32, (3,3), (2,2), activation='relu', padding='same', name='cv1'),
      layers.MaxPool2D((2,2), name='mp1'),
      layers.Conv2D(64, (2,2), activation='relu', padding='same', name='cv2'),
      layers.MaxPool2D((2,2), name='mp2'),
      layers.Flatten(name='ft'),
    ], 'cnn_layers')
  # C12
  def ly_c11dc21d():
    return keras.Sequential([
      layers.Conv2D(32, (3,3), (2,2), activation='relu', padding='same', name='cv1'),
      layers.MaxPool2D((2,2), name='mp1'),
      layers.Dropout(0.5, name='cdp1'),
      layers.Conv2D(64, (2,2), activation='relu', padding='same', name='cv2'),
      layers.MaxPool2D((2,2), name='mp2'),
      layers.Dropout(0.3, name='cdp2'),
      layers.Flatten(name='ft'),
    ], 'cnn_layers')
  # C21
  def ly_c11c21c31():
    return keras.Sequential([
      layers.Conv2D(32, (3,3), (2,2), activation='relu', padding='same', name='cv1'),
      layers.MaxPool2D((2,2), name='mp1'),
      layers.Conv2D(64, (2,2), activation='relu', padding='same', name='cv2'),
      layers.MaxPool2D((2,2), name='mp2'),
      layers.Conv2D(64, (3,3), activation='relu', padding='same', name='cv3'),
      layers.MaxPool2D((2,2), name='mp3'),
      layers.Flatten(name='ft'),
    ], 'cnn_layers')
  # C22
  def ly_c11dc21dc31d():
    return keras.Sequential([
      layers.Conv2D(32, (3,3), (2,2), activation='relu', padding='same', name='cv1'),
      layers.MaxPool2D((2,2), name='mp1'),
      layers.Dropout(0.2, name='cdp1'),
      layers.Conv2D(64, (2,2), activation='relu', padding='same', name='cv2'),
      layers.MaxPool2D((2,2), name='mp2'),
      layers.Dropout(0.3, name='cdp2'),
      layers.Conv2D(64, (3,3), activation='relu', padding='same', name='cv3'),
      layers.MaxPool2D((2,2), name='mp3'),
      layers.Dropout(0.5, name='cdp3'),
      layers.Flatten(name='ft'),
    ], 'cnn_layers')
  # C31
  def ly_c12c22c32():
    return keras.Sequential([
      layers.Conv2D(32, (3,3), (2,2), activation='relu', padding='same', name='cv11'),
      layers.Conv2D(64, (2,2), activation='relu', padding='same', name='cv12'),
      layers.Conv2D(128, (2,2), activation='relu', padding='same', name='cv13'),
      layers.MaxPool2D((2,2), name='mp1'),
      layers.Conv2D(64, (2,2), activation='relu', padding='same', name='cv21'),
      layers.Conv2D(32, (2,2), (2,2), activation='relu', padding='same', name='cv22'),
      layers.MaxPool2D((2,2), name='mp2'),
      layers.Flatten(name='ft'),
    ], 'cnn_layers')
  # C32
  def ly_c12dc22dc32d():
    return keras.Sequential([
      layers.Conv2D(32, (3,3), (2,2), activation='relu', padding='same', name='cv11'),
      layers.Conv2D(64, (2,2), activation='relu', padding='same', name='cv12'),
      layers.Conv2D(128, (2,2), activation='relu', padding='same', name='cv13'),
      layers.MaxPool2D((2,2), name='mp1'),
      layers.Dropout(0.5, name='cdp1'),
      layers.Conv2D(64, (2,2), activation='relu', padding='same', name='cv21'),
      layers.Conv2D(32, (2,2), (2,2), activation='relu', padding='same', name='cv22'),
      layers.MaxPool2D((2,2), name='mp2'),
      layers.Dropout(0.5, name='cdp2'),
      layers.Flatten(name='ft'),
    ], 'cnn_layers')

class DnnLys:
  # D11
  def lyd32d16d8():
    return keras.Sequential([
      layers.Dense(32, activation='relu', name='ds1'),
      layers.Dense(16, activation='relu', name='ds2'),
      layers.Dense(8, activation='relu', name='ds3'),
    ], 'dnn_layers')
  # D12
  def lyd32dd16dd8d():
    return keras.Sequential([
      layers.Dense(32, activation='relu', name='ds1'),
      layers.Dropout(0.5, name='ddp1'),
      layers.Dense(16, activation='relu', name='ds2'),
      layers.Dropout(0.3, name='ddp2'),
      layers.Dense(8, activation='relu', name='ds3'),
      layers.Dropout(0.2, name='ddp2'),
    ], 'dnn_layers')
  # D21
  def lyd128d32d8():
    return keras.Sequential([
      layers.Dense(128, activation='relu', name='ds1'),
      layers.Dense(32, activation='relu', name='ds2'),
      layers.Dense(8, activation='relu', name='ds3'),
    ], 'dnn_layers')
  # D22
  def lyd128dd32dd8d():
    return keras.Sequential([
      layers.Dense(128, activation='relu', name='ds1'),
      layers.Dropout(0.5, name='ddp1'),
      layers.Dense(32, activation='relu', name='ds2'),
      layers.Dropout(0.3, name='ddp2'),
      layers.Dense(8, activation='relu', name='ds3'),
      layers.Dropout(0.2, name='ddp2'),
    ], 'dnn_layers')
  # D31
  def lyd128d64d32d16d8():
    return keras.Sequential([
      layers.Dense(128, activation='relu', name='ds1'),
      layers.Dense(64, activation='relu', name='ds2'),
      layers.Dense(32, activation='relu', name='ds3'),
      layers.Dense(16, activation='relu', name='ds4'),
      layers.Dense(8, activation='relu', name='ds5'),
    ], 'dnn_layers')
  # D32
  def lyd128dd64dd32dd16dd8d():
    return keras.Sequential([
      layers.Dense(128, activation='relu', name='ds1'),
      layers.Dropout(0.5, name='ddp1'),
      layers.Dense(64, activation='relu', name='ds2'),
      layers.Dropout(0.5, name='ddp2'),
      layers.Dense(32, activation='relu', name='ds3'),
      layers.Dropout(0.3, name='ddp3'),
      layers.Dense(16, activation='relu', name='ds4'),
      layers.Dropout(0.3, name='ddp4'),
      layers.Dense(8, activation='relu', name='ds5'),
      layers.Dropout(0.3, name='ddp5'),
    ], 'dnn_layers')

class OpLy:
  def lydSfm():
    return keras.Sequential([
      layers.Dense(2, activation='softmax', name='op'),
    ], 'output_layer')

def testModels(cnn, dnn, op, name, input_shape):
  return keras.Sequential([keras.Input(shape=input_shape), cnn(), dnn(), op()], name)

def testModels2(cnn, dnn, op, name, input_shape):
  model=keras.Sequential([keras.Input(shape=input_shape), cnn(), dnn(), op()], name)
  return model.summary()


import math
nameModel=['C'+str(math.floor(i/2+1))+str(i%2+1)+'D'+str(math.floor(j/2+1))+str(j%2+1) for i in range(0,6) for j in range(0,6)]
cnnMethods=[method for method in dir(CnnLys)[-6:]]
dnnMethods=[method for method in dir(DnnLys)[-6:]]
candidateModels=[testModels(getattr(CnnLys, layers[0]), getattr(DnnLys, layers[1]), OpLy.lydSfm, name, input_shape) for layers,name in zip([(i,j) for i in cnnMethods for j in dnnMethods], nameModel)]
candidateCNN=[model.layers[0].summary for model in candidateModels]
candidateDNN=[model.layers[1].summary for model in candidateModels]
candidateModels


[layers, name for layers,name in zip([(i,j) for i in cnnMethods for j in dnnMethods], nameModel)]
[layers, name for layers,name in zip([(i,j) for i in cnnMethods for j in dnnMethods], nameModel)]

[(layers, name) for layers,name in zip([(i,j) for i in cnnMethods for j in dnnMethods], nameModel)]

for x,y in zip([(i,j) for i in cnnMethods for j in dnnMethods], range(0,36)):
  print(x[0],x[1],y)

for x, y in zip(for i in cnnMethods for j in dnnMethods, for k in range(0,6)):

for x,y in zip()

testModels(getattr(CnnLys, cnnMethods[0]), DnnLys.lyd128d32d8, OpLy.lydSfm, 'C11D11', input_shape)

testModels(CnnLys.ly_c11c21, DnnLys.lyd128d32d8, OpLy.lydSfm, 'C11D11', input_shape)
testModels(CnnLys.ly_c11c21, DnnLys.lyd128d64d32d16d8, OpLy.lydSfm, 'C11D12', input_shape)
testModels(CnnLys.ly_c11c21, DnnLys.lyd128dd32dd8d, OpLy.lydSfm, 'C11D21', input_shape)
testModels(CnnLys.ly_c11c21, DnnLys.lyd128dd64dd32dd16dd8d, OpLy.lydSfm, 'CD', input_shape)
testModels(CnnLys, DnnLys, OpLy.lydSfm, 'CD', input_shape)
testModels(CnnLys, DnnLys, OpLy.lydSfm, 'CD', input_shape)
testModels(CnnLys, DnnLys, OpLy.lydSfm, 'CD', input_shape)
testModels(CnnLys, DnnLys, OpLy.lydSfm, 'CD', input_shape)
testModels(CnnLys, DnnLys, OpLy.lydSfm, 'CD', input_shape)
testModels(CnnLys, DnnLys, OpLy.lydSfm, 'CD', input_shape)
testModels(CnnLys, DnnLys, OpLy.lydSfm, 'CD', input_shape)
testModels(CnnLys, DnnLys, OpLy.lydSfm, 'CD', input_shape)
testModels(CnnLys, DnnLys, OpLy.lydSfm, 'CD', input_shape)







def cnn_ly():
  return keras.Sequential([
    layers.Conv2D(32, (3,3), (2,2), activation='relu', padding='same', name='cv1'),
    layers.MaxPool2D((2,2), name='mp1'),
    layers.Conv2D(64, (2,2), activation='relu', padding='same', name='cv2'),
    layers.MaxPool2D((2,2), name='mp2'),
    layers.Conv2D(64, (3,3), activation='relu', padding='same', name='cv3'),
    layers.MaxPool2D((2,2), name='mp3'),
    layers.Flatten(name='ft'),
  ], 'cnn_layers')

def cnn_ly2():
  return keras.Sequential([
    layers.Conv2D(32, (3,3), (2,2), activation='relu', padding='same', name='cv1'),
    layers.Conv2D(64, (2,2), activation='relu', padding='same', name='cv2'),
    layers.MaxPool2D((2,2), name='mp2'),
    layers.Conv2D(64, (3,3), activation='relu', padding='same', name='cv3'),
    layers.MaxPool2D((2,2), name='mp3'),
    layers.Flatten(name='ft'),
  ], 'cnn_layers')

def dnn_ly():
  return keras.Sequential([
    layers.Dense(32, activation='relu', name='ds1'),
    layers.Dense(16, activation='relu', name='ds2'),
    layers.Dense(8, activation='relu', name='ds3'),
    layers.Dense(2, activation='softmax', name='ds4'),
  ], 'dnn_layers')

def dnn_ly2():
  return keras.Sequential([
    layers.Dense(128, activation='relu', name='ds1'),
    layers.Dense(64, activation='relu', name='ds1'),
    layers.Dense(32, activation='relu', name='ds1'),
    layers.Dense(16, activation='relu', name='ds2'),
    layers.Dense(8, activation='relu', name='ds3'),
    layers.Dense(2, activation='softmax', name='ds4'),
  ], 'dnn_layers')



model=keras.Sequential([keras.Input(shape=input_shape), cnn_ly(), dnn_ly(),], name)
model.summary()


name = 'm1'
model=keras.Sequential([keras.Input(shape=input_shape), cnn_ly(), dnn_ly(),], name)
model.summary()
model=keras.Sequential([keras.Input(shape=input_shape), cnn_ly(), dnn_ly2(),], name)
model.summary()
model=keras.Sequential([keras.Input(shape=input_shape), cnn_ly2(), dnn_ly(),], name)
model.summary()
model=keras.Sequential([keras.Input(shape=input_shape), cnn_ly2(), dnn_ly2(),], name)
model.summary()

model=keras.Sequential([keras.Input(shape=input_shape), CnnLys.ly_c11c21c31(), dnn_ly(),], name)
model.summary()
model.layers[0].summary()
model=keras.Sequential([keras.Input(shape=input_shape), cnn_ly2(), dnn_ly2(),], name)
model.summary()



dnn_layers=keras.Sequential([
    layers.Dense(32, activation='relu', name='ds1'),
    layers.Dense(16, activation='relu', name='ds2'),
    layers.Dense(8, activation='relu', name='ds3'),
    layers.Dense(2, activation='softmax', name='ds4'),
], 'dnn_layers')

name = 'm1'
model=keras.Sequential([
    keras.Input(shape=input_shape),
    cnn_ly(),
    dnn_ly(),
], name)
model.summary()

name = 'm1'
model=keras.Sequential([
    keras.Input(shape=input_shape),
    cnn_ly2(),
    dnn_ly(),
], name)
model.summary()

cnn_layers=keras.Sequential([
    layers.Conv2D(32, (3,3), (2,2), activation='relu', padding='same', name='cv1'),
    layers.MaxPool2D((2,2), name='mp1'),
    layers.Conv2D(64, (2,2), activation='relu', padding='same', name='cv2'),
    layers.MaxPool2D((2,2), name='mp2'),
    layers.Conv2D(64, (3,3), activation='relu', padding='same', name='cv3'),
    layers.MaxPool2D((2,2), name='mp3'),
    layers.Flatten(name='ft'),
], 'cnn_layers')
dnn_layers=keras.Sequential([
    layers.Dense(32, activation='relu', name='ds1'),
    layers.Dense(16, activation='relu', name='ds2'),
    layers.Dense(8, activation='relu', name='ds3'),
    layers.Dense(2, activation='softmax', name='ds4'),
], 'dnn_layers')
name = 'm1'
model=keras.Sequential([
    keras.Input(shape=input_shape),
    cnn_layers,
    # keras.Sequential([keras.Input(shape=cnn_layers.layers[-1].output_shape)]),
    dnn_layers,
], name)
model.summary()



cnn_layers=keras.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', padding='same', name='cv1'),
    layers.Conv2D(64, (2,2), activation='relu', padding='same', name='cv2'),
    layers.MaxPool2D((2,2), name='mp1'),
    layers.MaxPool2D((2,2), name='mp2'),
    layers.Conv2D(64, (3,3), activation='relu', padding='same', name='cv3'),
    layers.MaxPool2D((2,2), name='mp3'),
    layers.Flatten(name='ft'),
], 'cnn_layers')
dnn_layers=keras.Sequential([
    layers.Dense(32, activation='relu', name='ds1'),
    layers.Dense(16, activation='relu', name='ds2'),
    layers.Dense(8, activation='relu', name='ds3'),
    layers.Dense(2, activation='softmax', name='ds4'),
], 'dnn_layers')
name = 'm1'
model2=keras.Sequential([
    keras.Input(shape=input_shape),
    cnn_layers,
    # keras.Sequential([keras.Input(shape=cnn_layers.layers[-1].output_shape)]),
    dnn_layers,
], name)
model2.summary()



name = 'm1'
model=keras.Sequential([
    keras.Input(shape=input_shape),
    cnn_layers,
    # keras.Sequential([keras.Input(shape=cnn_layers.layers[-1].output_shape)]),
    dnn_layers,
], name)
model.summary()
cnn_layers.summary()
dnn_layers.summary()

cnn_layers.layers[-1].output_shape


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
