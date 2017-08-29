from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.graphics.Line import circle
from kivy.properties import ObjectProperty, StringProperty

from kivy.lang import Builder
Builder.load_file('cakvSummarizing.kv')

import pprint
import modSearch, modDatabase
import tool

class SummaryCard(GridLayout):

    def __init__(self, **kwargs):
        super(SearchCard, self).__init__(**kwargs)

class MomocoApp(App):

    def build(self):
        return SummaryCard(usrdir=usrdir)

if __name__ == '__main__':
    usrdir = MomocoApp().user_data_dir
    MomocoApp().run()
