import ui
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock


class MainApp(App):
    def build(self):
        self.title = 'Alarm Clock'
        main_screen = ui.MainScreen()
        Clock.schedule_interval(main_screen.ids.clock_label.tic_tac, 0.9)
        return main_screen


if __name__ == "__main__":
    Builder.load_file('ui.kv')
    MainApp().run()
