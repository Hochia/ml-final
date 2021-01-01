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

def getModels(cnn, dnn, op, name, input_shape):
  return keras.Sequential([keras.Input(shape=input_shape), cnn(), dnn(), op()], name)

def getModels2(cnn, dnn, op, name, input_shape):
  model=keras.Sequential([keras.Input(shape=input_shape), cnn(), dnn(), op()], name)
  return model.summary()
