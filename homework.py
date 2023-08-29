from bs4 import BeautifulSoup
import codecs
import datetime as dt
from datetime import date
import calendar
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/calendar"]

class new_assignment:
    def __init__(self, deadline, importance, lesson, task) -> None:
        self.deadline = deadline
        self.importance = importance
        self.lesson = lesson
        self.task = task

    

    def goog(self):
        creds = None

        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json")

        # if not creds or not creds.valid:
        #     if creds and creds.expired and creds.refresh_token:
        #         creds.refresh(Request())
        #     else:
        flow = InstalledAppFlow.from_client_secrets_file("C:\prog_questionmark\Calendar\keys\key.json", SCOPES)
        creds = flow.run_local_server(port=0)
            
        with open("token.json", "w") as token:
            token.write(creds.to_json())
        
        try:
            service = build("calendar", "v3", credentials=creds)

            now = dt.datetime.now().isoformat() + "Z"

            event_result = service.events().list(calendarId="primary", timeMin = now, maxResults=2, singleEvents=True, orderBy="startTime").execute()
            events = event_result.get("items", [])

            homework = [value for value in events if value["summary"] == "Homework"]
            # print(homework)
            homework[0]["description"] = homework[0]["description"]+f"\n{self.deadline} {self.importance} {self.lesson} {self.task}"
            service.events().update(calendarId = "skoralal4@gmail.com", eventId = "6nsls2o6eh5qev0cdcomeasm5r", body = homework[0]).execute()
            calendar_list = service.calendarList().list().execute()
            # print(calendar_list)
            

            
            for event in events:
                start = event["start"].get("dateTime", event["start"].get("date"))
                # print(start, event)

        except HttpError as error:
            print("eerroorr", error)

