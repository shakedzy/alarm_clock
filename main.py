import ui
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from utils import normalize_rgb



class MainApp(App):
    def build(self):
        self.title = 'Alarm Clock'
        Window.clearcolor = normalize_rgb([90, 12, 102]) + [1]
        main_screen = ui.MainScreen()
        Clock.schedule_interval(main_screen.ids.clock_label.tic_tac, 0.9)
        sm = ScreenManager()
        sm.add_widget(ui.MainScreen(name='main_screen'))
        sm.add_widget(ui.NewUserScreen(name='new_user_screen'))
        return sm


if __name__ == "__main__":
    Builder.load_file('ui.kv')
    MainApp().run()
