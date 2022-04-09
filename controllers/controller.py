from re import A
from secrets import token_bytes
from flask import render_template, request


from app import app
from models.events_list import events
from models.event import Event

@app.route('/events')
def index():
    return render_template("index.html", title="Events", all_events=events)

@app.route('/events', methods=["POST"])
def add_event():
    recurring_status = False
    if request.form.get('recurring') == 'recurring':
        recurring_status = True
    if request.form["date"]:
        events.append(Event(request.form["date"], request.form["title"], request.form["number_of_guests"], request.form["location"], request.form["description"], recurring_status))
    return render_template("index.html", title="Events", all_events=events)

@app.route('/events/delete', methods=["POST"])
def delete_event():
    for event in events:
        if event.title == request.form["delete"]:
            events.remove(event)
    return render_template("index.html", title="Events", all_events=events)