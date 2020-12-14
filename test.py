from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button


class FirstKivy(App):

    def build(self):
        return Button(text = "This is a button!", pos = (300, 350), size_hint = (.25, .18))

FirstKivy().run()