import os
import json
import firebase_admin
from firebase_admin import credentials

# Path to the secret file
service_account_path = "/etc/secrets/service_account"

try:
    # Read the plain text file
    with open(service_account_path, 'r') as f:
        service_account_json = f.read()

    # Parse the JSON content
    service_account_dict = json.loads(service_account_json)

    # Initialize Firebase Admin SDK using the parsed JSON
    cred = credentials.Certificate(service_account_dict)
    firebase_admin.initialize_app(cred)

except Exception as e:
    raise Exception(f"Error initializing Firebase Admin SDK: {e}")
