'''A demo is available in question3demo.jpynb'''

#build neural network
import tensorflow as tf
#store an array locally in the end
import numpy as np
#check the error rate
import matplotlib.pyplot as plt
#import datasets
import pandas as pd
#split the training and testing sets for training the neural network
from sklearn.model_selection import train_test_split
#tools to build neural networks
from keras.models import Sequential
from keras.layers import Dense, Activation
from sklearn.decomposition import PCA
from keras import backend as K

#import data
x_data = pd.read_csv('train_data.txt',delim_whitespace=True)
y_data = pd.read_csv('train_truth.txt',delim_whitespace=True)
x_pred = pd.read_csv('test_data.txt',delim_whitespace=True)

#select 1/3 of the training data as testing dataset for the neural network
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size = 0.33)
n_input = x_train.shape[1]#dimensions3

#create the neural network sequentially
model = Sequential()
#add layers to neural network
model.add(Dense(4, input_dim=n_input,activation='relu'))
model.add(Dense(4, activation="sigmoid"))
model.add(Dense(1))
#use regression loss function and regression matrix
model.compile(optimizer='Adam',loss='mse', metrics=[tf.keras.metrics.MeanSquaredError()])

#train the model, use test data as validation data
history = model.fit(x_train, y_train,validation_data=(x_test,y_test),batch_size=32, epochs=200, verbose=0)
'''
#visualize the overall change in error rate in order to access if the model is trained well
#plot available in the demo
#if want to view the plot locally, unmute/un-comment this session
plt.plot(list(history.history['mean_squared_error']))
plt.plot(list(history.history['val_mean_squared_error']))
plt.title('Model Mean Squared Error')
plt.ylabel('mean_squared_error')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.savefig('MSE.png')
'''
#final output using the trained model and the x_test dataset
y_prediction = model.predict(x_pred)
#write output into files
np.savetxt('test_predicted.txt',y_prediction,header='y')
