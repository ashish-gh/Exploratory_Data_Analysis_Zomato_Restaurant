from django.test import TestCase

import inspect
from apps.ml.classifier.lstm import LstmClassifier
from apps.ml.classifier.lstm import LstmClassifier

class MLTest(TestCase):

    def test_lstm_algorithm(self):

        input_data = {"votes": 97,
                "average_cost": 7,
                "word_count": 158,
                "has_table_booking": 0,
                "has_online_delivery": 0,
                "is_delivering_now": 0
                }
        
        lstm = LstmClassifier()
        response = lstm.compute_prediction(input_data)
        self.assertEqual('OK', response['status'])
        # self.assertTrue('rate' in response)
        # self.assertEqual(-0.0042696763, response['rate'])
