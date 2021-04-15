from modules.event import *

event_1 = Event("15/04/21", "Cheese Conference", 100, "Bree Room", "Conference for Cheese Lovers", True)
event_2 = Event("30/04/21", "Wedding", 50, "Rose Room", "Wedding for sad people", False)
events = [event_1, event_2]

def add_new_event(event):
    events.append(event)