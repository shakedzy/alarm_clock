import time
import utils
from datetime import datetime


class Clock:
    alarms = set()
    users = set()

    day = 0
    hour = 0
    minute = 0
    second = 0

    def update(self):
        prev_minute = self.minute
        now = datetime.now()
        self.day = now.weekday()
        self.hour = now.hour
        self.minute = now.minute
        self.second = now.second
        if prev_minute != now.minute:
            for alarm in self.alarms:
                if alarm.should_ring():
                    self.activate_alarm(alarm.user)

    def __init__(self):
        now = datetime.now()
        self.day = now.weekday()
        self.hour = now.hour
        self.minute = now.minute
        self.second = now.second

    def activate_alarm(self, user):
        # TODO
        pass

    def snooze(self):
        # TODO
        pass

    def add_user(self):
        # TODO
        pass

    def remove_user(self, user):
        self.users.remove(user)
        for alarm in self.alarms:
            if alarm.user == user:
                self.alarms.remove(alarm)
#
