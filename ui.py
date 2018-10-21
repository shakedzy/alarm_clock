from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from clock import Clock as ClockMechanics
from utils import num_to_str


class ClockLabel(Label, ClockMechanics):
    def get_time(self):
        return '{0}:{1}:{2}'.format(num_to_str(self.hour),
                                    num_to_str(self.minute),
                                    num_to_str(self.second))

    def tic_tac(self, *args):
        self.update()
        self.text = self.get_time()


class MainScreen(Screen):
    pass


class NewUserScreen(Screen):
    pass


class EditUserScreen(Screen):
    pass


class EditAlarmScreen(Screen):
    pass


class AlarmScreen(Screen):
    pass

