import os
os.environ['KIVY_DPI'] = '320'
os.environ['KIVY_METRICS_DENSITY'] = '2'

from kivy.app import App
from son import LoginScreen

class MyApp(App):

    def build(self):
        return LoginScreen(uOtext='None',pOtext='None')


if __name__ == '__main__':
    MyApp().run()
