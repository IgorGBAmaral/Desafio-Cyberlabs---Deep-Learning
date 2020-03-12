import tensorflow as tf
import numpy as np
import keras as k
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator

classifier = tf.keras.Sequential()

classifier.add(tf.keras.layers.Conv2D(32, (3, 3), input_shape=(64, 64, 3), activation='relu'))
classifier.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))

classifier.add(tf.keras.layers.Conv2D(32, (3, 3), activation='relu'))
classifier.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))

classifier.add(tf.keras.layers.Flatten())

classifier.add(tf.keras.layers.Dense(units=128, activation='relu'))
classifier.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

validation_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory('/content/drive/My Drive/Igor_CyberLabs/Object detection/Train',
                                                 target_size=(64, 64),
                                                 batch_size=32,
                                                 class_mode='binary')

validation_set = validation_datagen.flow_from_directory('/content/drive/My Drive/Igor_CyberLabs/Object detection/Test',
                                                        target_size=(64, 64),
                                                        batch_size=32,
                                                        class_mode='binary')

classifier.fit(training_set,
               epochs=5,
               steps_per_epoch=160,
               validation_data=validation_set,
               validation_steps=2000)

test_image = image.load_img('/content/drive/My Drive/Igor_CyberLabs/Object detection/Test/Gol Test/5895075.jpg',
                            target_size=(64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)

result = classifier.predict(test_image)
result = round(result[0][0])

print(result)
print('----------------')

# print (training_set.class_indices)

if result == 1:
    prediction = 'Gol'
else:
    prediction = 'Azul'

print(prediction)

