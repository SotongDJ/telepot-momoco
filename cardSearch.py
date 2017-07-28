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
        self.sumited(tah)

    def sumited(self,tar):
        modDatabase.refesdb(usrdir=self.usrdir)
        tempa = modSearch.sachi(usrdir=self.usrdir,dicto=self.dicto)
        self.resut = modSearch.listSachi(usrdir,tempa,lingua='hanT')
        tar.clear_widgets()

        nutit = 0
        nutes = 0
        nuuid = 0
        heuid = 0.05 #1
        hitit = 0.10 #5
        hites = 0.20 #5
        for namma in self.resut.get('resut',{}).keys():
            nutes = nutes + len(self.resut.get('resut',{}).get(namma,[]))
        sumhi = (nutit*hitit)+(nutes*(hites+heuid))

        tampo = GridLayout(cols=1,size_hint_y=sumhi)
        for namma in sorted(self.resut.get('resut',{}).keys()):
            conto = self.resut.get('resut',{}).get(namma,{})
            #itegro = GridLayout(cols=1)
            tampo.add_widget(Titol(text=namma,size_hint_y=hitit))
            for n in sorted(list(conto.keys())):
                tampo.add_widget(TextInput(text=n,size_hint_y=heuid))
                #itegro.add_widget(TextInput(text=n,size_hint_y=heuid))
                tampo.add_widget(Tesol(text=conto.get(n,''),size_hint_y=hites))
                #itegro.add_widget(Tesol(text=conto.get(n,''),size_hint_y=hites))
            #tampo.add_widget(itegro)

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
