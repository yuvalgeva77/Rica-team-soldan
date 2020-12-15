from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout


class FirstKivy(App):

    def do_quit_button(self, obj):
        quit()

    def build(self):
        layout = GridLayout(cols = 2, row_force_default = True, row_default_height = 100)

        report_button = Button(text = "Show report", pos = (300, 350), size_hint = (.10, .10))
        email_button = Button(text = "Check email", pos = (100, 350), size_hint = (.10, .10))
        kismet_button = Button(text = "Start Kismet", pos = (100, 350), size_hint = (.10, .10))
        nessus_button = Button(text = "Start Nessus", pos = (100, 350), size_hint = (.10, .10))
        av_button = Button(text = "Start Antivirus", pos = (100, 350), size_hint = (.10, .10))
        quit_button = Button(text = "Quit", pos = (100, 350), size_hint = (.10, .10))
        quit_button.bind(on_press = self.do_quit_button)

        

        for but in [report_button, email_button, kismet_button, nessus_button, av_button, quit_button]:
            layout.add_widget(but)


        return layout

FirstKivy().run()