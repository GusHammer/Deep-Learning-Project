import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
from PIL import Image
import pickle

batch_size = 128
epochs = 75
height = 128
width = 128

modelPath = os.getcwd()
os.chdir("../Database/cheese_photos")
train_dir = os.getcwd()
train_classes_dirs = []
classes = []

for directory in os.listdir():
	train_classes_dirs.append(os.path.join(train_dir, directory))
	classes.append(directory)

train_image_generator = ImageDataGenerator(horizontal_flip=True, vertical_flip=True, width_shift_range=0.2, height_shift_range=0.2, rotation_range=30)
train_data_gen = train_image_generator.flow_from_directory(batch_size=2000, directory=train_dir, shuffle=True, target_size=(height,width), class_mode="categorical")

test_image_generator = ImageDataGenerator(horizontal_flip=True, vertical_flip=True, width_shift_range=0.2, height_shift_range=0.2, rotation_range=30)
test_data_gen = train_image_generator.flow_from_directory(batch_size=128, directory=train_dir, shuffle=True, target_size=(height,width), class_mode="categorical")

train_images, train_classes = next(train_data_gen)
train_labels = []
for image in train_classes:
	for i in range(len(image)):
		if image[i] == 1:
			train_labels.append(i)
			break
			
test_images, test_classes = next(test_data_gen)
test_labels = []
for image in test_classes:
	for i in range(len(image)):
		if image[i] == 1:
			test_labels.append(i)
			break

model = keras.models.Sequential([
    Conv2D(16, 3, padding='same', activation='relu', input_shape=(height, width ,3)),
    MaxPooling2D(),
    Conv2D(32, 3, padding='same', activation='relu'),
    MaxPooling2D(),
    Conv2D(64, 3, padding='same', activation='relu'),
    MaxPooling2D(),
    Conv2D(128, 1, padding='same', activation='relu'),
    MaxPooling2D(),
    Conv2D(256, 1, padding='same', activation='relu'),
    MaxPooling2D(),
    Conv2D(512, 1, padding='same', activation='relu'),
    MaxPooling2D(),
    Flatten(),
    Dense(512, activation='relu'),
    Dense(len(train_classes_dirs), 'softmax')
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
print(model.summary())
model.fit(train_images, train_labels, batch_size=128, validation_data=(test_images,test_labels), epochs=epochs)

os.chdir(modelPath)
model.save("model")
