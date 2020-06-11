import os
import pandas as pd
import numpy as np
import tensorflow as tf
from keras.models import load_model
from sklearn.preprocessing import StandardScaler
# from keras.preprocessing.text import Tokenizer


class LstmClassifier:
    def __init__(self):
        path_to_artifacts = os.path.dirname('../../research/')
        my_file = os.path.join(path_to_artifacts, 'lstm_model_2.h5')
        self.model = load_model(my_file)

    def preprocessing(self, input_data):

        votes = np.int64(input_data["votes"]) 
        average_cost = np.int64(input_data["average_cost"])
        word_count = np.int64(input_data["word_count"])
        has_table_booking = np.int64(input_data["has_table_booking"])
        has_online_devilery = np.int64(input_data["has_online_delivery"])
        is_delivering_now = np.int64(input_data["is_delivering_now"])

        # 2.2 Numerical Features: 
        votes_pred = votes.reshape(-1, 1)
        avg_cost_pred = average_cost.reshape(-1, 1)
        word_count_pred = word_count.reshape(-1, 1)
        has_table_booking_pred = has_table_booking.reshape(-1, 1)
        has_online_delivery_pred = has_online_devilery.reshape(-1, 1)
        is_delivering_now_pred = is_delivering_now.reshape(-1, 1)

        ## Concate Numerical features
        input_data = np.concatenate((votes_pred, avg_cost_pred,word_count_pred, has_table_booking_pred, has_online_delivery_pred, is_delivering_now_pred), axis = 1)

        scaler = StandardScaler()
        input_data = scaler.fit_transform(input_data)

        return input_data


    def predict(self, input_data):
        return self.model.predict(input_data)

    def postprocessing(self, input_data):
        return {
            "rate": input_data[0],  
            "status": "OK"
            }

    def compute_prediction(self, input_data):
        try:
            input_data = self.preprocessing(input_data)
            prediction = self.predict(input_data)[0]  # only one sample
            prediction = self.postprocessing(prediction)
        except Exception as e:
            return {"status": "Error", "message": str(e)}

        return prediction