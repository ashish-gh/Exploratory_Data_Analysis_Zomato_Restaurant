from django.test import TestCase
from rest_framework.test import APIClient

class EndpointTests(TestCase):

    def test_predict_view(self):
        client = APIClient()
        input_data = {
            "votes": 97,
            "average_cost": 7,
            "word_count": 158,
            "has_table_booking": 0,
            "has_online_delivery": 0,
            "is_delivering_now": 0
                    }
        
        classifier_url = "/api/v1/rate_classifier/predict"
        response = client.post(classifier_url, input_data, format='json')
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.data["rate"], "<=50K")
        self.assertTrue("request_id" in response.data)
        self.assertTrue("status" in response.data)