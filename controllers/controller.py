from flask import render_template, request

from app import app
from models.events_list import *
from models.event import Event
from src.functions import get_input, get_date, get_date_data


@app.route('/events')
def index():
    return render_template("index.html", title="Events", all_events=events)

@app.route('/events', methods=["POST"])
def add_event():
    recurring_status = False
    date_list = request.form['date'].split('-')
    year = get_date_data(date_list)[0]
    month = get_date_data(date_list)[1]
    day = get_date_data(date_list)[2]
    if request.form.get('recurring') :
        recurring_status = True
    if request.form["date"]:
        events.append(Event(get_date(year, month, day), get_input("title"), request.form["number_of_guests"], request.form["location"], request.form["description"], recurring_status))
    return render_template("index.html", title="Events", all_events=events)

@app.route('/events/delete', methods=["POST"])
def delete_event():
    for event in events:
        if event.title == request.form["delete"]:
            events.remove(event)
    return render_template("index.html", title="Events", all_events=events)