import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
API_VERSION = 'v1'


flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
creds = flow.run_local_server(port=0)

service = build('gmail', API_VERSION, credentials=creds)

results = service.users().labels().list(userId='me').execute()
labels = results.get('labels', [])
print("Labels:")
for label in labels:
    print(label['name'])

results = service.users().messages().list(userId='me').execute()
messages = results.get('messages', [])
print("\nEmail Messages:")
for message in messages:
    msg = service.users().messages().get(userId='me', id=message['id']).execute()
    print(f"Subject: {msg['subject']}")
    print(f"From: {msg['from']}")
    print(f"Date: {msg['internalDate']}")
    print(f"Snippet: {msg['snippet']}")
    print("\n")

