class Event:
    def __init__(self, name, date, participant_count):
        self.name = name
        self.date = date
        self.participant_count = participant_count

    def add_participant(self):
        self.participant_count += 1

    def get_participant_count(self):
        print(self.participant_count)

new_event = Event("Coachella", 10/23/2002, 100000)

print(new_event.name)

new_event.add_participant()

print(new_event.get_participant_count())

