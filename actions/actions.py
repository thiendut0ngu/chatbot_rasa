import logging
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

logger = logging.getLogger(__name__)

class ActionAddEvent(Action):
    def name(self) -> Text:
        return "action_add_event"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        event_name = tracker.get_slot("event_name")
        event_date = tracker.get_slot("event_date")
        event_time = tracker.get_slot("event_time")
        attendees = tracker.get_slot("attendees")

        # save event to database or send to external API
        # ...

        dispatcher.utter_message(text=f"Event '{event_name}' added to schedule on {event_date} at {event_time} with attendees {attendees}.")
        return []

class ActionChangeEvent(Action):
    def name(self) -> Text:
        return "action_change_event"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        event_name = tracker.get_slot("event_name")
        event_date = tracker.get_slot("event_date")
        event_time = tracker.get_slot("event_time")
        attendees = tracker.get_slot("attendees")

        # update event in database or send to external API
        # ...

        dispatcher.utter_message(text=f"Event '{event_name}' changed to {event_date} at {event_time} with attendees {attendees}.")
        return []

class ActionRemoveEvent(Action):
    def name(self) -> Text:
        return "action_remove_event"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        event_name = tracker.get_slot("event_name")

        # remove event from database or external API
        # ...

        dispatcher.utter_message(text=f"Event '{event_name}' removed from schedule.")
        return []

class ActionAddAttendee(Action):
    def name(self) -> Text:
        return "action_add_attendee"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        event_name = tracker.get_slot("event_name")
        attendee_name = tracker.get_slot("attendee_name")

        # add attendee to event in database or send to external API
        # ...

        dispatcher.utter_message(text=f"Attendee '{attendee_name}' added to event '{event_name}'.")
        return []

class ActionChangeAttendee(Action):
    def name(self) -> Text:
        return "action_change_attendee"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        event_name = tracker.get_slot("event_name")
        attendee_name = tracker.get_slot("attendee_name")

        # change attendee in event in database or send to external API
        # ...

        dispatcher.utter_message(text=f"Attendee '{attendee_name}' changed in event '{event_name}'.")
        return []

class ActionRemoveAttendee(Action):
    def name(self) -> Text:
        return "action_remove_attendee"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        event_name = tracker.get_slot("event_name")
        attendee_name = tracker.get_slot("attendee_name")

        # remove attendee from event in database or send to external API
        # ...

        dispatcher.utter_message(text=f"Attendee '{attendee_name}' removed from event '{event_name}'.")
        return []

class ScheduleForm(FormAction):
    def name(self) -> Text:
        return "schedule_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return [
            "event_name",
            "event_date",
            "event_time",
            "attendees"
        ]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {
            "event_name": self.from_text(),
            "event_date": self.from_text(),
            "event_time": self.from_text(),
            "attendees": self.from_text()
        }

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        event_name = tracker.get_slot("event_name")

        # check if event already exists in database or external API
        # ...

        if event_name:
            return [
                ActionChangeEvent(),
                ActionChangeAttendee()
            ]