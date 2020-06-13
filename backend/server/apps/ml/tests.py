from django.test import TestCase

import inspect
from apps.ml.registry import MLRegistry

from apps.ml.rate_classifier.lstm import LstmClassifier
from apps.ml.rate_classifier.lstm import LstmClassifier


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


    # add below method to MLTests class:
    def test_registry(self):
        registry = MLRegistry()
        self.assertEqual(len(registry.endpoints), 0)
        endpoint_name = "rate_classifier"
        algorithm_object = LstmClassifier()
        algorithm_name = "lstm"
        algorithm_status = "production"
        algorithm_version = "0.0.1"
        algorithm_owner = "Ashish"
        algorithm_description = "Lstm simple pre-preocessing"
        algorithm_code = inspect.getsource(LstmClassifier)
        # add to registry
        registry.add_algorithm(endpoint_name, algorithm_object, algorithm_name,
                    algorithm_status, algorithm_version, algorithm_owner,
                    algorithm_description, algorithm_code)
        # there should be one endpoint available
        self.assertEqual(len(registry.endpoints), 1)