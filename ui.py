from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from clock import Clock as ClockMechanics
from utils import num_to_str, normalize_rgb


class BaseScreen(Screen):
    transition_duration = 0.5


class ClockLabel(Label, ClockMechanics):
    def get_time(self):
        return '{0}:{1}:{2}'.format(num_to_str(self.hour),
                                    num_to_str(self.minute),
                                    num_to_str(self.second))

    def tic_tac(self, *args):
        self.update()
        self.text = self.get_time()


class MainScreen(BaseScreen):
    pass


class NewUserScreen(BaseScreen):
    pass


class EditUserScreen(BaseScreen):
    pass


class EditAlarmScreen(BaseScreen):
    pass


class AlarmScreen(BaseScreen):
    rgb = [255, 255, 255]
    pass

