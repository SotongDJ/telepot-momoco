from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, StringProperty

from kivy.lang import Builder
Builder.load_file('cakvEditing.kv')

import modDatabase
import tool

class DataPart(GridLayout):

    datte = ObjectProperty()
    namma = ObjectProperty()
    klass = ObjectProperty()
    shoop = ObjectProperty()
    fromm = ObjectProperty()
    price = ObjectProperty()
    karen = ObjectProperty()
    toooo = ObjectProperty()
    tpric = ObjectProperty()
    tkare = ObjectProperty()
    desci = ObjectProperty()

    datteTitle = StringProperty()
    nammaTitle = StringProperty()
    klassTitle = StringProperty()
    shoopTitle = StringProperty()
    frommTitle = StringProperty()
    priceTitle = StringProperty()
    karenTitle = StringProperty()
    tooooTitle = StringProperty()
    tpricTitle = StringProperty()
    tkareTitle = StringProperty()
    desciTitle = StringProperty()

    datteText = StringProperty()
    nammaText = StringProperty()
    klassText = StringProperty()
    shoopText = StringProperty()
    frommText = StringProperty()
    priceText = StringProperty()
    karenText = StringProperty()
    tooooText = StringProperty()
    tpricText = StringProperty()
    tkareText = StringProperty()
    desciText = StringProperty()

    storeText = StringProperty()
    sumitText = StringProperty()
    uuidText = StringProperty()
    usrdir = StringProperty()

    def stored(self,fro,too,tar,tan):
        too = fro
        tar.text = too
        self.temra.update({ tan : too })
        modDatabase.chRaw(usrdir=self.usrdir,temra=self.temra,uuid=self.uuidText)

    def sumited(self):
        modDatabase.chRaw(usrdir=self.usrdir,temra=self.temra,uuid=self.uuidText)

    def __init__(self, **kwargs):
        super(DataPart, self).__init__(**kwargs)
        rawdb = modDatabase.opendb(usrdir=self.usrdir).get('raw',{})
        self.datteText = rawdb.get(self.uuidText,{}).get('datte','')
        self.nammaText = rawdb.get(self.uuidText,{}).get('namma','')
        self.klassText = rawdb.get(self.uuidText,{}).get('klass','')
        self.shoopText = rawdb.get(self.uuidText,{}).get('shoop','')
        self.frommText = rawdb.get(self.uuidText,{}).get('fromm','')
        self.priceText = rawdb.get(self.uuidText,{}).get('price','')
        self.karenText = rawdb.get(self.uuidText,{}).get('karen','')
        self.tooooText = rawdb.get(self.uuidText,{}).get('toooo','')
        self.tpricText = rawdb.get(self.uuidText,{}).get('tpric','')
        self.tkareText = rawdb.get(self.uuidText,{}).get('tkare','')
        self.desciText = rawdb.get(self.uuidText,{}).get('desci','')

        self.temra={
            'datte' : self.datteText,
            'namma' : self.nammaText,
            'klass' : self.klassText,
            'shoop' : self.shoopText,
            'fromm' : self.frommText,
            'price' : self.priceText,
            'karen' : self.karenText,
            'toooo' : self.tooooText,
            'tpric' : self.tpricText,
            'tkare' : self.tkareText,
            'desci' : self.desciText,
        }

        self.datteTitle = "Date: "
        self.nammaTitle = "Name: "
        self.klassTitle = "Class: "
        self.shoopTitle = "Seller: "
        self.frommTitle = "From: "
        self.karenTitle = "Currency: "
        self.priceTitle = "Price: "
        self.tooooTitle = "To: "
        self.tkareTitle = "Currency: "
        self.tpricTitle = "Price: "
        self.desciTitle = "Notes: "

        self.storeText = "Store -->"
        self.sumitText = "Sumit"

        self.temra={
            'datte' : self.datteText,
            'namma' : self.nammaText,
            'klass' : self.klassText,
            'shoop' : self.shoopText,
            'fromm' : self.frommText,
            'price' : self.priceText,
            'karen' : self.karenText,
            'toooo' : self.tooooText,
            'tpric' : self.tpricText,
            'tkare' : self.tkareText,
            'desci' : self.desciText,
        }

class EditCard(GridLayout):

    indata = ObjectProperty()
    uuidTitle = StringProperty()
    datapar = ObjectProperty()

    calloutText = StringProperty()
    cleenText = StringProperty()
    usrdir = StringProperty()

    def callout(self,uuid,tar):
        tar.clear_widgets()
        tar.add_widget(DataPart(uuidText=uuid,usrdir=self.usrdir))

    def cleen(self,tar):
        tar.clear_widgets()

    def __init__(self, **kwargs):
        super(EditCard, self).__init__(**kwargs)
        self.uuidTitle = "UUID: "
        self.cleenText = "Clean"
        self.calloutText = "Call out Data"

class MomocoApp(App):

    def build(self):
        return EditCard(usrdir=usrdir)

if __name__ == '__main__':
    usrdir = MomocoApp().user_data_dir
    MomocoApp().run()
