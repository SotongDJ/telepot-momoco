import pprint, modArgona

class MsgCreo:
    def __init__(self,lingua='SiMP'):
        self.lingua = lingua

    def temran(self,temra={}):
        resut = open('descri/creoTemra.'+self.lingua).read()
        for n in temra.keys():
            if temra.get(n,'') == '':
                sitit = "____"
            else:
                sitit = temra.get(n)
            resut = resut.replace('@'+n+'@',sitit)
        return resut

    def recoman(self,esurut={},numano=""):
        resut = open('descri/creoRecom.'+self.lingua).read()
        resut = resut.replace('@numano@',numano)
        # pprint.pprint(temra)

        lista = ''
        if esurut.get('datte','') != '':
            lista = lista +'Date: ('+esurut.get('datte')+')\n　/datte'+numano+'\n'
        if esurut.get('namma','') != '':
            lista = lista +'Name/Remind: ('+esurut.get('namma')+')\n　/namma'+numano+'\n'
        if esurut.get('shoop','') != '':
            lista = lista +'Shop/Agent: ('+esurut.get('shoop')+')\n　/shoop'+numano+'\n'
        if esurut.get('klass','') != '':
            lista = lista +'Class: ('+esurut.get('klass')+')\n　/klass'+numano+'\n'

        focod = False
        if esurut.get('fromm','') != '':
            focod = True
        if esurut.get('karen','') != '':
            focod = True
        if esurut.get('price','') != '':
            focod = True
        if focod:
            lista = lista + '\nFrom: \n　('

            if esurut.get('fromm','') != '':
                lista = lista + '[' + esurut.get('fromm','') + ']　/fromm' + numano + '\n'
            lista = lista + esurut.get('karen','___') + '　'
            lista = lista + esurut.get('price','') + ')\n'
            if esurut.get('karen','') != '':
                lista = lista + '　/karen' + numano +'\n'
            if esurut.get('price','') != '':
                lista = lista + '　/price' + numano +'\n'

        tocod = False
        if esurut.get('toooo','') != '':
            tocod = True
        if esurut.get('tkare','') != '':
            tocod = True
        if esurut.get('tpric','') != '':
            tocod = True
        if tocod:
            lista = lista + '\nTo: \n　('

            if esurut.get('toooo','') != '':
                lista = lista + '[' + esurut.get('toooo') + ']　/toooo' + numano + '\n'
            lista = lista + '　' + esurut.get('tkare','___') + '　'
            lista = lista + esurut.get('tpric','') + ')\n'
            if esurut.get('tkare','') != '':
                lista = lista + '　/tkare' + numano +'\n'
            if esurut.get('tpric','') != '':
                lista = lista + '　/tpric' + numano +'\n'

        if esurut.get('desci','') != '':
            lista = lista +'\nDescription:\n　'+esurut.get('desci')+'\n'

        resut = resut.replace('@lista@',lista)

        if esurut.get('solok','') == '@esurut@':
            resut = resut.replace('@recomnumano@',"Replace All: \n"+"　/recom" + numano + "\n")
        else:
            resut = resut.replace('@recomnumano@',"")
        return resut

    def savon(self,temra={}):
        resut = open('descri/creoSaved.'+self.lingua).read()
        for n in temra.keys():
            resut = resut.replace('@'+n+'@',temra.get(n,"____"))
        return resut
