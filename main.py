from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, StringProperty

from kivy.lang import Builder
Builder.load_file('cakvSearching.kv')

import pprint
import modSearch, modDatabase, modVariables
import tool

class MainCard(GridLayout):
    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        self.prese = {}
        self.prese.update({ 'setti' : modDatabase.openSetting(usrdir) })
        self.prese.update({ 'temra' : modVariables.keywo('temra') })
        self.prese.update({ 'stati' : modVariables.keywo('statics') })
        self.prese.update({ 'listi' : modVariables.keywo('listi') })
        self.prese.update({ 'karatio' : modDatabase.openKaratio(usrdir) })

class MainApp(App):

    def build(self):
        return MainCard()

if __name__ == '__main__':
    usrdir = MainApp().user_data_dir
    MainApp().run()
