import os
os.environ['KIVY_DPI'] = '320'
os.environ['KIVY_METRICS_DENSITY'] = '2'

from kivy.app import App
from son import LoginScreen

class MomocoApp(App):

    def build(self):
        return LoginScreen(usnanText='None',paswdText='None',usrdir=usrdir)


if __name__ == '__main__':
    usrdir = MomocoApp().user_data_dir
    MomocoApp().run()
