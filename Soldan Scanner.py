import subprocess
from app import SoldanIT
import webbrowser as wb
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window



class SoldanScanner(App):

    def do_quit_button(self, obj):
        quit()
    def report(self, instance):
        with open('report.txt') as file:
            content= file.read()
        popup = Popup(title='Report',
            content = Label(text=content),
            size_hint = (None, None), size = (700, 700),
            auto_dismiss = True)
        popup.open()

    def do_nessus_install_button(self, instance):
        wb.open("https://de.tenable.com/products/nessus")
        ## TODO: Open the description file

    def do_nessus_button(self, instance):
        wb.open("https://localhost:8834/")
    
    def do_av_button(self, instance):
        SoldanIT.run_scan(self, instance)

    def build(self):
        layout = GridLayout(cols=2, row_force_default=True, row_default_height=100)

        report_button = Button(text="Show report", pos=(300, 350), size_hint=(.10, .10))
        report_button.bind(on_press=self.report)
        nessus_install_button = Button(text="Install Nessus", pos=(100, 350), size_hint=(.10, .10))
        nessus_install_button.bind(on_press = self.do_nessus_install_button)
        nessus_button = Button(text="Start Nessus", pos=(100, 350), size_hint=(.10, .10))
        nessus_button.bind(on_press = self.do_nessus_button)
        av_button = Button(text="Start Antivirus", pos=(100, 350), size_hint=(.10, .10))
        av_button.bind(on_press = self.do_av_button)
        quit_button = Button(text="Quit", pos=(100, 350), size_hint=(.10, .10))
        quit_button.bind(on_press=self.do_quit_button)

        for but in [report_button, nessus_button, nessus_install_button, av_button, quit_button]:
            layout.add_widget(but)

        return layout


SoldanScanner().run()