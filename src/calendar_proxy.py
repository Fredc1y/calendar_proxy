# Calendar Proxy
# Copyright (c) 2024 Frederik Schinner | f@schinner.dev
#
# Released under the MIT License.
# See the LICENSE file in the project root for more information.

import requests
import json
from icalendar import Calendar, Event
# from datetime import datetime
from .utils import calculate_event_id
# import hashlib

app = Flask(__name__)

CALENDAR_URL = ""
JSON_FILE = "data/events.json"
DELETED_EVENTS_FILE = "data/deleted_events.json"

HOST = '127.0.0.1'
PORT = 5000

# fetches all calendar events from the CALENDAR_URL and parse them into the json
# if they fulfill all requirements.
def fetch_and_parse_events():
    try:
        with open(JSON_FILE, "r") as f:
            previous_events = json.load(f)
    except FileNotFoundError:
        previous_events = {}

    deleted_events = load_deleted_events()

    response = requests.get(CALENDAR_URL)
    response.raise_for_status()
    
    calendar = Calendar.from_ical(response.content)
    hashes = set()

    for component in calendar.walk():
        if component.name == "VEVENT":
            event_data = {
                "summary": str(component.get("SUMMARY")),
                "dtstart": component.get("DTSTART").dt,
                "dtend": component.get("DTEND").dt,
                "location": str(component.get("LOCATION")),
                "user_added": False
            }
            event_id = calculate_event_id(event_data)

            if event_id in deleted_events:
                continue

            hashes.add(event_id)
            
            if event_id not in previous_events:
                previous_events[event_id] = event_data

    # Remove all outdated (deleted in the remote calendar) events from the json
    previous_events = {
        k: v for k, v in previous_events.items() if k in hashes or v.get("user_added", False)
    }

    save_events(previous_events)


def load_events():
    with open(JSON_FILE, "r") as f:
        return json.load(f)

def save_events(events):
    with open(JSON_FILE, "w") as f:
        json.dump(events, f, indent=4, default=str)

def load_deleted_events():
    try:
        with open(DELETED_EVENTS_FILE, "r") as f:
            return set(json.load(f))
    except FileNotFoundError:
        return set()

def save_deleted_events(deleted_events):
    with open(DELETED_EVENTS_FILE, "w") as f:
        json.dump(list(deleted_events), f, indent=4)


if __name__ == "__main__":
    fetch_and_parse_events()
    app.run(host=HOST, port=PORT)