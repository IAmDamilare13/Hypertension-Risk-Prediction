# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle

# Load the Saved Model
loaded_model = pickle.load(open('C:/Users/DAMILARE-PC/Documents/School Materials/UG Project Resources/mlModel/trainedModel.sav', 'rb'))

# Input data
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
