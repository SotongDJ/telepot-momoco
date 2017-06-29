from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, StringProperty

from kivy.lang import Builder
Builder.load_file('cakvSearching.kv')

import pprint
import modSearch
import tool

class Labo(Label):
    pass

class SearchCard(GridLayout):

    dtempo = ObjectProperty()
    utempo = ObjectProperty()
    cokas = ObjectProperty()
    keywo = ObjectProperty()

    tempor = ObjectProperty()

    dtempoTitle = StringProperty()
    utempoTitle = StringProperty()
    cokasTitle = StringProperty()
    keywoTitle = StringProperty()

    dtempoText = StringProperty()
    utempoText = StringProperty()
    cokasText = StringProperty()
    keywoText = StringProperty()

    storeText = StringProperty()
    sumitText = StringProperty()
    usrdir = StringProperty()

    def stored(self,fro,too,tar,tan):
        too = fro
        tar.text = too
        self.dicto.update({ tan : too })

    def sumited(self,tar):
        self.resut = modSearch.sachi(usrdir=self.usrdir,dicto=self.dicto)
        tar.add_widget(Labo(text=pprint.pformat(self.resut,compact=True)))

    def __init__(self, **kwargs):
        super(SearchCard, self).__init__(**kwargs)
        self.dtempoTitle = "Start: "
        self.utempoTitle = "End: "
        self.cokasTitle = "Class: "
        self.keywoTitle = "Keywo: "

        self.storeText = 'Store -->'
        self.sumitText = 'Sumit'

        self.dicto={
            'dtempo' : self.dtempoText,
            'utempo' : self.utempoText,
            'cokas' : self.cokasText,
            'keywo' : self.keywoText,
        }

class SearchingApp(App):

    def build(self):
        dtempoText = tool.date(modde=6)
        utempoText = tool.date(modde=6)
        return SearchCard(dtempoText=dtempoText,utempoText=utempoText,usrdir=usrdir)

if __name__ == '__main__':
    usrdir = SearchingApp().user_data_dir
    SearchingApp().run()
