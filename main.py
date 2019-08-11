# pip install kivy screeninfo pygame

import kivy
kivy.require('1.11.1')

from screeninfo import get_monitors

from kivy.app import App
from kivy.uix.label import Label
from kivy.config import Config

first_monitor = get_monitors()[0]

Config.set('graphics', 'width', first_monitor.width)
Config.set('graphics', 'height', first_monitor.height)
Config.write()

class Application(App):
    def build(self):
        return Label(text="wowowowowow", font_size="70px")

if __name__ == '__main__':
    Application().run();
