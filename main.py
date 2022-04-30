from distutils.command.build import build
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window

class PaintWindow(Widget):
    pass

class PaintApp(App):

    def build(self):
        return PaintWindow()


PaintApp().run()s