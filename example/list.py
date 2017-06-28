import os
os.environ['KIVY_DPI'] = '320'
os.environ['KIVY_METRICS_DENSITY'] = '2'

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.properties import ObjectProperty, StringProperty

class Buto(Button):
    inTa = StringProperty()

    def pus(self):
        print(self.inTa)

class Selection(AnchorLayout):
    usrdir = StringProperty()
    def login(self,tar):
        tar.clear_widgets()
        tar.add_widget(LoginScreen(usrdir=usrdir))


class LoginScreen(GridLayout):

    usnan = ObjectProperty()
    paswd = ObjectProperty()
    resut = ObjectProperty()
    hinti = ObjectProperty()

    usnanTitle = StringProperty()
    paswdTitle = StringProperty()

    hintiText = StringProperty()
    sumitText = StringProperty()
    usrdir = StringProperty()

    def sumited(self,tar,taa,tao):
        wd = "Name:"+taa+", Password:"+tao
        laba = Buto(text=wd,inTa=tao)
        tar.add_widget(laba)

    def close(self):
        App.get_running_app().stop()

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.usnanTitle = 'Name'
        self.paswdTitle = 'Password'
        self.sumitText = 'Sumit'

class Choose(GridLayout):
    usrdir = StringProperty()

    def returan(self):
        LasApp.hiwi.clear_widgets()
        LasApp.hiwi.add_widget(Selection(usrdir=usrdir))

    def __init__(self, **kwargs):
        super(Choose, self).__init__(**kwargs)
        LasApp.hiwi.add_widget(Selection(usrdir=usrdir))

class LasApp(App):
    hiwi = ObjectProperty()

    def build(self):
        return Choose(usrdir=usrdir)


if __name__ == '__main__':
    usrdir = LasApp().user_data_dir
    LasApp().run()
