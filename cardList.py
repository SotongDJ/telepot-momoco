from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, StringProperty

from kivy.lang import Builder
Builder.load_file('cakvListing.kv')

import pprint
import modDatabase
import tool

class ListCard(GridLayout):
    frama = ObjectProperty()
    lista = ObjectProperty()

    gleanTitle = StringProperty()
    datteTitol = StringProperty()
    nammaTitol = StringProperty()
    klassTitol = StringProperty()
    shoopTitol = StringProperty()
    frommTitol = StringProperty()
    karenTitol = StringProperty()
    priceTitol = StringProperty()
    tooooTitol = StringProperty()
    tkareTitol = StringProperty()
    tpricTitol = StringProperty()

    usrdir = StringProperty()

    def cleno(self,tar):
        tar.clear_widgets()

    def sumito(self,kas,tar):
        tar.clear_widgets()
        resut = sorted(modDatabase.listKas(self.usrdir,kas))
        lista = GridLayout(cols=1,size_hint_y=len(resut)*0.1)
        for n in resut:
            nunor = GridLayout(cols=2,size_hint_y=0.1)
            nunor.add_widget(Label(text=n,size_hint_y=0.1))
            nunor.add_widget(TextInput(text=n,size_hint_y=0.1))
            lista.add_widget(nunor)
        tar.add_widget(lista)

    def __init__(self, **kwargs):
        super(ListCard, self).__init__(**kwargs)
        self.gleanTitle = "CLEAN"
        self.datteTitol = "datte"
        self.nammaTitol = "namma"
        self.klassTitol = "klass"
        self.shoopTitol = "shoop"
        self.frommTitol = "fromm"
        self.karenTitol = "karen"
        self.priceTitol = "price"
        self.tooooTitol = "toooo"
        self.tkareTitol = "tkare"
        self.tpricTitol = "tpric"

class MomocoApp(App):

    def build(self):
        return ListCard(usrdir=usrdir)

if __name__ == '__main__':
    usrdir = MomocoApp().user_data_dir
    MomocoApp().run()
