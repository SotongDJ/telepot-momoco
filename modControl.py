from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, StringProperty

import modDatabase, modVariables

#def printo(prese,tar):

#def comman(prese):
def modde(prese,testa):
    prese.update({ 'primo' : testa })

def filto(prese,testa,resutla,butonla):
    usrdir = prese.get('usrdir','')
    lingua = prese.get('lingua','enMY')

    keywo = prese.get('keywo','')
    keyse = prese.get('keyse','')
    primo = prese.get('primo','')
    submo = prese.get('submo','')
    temra = prese.get('temra',modVariables.keywo('temra'))
    recom = prese.get('recom',{})
    chset = prese.get('chset',{})
    stati = prese.get('stati',modVariables.keywo('statics'))
    listi = prese.get('listi',modVariables.keywo('listi'))
    setti = prese.get('setti',modVariables.keywo('setting'))
    karatio = prese.get('karatio',{})

    rawdb = modDatabase.opendb(usrdir).get('raw',{})
    keydb = modDatabase.opendb(usrdir).get('key',{})

    prese.update({ 'resut' : { 'forma' : '', 'conte' : {} } })

    #if 'primo' == '':
    #    lista = GridLayout(cols=2,size_hint_y=6)
    #    lista.add_widget(Button(text='Searching',on_text_validate=modde(prese=prese,testa='sachi')))
    #    butonla.add_widget(lista)

    lista = GridLayout(cols=2,size_hint_y=6)
    lista.add_widget(Button(text='Searching',on_press=modde(prese=prese,testa='sachi')))
    butonla.add_widget(lista)

    resutla.clear_widgets()
    resutla.add_widget(Label(text=testa))


    return prese
