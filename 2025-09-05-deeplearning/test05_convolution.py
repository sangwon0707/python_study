import numpy as np, sys
import matplotlib.pyplot as plt
import os
import tensorflow as tf
import keras

from keras.datasets import mnist
from keras import Sequential, Input
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.utils import to_categorical

seed = 0
np.random.seed(seed)
tf.random.set_seed(seed)
(X_train, Y_class_train), (X_test, Y_class_test) = mnist.load_data()

print("Study-Set image : %d " % (X_train.shape[0]))
print("Test-Set image : %d " % (X_test.shape[0]))