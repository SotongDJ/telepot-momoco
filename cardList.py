from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, StringProperty

from kivy.lang import Builder
Builder.load_file('cakvListing.kv')

import pprint
import modSearch, modDatabase
import tool

class Titol(Label):
    pass

class Tesol(Label):
    pass

class ListCard(GridLayout):

    dtempo = ObjectProperty()
    utempo = ObjectProperty()
    cokas = ObjectProperty()
    keywo = ObjectProperty()

    tempor = ObjectProperty()
    trasa = ObjectProperty()

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

    

    def __init__(self, **kwargs):
        super(ListCard, self).__init__(**kwargs)
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

class MomocoApp(App):

    def build(self):
        return ListCard(usrdir=usrdir)

if __name__ == '__main__':
    usrdir = MomocoApp().user_data_dir
    MomocoApp().run()
