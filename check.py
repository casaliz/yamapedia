import sys, os
from PIL import Image
import numpy as np
import pandas as pd
from keras.models import model_from_json

if len(sys.argv) <= 1:
  quit()

image_size = 200
input_dir = '10types'
categories = [name for name in os.listdir(input_dir) if name != ".DS_Store"]

X = []
for file_name in sys.argv[1:]:
  img = Image.open(file_name)
  img = img.convert("RGB")
  img = img.resize((image_size, image_size))
  in_data = np.asarray(img)
  X.append(in_data)

X = np.array(X)
model = model_from_json(open('model_structure.json').read())
model.load_weights('model.h5')

predict = model.predict(X)

print(predict)

for pre in predict:
  y = pre.argmax()
  print("answer : ", categories[y])
