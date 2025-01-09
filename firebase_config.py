import os
import json
import firebase_admin
from firebase_admin import credentials

# Path to the secret file
SERVICE_ACCOUNT_PATH = "/etc/secrets/service_account"  # Adjusted for Render secrets

try:
    # Check if the secret file exists
    if os.path.exists(SERVICE_ACCOUNT_PATH):
        # Read the plain text file
        with open(SERVICE_ACCOUNT_PATH, 'r') as f:
            service_account_json = f.read()

        # Parse the JSON content
        service_account_dict = json.loads(service_account_json)

        # Initialize Firebase Admin SDK using the parsed JSON
        cred = credentials.Certificate(service_account_dict)
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://musify-2ad60-default-rtdb.asia-southeast1.firebasedatabase.app'
        })
    else:
        raise FileNotFoundError(f"Service account file not found at: {SERVICE_ACCOUNT_PATH}")

except json.JSONDecodeError:
    raise Exception("Failed to parse the service account JSON. Ensure the file content is valid JSON.")
except Exception as e:
    raise Exception(f"Error initializing Firebase Admin SDK: {e}")
