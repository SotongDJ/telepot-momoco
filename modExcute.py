import tool, modDatabase, modSearch, modVariables
from msgMain import msgMain
from msgShort import msgShort

"""
This is the main part of Momocobot to handle income msg
and reply required msg back to user.

The codes of this file mainly lineage from comme() in momocobot.py.
"""
class Excut:
    """ process  msg
    grab command from hande()
    assign task to other mod
    and reply result back to hande()
    """

    def codGen(self): #condition of general function
        resut = False
        keyse = ["/start","/help","/exit"]
        for keywo in keyse:
            if keywo in self.text:
                resut = True
        return resut

    def moGen(self):
        if "/start" in self.text:
            mesut = msgMain(lingua=self.lingua,tasta='start')
            if self.primo == ['']:
                mesut = mesut + msgShort(lingua=self.lingua,tasta='cof')
                self.mesut = [mesut]
                self.cos=1
        elif "/help" in self.text:
            mesut = msgMain(lingua=self.lingua,tasta='help')
            if self.primo == ['']:
                mesut = mesut + msgShort(lingua=self.lingua,tasta='cof')
                self.mesut = [mesut]
                self.cos=1
        elif "/exit" in self.text:
            self.mesut = [msgShort(lingua=self.lingua,tasta='bye')]
            self.cos=1

    def moRaw():
        print('')

    def __init__(self,msg,arg):
        super(Excut, self).__init__(*args, **kwargs)
        self.text=msg['text']
        self.arg=arg

        self.mesut=[]
        self.cos=0
        self.primo = arg.get('primo',[''])
        self.submo = arg.get('submo','')
        self.temra = arg.get('temra',{})
        self.keywo = arg.get('keywo','')
        self.kasso = arg.get('kasso','')
        self.lingua = arg.get('setti',{}).get('lingua','enMY')

        if self.codGen():
            self.moGen()

        self.arg.update({
            'primo':self.primo,
            'submo':self.submo,
            'temra':self.temra,
            'keywo':self.keywo,
            'kasso':self.kasso,
        })
