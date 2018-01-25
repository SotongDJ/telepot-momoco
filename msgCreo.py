class MsgCreo:
    def __init__(self,lingua='SiMP'):
        self.lingua = lingua

    def temran(self,temra={}):
        resut = open('descri/creoTemra.'+self.lingua).read()
        for n in temra.keys():
            resut = resut.replace('@'+n+'@',temra.get(n,"____"))
        return resut

    def recoman(self,temra={},esurut={},numano=""):
        resut = open('descri/creoRecom.'+self.lingua).read()
        for n in temra.keys():
            if esurut.get(n,'') != '':
                if temra.get(n,'') != '':
                    testa = temra.get(n)+" <-- /"+ n + numano + " "+ esurut.get(n,'')
                else:
                    testa = "/" + n + numano + " "+ esurut.get(n,'')
            else:
                if esurut.get('solok','') != '' and esurut.get('solok','') != 'esurut':
                    testa = "/" + n + numano + " "+ esurut.get('solok')
                else:
                    testa = "____"
            resut = resut.replace('@'+n+'@',testa)

        if esurut.get('solok','') == 'esurut':
            resut = resut.replace('@recomnumano@',"/recom" + numano)
        else:
            resut = resut.replace('@recomnumano@',"not available")
        return resut
