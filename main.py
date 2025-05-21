import os.path 
import datetime as dt

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def main():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=8080)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    try:
        service = build('calendar', 'v3', credentials=creds)

        event = {
            "summary": "adding event through API",
            "location": "from room number: B2T6",
            "description": "this is a test event",
            "colorId": "11",
            "start": {
                "dateTime": "2025-05-21T12:00:00",
                "timeZone": "Asia/Kolkata"
            },
            "end": {
                "dateTime": "2025-05-21T13:00:00",
                "timeZone": "Asia/Kolkata"
            },
            "attendees": [
                {
                    "email": "pragadeeshv.aiml2023@citchennai.net"
                }
            ]
        }
        event = service.events().insert(calendarId='primary', body=event).execute()
        print("Event created: %s" % (event.get('htmlLink')))
    except Exception as e:
        print('An error occurred: %s' % e)

if __name__ == '__main__':
    main()