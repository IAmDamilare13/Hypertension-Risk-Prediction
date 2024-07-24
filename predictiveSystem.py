# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle
import os

# Construct the relative path to the model file
model_path = os.path.join(os.path.dirname(__file__), 'trainedModel.sav')

# Load the Saved Model
with open(model_path, 'rb') as model_file:
    loaded_model = pickle.load(model_file)

#Input data
input_data = [[1, 25, 135, 70, 28.54]]

# Convert the input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# Reshape the array for a single instance prediction
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

# Make a prediction
prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

# Interpret the prediction
if prediction[0] == 0:
    print('Good Health')
elif prediction[0] == 1:
    print('Mild Risk of Hypertension')
elif prediction[0] == 2:
    print('High Risk of Hypertension')
else:
    print('Error! Verify Input.')
