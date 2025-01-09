import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Specify the absolute path to the service_account.json file
SERVICE_ACCOUNT_PATH = "/etc/secrets/service_account"

# Check if the service account file exists
if not os.path.exists(SERVICE_ACCOUNT_PATH):
    raise FileNotFoundError(f"Service account file not found at: {SERVICE_ACCOUNT_PATH}")

# Initialize Firebase Admin SDK
cred = credentials.Certificate(SERVICE_ACCOUNT_PATH)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://musify-2ad60-default-rtdb.asia-southeast1.firebasedatabase.app'
})
