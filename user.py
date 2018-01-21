import utils

class User:
    'A regular user of the alarm clock'

    # alarm key is its minute-of-the-week. value is a dict of its attributes
    alarms = {}
    next_alarm = None
    current_alarm = None
    snooze = None
    alarm_sound = 'alarm.wav'

    def __init__(self):
        pass

    def refresh(self):
        if bool(self.alarms):
            current_week_minute = utils.datetime_to_week_minute()
            try:
                self.next_alarm = min(filter(lambda x: x > current_week_minute,self.alarms.keys()))
            except ValueError:
                self.next_alarm = min(self.alarms.keys())
        else:
            self.next_alarm = None

    def trigger(self):
        self.current_alarm = self.alarms[self.next_alarm]
        sound = self.alarms[self.current_alarm].get('sound',default=self.alarm_sound)
        utils.play_sound(sound)
        self.refresh()

    def silence(self):
        self.remove_one_time_alarm(self.current_alarm)
        self.current_alarm = None
        utils.stop_sound()

    def snooze_alarm(self):
        snooze = self.alarms[self.current_alarm].get('snooze',default=self.snooze)
        if snooze:
            snoozed_week_minute = utils.datetime_to_week_minute() + snooze
            if snoozed_week_minute > utils.MAX_WEEK_MINUTE:
                snoozed_week_minute -= utils.MAX_WEEK_MINUTE
            attributes = self.alarms[self.current_alarm]
            self.add_alarm(self.current_alarm,**attributes)
            self.silence()
            self.refresh()

    def add_alarm(self, week_minute, **kwargs):
        self.alarms[week_minute] = kwargs
        self.refresh()

    def remove_one_time_alarm(self, week_minute):
        if not self.alarms[week_minute].get('repeat',default=True):
            self.remove_alarm(week_minute)

    def remove_alarm(self, week_minute):
        try:
            del self.alarms[week_minute]
            self.refresh()
        except KeyError:
            pass

    def set_alarm_sound(self,sound_file):
        self.alarm_sound = sound_file

    def set_snooze(self,snooze_minutes):
        self.snooze = snooze_minutes
