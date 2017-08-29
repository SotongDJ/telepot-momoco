from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, StringProperty
from kivy.graphics.instructions import InstructionGroup
from kivy.graphics import Rectangle,Color,Line

from kivy.lang import Builder
Builder.load_file('cakvSummarizing.kv')

import pprint
import modSearch, modDatabase
import tool

class SummaryCard(GridLayout):
    choseBox = ObjectProperty()
    resutBox = ObjectProperty()

    def tik(self,tar):
        tar.canvas.clear()

        lx = self.size[0]
        ly = self.size[1]

        #blue = InstructionGroup()
        #blue.add(Color(0, 0, 1, 1))
        #blue.add(Rectangle(pos=self.pos, size=(lx,ly*0.5)))

        black = InstructionGroup()
        black.add(Color(0, 0, 0, 1))
        black.add(Line(circle=(lx*0.5, ly*0.5, 100), width=15, joint='round', close=True))

        # Here, self should be a Widget or subclass
        #[tar.canvas.add(group) for group in [blue, black]]
        tar.canvas.add(black)

    def __init__(self, **kwargs):
        super(SummaryCard, self).__init__(**kwargs)

class MomocoApp(App):

    def build(self):
        #return SummaryCard(usrdir=usrdir)
        return SummaryCard()

if __name__ == '__main__':
    usrdir = MomocoApp().user_data_dir
    MomocoApp().run()
