from flask import render_template, request
from app import app
from modules.event_list import events, add_new_event
from modules.event import Event

@app.route('/')
def index():
    return "Welcome!"

@app.route('/upcoming_events')
def upcoming_events():
    return render_template('upcoming_events.html', title='Our Upcoming Events', events=events)

@app.route('/upcoming_events', methods=['POST'])
def add_event():
    eventDate = request.form['eventDate']
    eventName = request.form['eventName']
    eventGuests = request.form['eventGuest']
    eventLocation = request.form['eventLocation']
    eventDesc = request.form['eventDesc']
    eventRepeat = True if 'eventRepeat' in request.form else False
    newEvent = Event(date=eventDate, name_of_event=eventName, number_of_guests=eventGuests, room_location=eventLocation, description=eventDesc, repeat=eventRepeat)
    add_new_event(newEvent)

    return render_template('upcoming_events.html', title='Our Upcoming Events', events=events)