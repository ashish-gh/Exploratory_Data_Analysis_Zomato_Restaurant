"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
application = get_wsgi_application()

import inspect 
from apps.ml.registry import MLRegistry
from apps.ml.rate_classifier.lstm import LstmClassifier

try:
    registry = MLRegistry() # create ML registry
    # LSTM
    lstm = LstmClassifier()
    # add to ML registry
    registry.add_algorithm(endpoint_name="rate_classifier",
                            algorithm_object=lstm,
                            algorithm_name="lstm",
                            algorithm_status="production",
                            algorithm_version="0.0.1",
                            owner="Ashish",
                            algorithm_description="LSTM with simple pre and post processing",
                            algorithm_code=inspect.getsource(LstmClassifier))

except Exception as e:
    print("Exception while loading the algorithms to the registry,", str(e))
