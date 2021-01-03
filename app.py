import clamAV
import time
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.recycleview import RecycleView
from kivy.app import App
from functools import partial

class SoldanIT(FloatLayout):

    def __init__(self, **kwargs):
        super(SoldanIT, self).__init__(**kwargs)
        self.size=(600, 600)
        self.row_force_default = True
        self.row_default_height = 80
        b_clamav = Button(text="Scan")
        b_clamav.size_hint = (.25, .18)
        b_clamav.pos = (20, 20)
        b_clamav.bind(on_press=partial(self.run_scan, b_clamav))
        self.add_widget(b_clamav)
        b_report = Button(text="Show report")
        b_report.size_hint = (.25, .18)
        b_report.pos = (580, 250)
        b_report.bind(on_press=partial(self.show_report, b_report))
        self.add_widget(b_report)

    def run_scan(self, instance, *args):
        start_popup = Popup(title='Scanner',
                      content=Label(text='Scan has started. It could take a few minutes.'),
                      size_hint=(None, None), size=(400, 200))
        start_popup.open()
        clamAV.run_scan()
        finish_popup = Popup(title='Scanner',
                            content=Label(text='Scan has finished.'),
                            size_hint=(None, None), size=(400, 200))
        finish_popup.open()

    def show_report(self, instance, *args):
        report = clamAV.create_report()
        fields_list = RecycleView()
        fields_list.data = [{field[0]: field[1]} for field in report.items()]
        report_popup = Popup(title='Report',
                            size_hint=(None, None), size=(400, 400))
        report_popup.obj_
        report_popup.open()


class MyApp(App):

    def build(self):
        return SoldanIT()


if __name__ == '__main__':
    MyApp().run()