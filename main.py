from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, StringProperty

from kivy.lang import Builder
Builder.load_file('cakvMain.kv')

import pprint
import modSearch, modDatabase, modVariables, modControl
import tool

class MainCard(GridLayout):
    tastala = ObjectProperty()
    resutla = ObjectProperty()
    butonla = ObjectProperty()

    def sumited(self,butonla,resutla,testa):
        self.prese = modControl.filto(prese=self.prese,testa=testa,butonla=butonla,resutla=resutla)

    def __init__(self, **kwargs):
        super(MainCard, self).__init__(**kwargs)
        self.prese = {}
        self.prese.update({ 'setti' : modDatabase.openSetting(usrdir) })
        self.prese.update({ 'usrdir' : usrdir })
        self.prese.update({ 'temra' : modVariables.keywo('temra') })
        self.prese.update({ 'stati' : modVariables.keywo('statics') })
        self.prese.update({ 'listi' : modVariables.keywo('listi') })
        self.prese.update({ 'karatio' : modDatabase.openKaratio(usrdir) })

class MomocoApp(App):

    def build(self):
        return MainCard()

if __name__ == '__main__':
    usrdir = MomocoApp().user_data_dir
    MomocoApp().run()
