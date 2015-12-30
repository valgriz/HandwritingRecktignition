""" Converts image to usable format (i.e. pixel array) and runs classifier on it """
from preprocess_images import *
import os
import numpy as np

img = "temp"
img_matrix = img_to_matrix(image)
data = flatten_image(img_matrix)

# Run classifier

