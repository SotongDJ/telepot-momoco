from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, StringProperty

from kivy.lang import Builder
Builder.load_file('cakvSearching.kv')

import pprint
import modSearch, modDatabase
import tool

class Titol(Label):
    pass

class Tesol(Label):
    pass

class SearchCard(GridLayout):

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

    def stored(self,fro,too,tar,tan,tah):
        too = fro
        tar.text = too
        self.dicto.update({ tan : too })
        if self.dicto.get('keywo','') != '':
            self.sumited(tah)
        else:
            tah.clear_widgets()
            tah.add_widget(Label(text='Require keyword'))

    def sumited(self,tar):
        modDatabase.refesdb(usrdir=self.usrdir)
        tempa = modSearch.sachi(usrdir=self.usrdir,dicto=self.dicto)
        self.resut = modSearch.listSachi(usrdir,tempa,lingua='hanT')
        tar.clear_widgets()

        nummo = 0
        heiyo = 0.1
        for namma in self.resut.get('resut',{}).keys():
            nummo = nummo + 1 # for uuid TextInput
            nummo = nummo + len(namma.splitlines())
            conto = self.resut.get('resut',{}).get(namma,{})
            for n in conto.keys():
                nummo = nummo + len(conto.get(n,'').splitlines())

        tampo = GridLayout(cols=1,size_hint_y=nummo*heiyo)
        for namma in sorted(self.resut.get('resut',{}).keys()):
            conto = self.resut.get('resut',{}).get(namma,{})
            tanum = len(namma.splitlines())
            tampo.add_widget(Titol(text=namma,size_hint_y=tanum*heiyo))
            for n in sorted(list(conto.keys())):
                tampo.add_widget(TextInput(text=n,size_hint_y=heiyo))
                tanum = len(conto.get(n,'').splitlines())
                tampo.add_widget(Tesol(text=conto.get(n,''),size_hint_y=tanum*heiyo))

        tar.add_widget(tampo)

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

class MomocoApp(App):

    def build(self):
        dtempoText = tool.date(modde=6)
        utempoText = tool.date(modde=6)
        return SearchCard(dtempoText=dtempoText,utempoText=utempoText,usrdir=usrdir)

if __name__ == '__main__':
    usrdir = MomocoApp().user_data_dir
    MomocoApp().run()
