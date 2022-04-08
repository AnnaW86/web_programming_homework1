class Event():
    def __init__(self, date, title, number_of_guests, location, description, recurring):
        self.date = date
        self.title = title
        self.number_of_guests = number_of_guests
        self.location = location
        self.description = description
        self.recurring = recurring