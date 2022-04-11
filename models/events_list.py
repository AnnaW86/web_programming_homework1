import datetime

from models.event import Event

def get_date(year, month, day):
    return datetime.date(year, month, day).strftime("%d/%m/%Y")


event1 = Event(get_date(2022, 3, 28), 'Benjamin\'s birthday', 17, "RCP", "Kids' softplay. Woo!", True)
event2 = Event(get_date(2022, 4, 14), 'My birthday', 4, "Home", "It's my birthday, so eat cake.", True)
event3 = Event(get_date(2022, 8, 20), 'Sarah\'s birthday', 14, "Everywhere", "Littlest one turning 4.", True)
event4 = Event(get_date(2022, 12, 6), 'Nick\'s birthday', 4, "Home", "Biggest one turning 40-something.", True)
event5 = Event(get_date(2022, 5, 21), 'Wedding', 100, "England-shire", "Wedding garden party", False)
events = [event1, event2, event3, event4, event5]