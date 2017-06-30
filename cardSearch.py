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

    def stored(self,fro,too,tar,tan):
        too = fro
        tar.text = too
        self.dicto.update({ tan : too })

    def sumited(self,tar):
        modDatabase.refesdb(usrdir=self.usrdir)
        tempa = modSearch.sachi(usrdir=self.usrdir,dicto=self.dicto)
        self.resut = modSearch.listSachi(usrdir,tempa,lingua='hanT')
        lenes = self.resut.get('lenes',1)
        lenam = self.resut.get('lenam',1)
        tar.clear_widgets()
        for uuid in self.resut.get('resut',{}).keys():
            hei = len(self.resut.get('resut',{}).get(uuid,['']))
            namgro = GridLayout(cols=2,size_hint_y=hei)

            itegro = GridLayout(cols=1,size_hint_x=lenes)
            for n in self.resut.get('resut',{}).get(uuid,[]):
                itegro.add_widget(Button(text=n,height=20))

            namgro.add_widget(Button(text=uuid,size_hint_x=lenam))
            namgro.add_widget(itegro)

            tar.add_widget(namgro)

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
