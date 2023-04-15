import numpy as np
import scipy
import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras.preprocessing.image import ImageDataGenerator

model = keras.Sequential([
    layers.Conv2D(16, 3, padding='same', activation='relu', input_shape=(224, 224, 3)),
    layers.MaxPooling2D(),
    layers.Conv2D(32, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(64, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(5)
])


model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])


datagen = ImageDataGenerator(rescale=1./255)


train_data = datagen.flow_from_directory('train/',
                                         target_size=(224, 224),
                                         batch_size=32,
                                         class_mode='sparse')
val_data = datagen.flow_from_directory('val/',
                                       target_size=(224, 224),
                                       batch_size=32,
                                       class_mode='sparse')


history = model.fit(train_data, validation_data=val_data, epochs=10)


test_data = datagen.flow_from_directory('test/',
                                        target_size=(224, 224),
                                        batch_size=32,
                                        class_mode='sparse')
test_loss, test_acc = model.evaluate(test_data)
print('Test accuracy:', test_acc)

model.save('model')
