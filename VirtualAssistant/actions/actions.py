# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from __future__ import print_function

from rasa_sdk.events import AllSlotsReset
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase

import datetime
from datetime import datetime, timedelta
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pickle



class ActionToggleLight(Action):
    def name(self) -> Text:
        return "action_toggle_light"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,domain: Dict[Text, Any],
        ) -> List[Dict[Text, Any]]:
        # Your Adafruit IO credentials

        adafruit_io_username = "your_username"
        adafruit_io_key = "your_key"

        # Get the intent and extract relevant information from the tracker
        intent = tracker.latest_message['intent'].get('name')

        # Adjust the following logic based on your specific Rasa intents
        if intent == 'turn_on_light':
            # Make a request to turn on the button on Adafruit server
            url = f"https://io.adafruit.com/api/v2/{adafruit_io_username}/feeds/your_button_feed/data"
            headers = {"X-AIO-Key": adafruit_io_key}
            data = {"value": "1"}
            response = requests.post(url, json=data, headers=headers)

            if response.status_code == 200:
                dispatcher.utter_message("Light turned on.")
            else:
                dispatcher.utter_message("Failed to turn on the button.")

        elif intent == 'turn_off_light':
            # Make a request to turn off the button on Adafruit server
            url = f"https://io.adafruit.com/api/v2/{adafruit_io_username}/feeds/your_button_feed/data"
            headers = {"X-AIO-Key": adafruit_io_key}
            data = {"value": "0"}
            response = requests.post(url, json=data, headers=headers)

            if response.status_code == 200:
                dispatcher.utter_message("Light turned off.")
            else:
                dispatcher.utter_message("Failed to turn off the button.")

        return []


class AddEventToCalendar(Action):

    def name(self) -> Text:
        return "action_add_event"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        event_name = tracker.get_slot('event')
        time = tracker.get_slot('time')
        new_time = datetime.strptime(time, '%d/%m/%y %H:%M:%S')

        add_event(event_name, new_time)

        dispatcher.utter_message(text="Event Added")

        return [AllSlotsReset()]


class getEvent(Action):

    def name(self) -> Text:
        return "action_get_event"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        event_name = get_event()

        print(event_name)
        # confirmed_event = tracker.get_slot(Any)
        dispatcher.utter_message(text="got events {name}".format(name=event_name))
        return []


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

CREDENTIALS_FILE = 'credentials.json'


def get_calendar_service():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service


def add_event(event_name, time):
    # creates one hour event tomorrow 10 AM IST
    service = get_calendar_service()

    #    d = datetime.now().date()
    #    tomorrow = datetime(d.year, d.month, d.day, 10)+timedelta(days=1)
    #    start = tomorrow.isoformat()
    end = (time + timedelta(hours=1)).isoformat()

    event_result = service.events().insert(calendarId='primary',
                                           body={
                                               "summary": event_name,
                                               "description": 'This is a tutorial example of automating google calendar with python',
                                               "start": {"dateTime": time.isoformat(), "timeZone": 'Etc/GMT+7'},
                                               "end": {"dateTime": end, "timeZone": 'Etc/GMT+7'},
                                           }
                                           ).execute()

    print("created event")
    print("id: ", event_result['id'])
    print("summary: ", event_result['summary'])
    print("starts at: ", event_result['start']['dateTime'])
    print("ends at: ", event_result['end']['dateTime'])


def get_event():
    service = get_calendar_service()
    now = datetime.utcnow().isoformat() + 'Z'
    events = service.events().list(calendarId='primary', timeMin=now,
                                   maxResults=10, singleEvents=True,
                                   orderBy='startTime').execute().get("items", [])

    print(events[0]["summary"])
    return events[0]["summary"]


def do_event():
    service = get_calendar_service()
    now = datetime.utcnow().isoformat() + 'Z'
    events = service.events().list(calendarId='primary', timeMin=now,
                                   maxResults=10, singleEvents=True,
                                   orderBy='startTime').execute().get("items", [])

    print(events[0]["end"])
    return events[0]["end"]




class ActionDoEvent(Action):

    def name(self) -> Text:
        return "action_do_event"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        event_name = do_event()

        print(event_name)
        # confirmed_event = tracker.get_slot(Any)
        dispatcher.utter_message(text="got events {name}".format(name=event_name))
        return []


class ActionMyKB(ActionQueryKnowledgeBase):
    def __init__(self):
        # load knowledge base with data from the given file
        knowledge_base = InMemoryKnowledgeBase("knowledge_base_data.json")

        # overwrite the representation function of the hotel object
        # by default the representation function is just the name of the object
        knowledge_base.set_representation_function_of_object(
            "hotel", lambda obj: obj["name"] + " (" + obj["city"] + ")"
        )

        super().__init__(knowledge_base)


class ActionInformWeather(Action):
    def name(self) -> Text:
        return "action_inform_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Get the necessary slots from the tracker
        api_key = tracker.get_slot("api_key")

        # Initialize an empty dictionary to store data for each feed
        adafruit_data = {}

        for device_id in device_ids:
            # Make a request to the Adafruit server for each feed
            adafruit_url = f"https://io.adafruit.com/api/v2/{device_id}/feeds"
            headers = {"X-AIO-Key": api_key}

            try:
                response = requests.get(adafruit_url, headers=headers)
                data = response.json()

                # Extract relevant information from the response
                # Modify this part based on the actual structure of the Adafruit response
                relevant_info = data["your_desired_key"]

                # Store the relevant information in the dictionary
                adafruit_data[device_id] = relevant_info

            except Exception as e:
                # Handle errors for each feed appropriately
                dispatcher.utter_message(
                    f"An error occurred while fetching data from Adafruit server for {device_id}: {str(e)}")

                # Set None for the feed that encountered an error
                adafruit_data[device_id] = None

        # Send the collected information to the user
        for device_id, info in adafruit_data.items():
            if info is not None:
                dispatcher.utter_message(f"The data from Adafruit server for {device_id} is: {info}")

        # Set a slot with the fetched data (optional)
        return [SlotSet("adafruit_data", adafruit_data)]
