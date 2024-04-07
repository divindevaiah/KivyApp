from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from plyer import notification


class DivinApp(BoxLayout):
    def __init__(self):
        super(DivinApp, self).__init__()
        self.i = 0

    def switch_state(self):
        self.i += 1
        self.show_notification()
        self.coord_id.text = f'{self.i}'

    def show_notification(self):
        notification.notify(title='test', message=f"Count: {self.i}")


class DemoApp(App):
    def build(self):
        return DivinApp()

if __name__ == '__main__':
    DemoApp().run()

