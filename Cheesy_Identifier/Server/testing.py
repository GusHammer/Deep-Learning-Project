import tensorflow as tf
import os
from tensorflow import keras
from PIL import Image
import numpy as np

model = keras.models.load_model("model")

path = os.getcwd()

os.chdir("../Database/cheese_photos")
train_dir = os.getcwd()
train_classes_dirs = []
classes = []

for directory in os.listdir():
	train_classes_dirs.append(os.path.join(train_dir, directory))
	classes.append(directory)

os.chdir(path)

test = Image.open("cam.png")
test = test.resize((128,128))
test = np.array(test)
if test.shape[2] == 4:
	test = test[:, :, :3]
predictions = model.predict([[test]])
highest = 0
value = 0
print(predictions)
for item in range(len(predictions[0])):
	if predictions[0][item] > value:
		highest = item
		value = predictions[0][item]
		
print(classes[int(highest)])