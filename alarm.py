import time
from datetime import datetime


class Alarm:
    on = True
    user = None
    days = set()
    hour = None
    minute = None
    alarm_id = None

    def __init__(self, user):
        self.alarm_id = int(round(time.time() * 1000))
        self.user = user
        self.hour = 7
        self.minute = 0
        self.days = {(datetime.now().weekday()+1) % 7}

    def set_time(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def add_day(self, day):
        self.days.add(day)

    def remove_day(self, day):
        try:
            self.days.remove(day)
        except KeyError:
            pass

    def toggle(self):
        self.on = not self.on

    def should_ring(self, day=None, hour=None, minute=None):
        if self.on:
            now = datetime.now()
            if day is None:
                day = now.weekday()
            if hour is None:
                hour = now.hour
            if minute is None:
                minute = now.minute
            return day in self.days and hour == self.hour and minute == self.minute
        else:
            return False
