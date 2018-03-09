import pprint, modArgona

class MsgCreo:
    def __init__(self,lingua='SiMP'):
        self.lingua = lingua

    def temran(self,temra={}):
        resut = open('descri/creoTemra.'+self.lingua).read()
        for kan in temra.keys():
            if temra.get(kan,'') == '':
                sitit = "____"
            else:
                sitit = temra.get(kan)
            resut = resut.replace('@'+kan+'@',sitit)
        return resut

    def recoman(self,esurut={},numano=""):
        resut = open('descri/creoRecom.'+self.lingua).read()
        resut = resut.replace('@numano@',numano)
        # pprint.pprint(temra)

        lista = ''
        if esurut.get('datte','') != '':
            lista = lista +'Date: ('+esurut.get('datte')+')\n　/datteR' + numano+'\n'
        if esurut.get('namma','') != '':
            lista = lista +'Name/Remind: ('+esurut.get('namma')+')\n　/nammaR' + numano+'\n'
        if esurut.get('shoop','') != '':
            lista = lista +'Shop/Agent: ('+esurut.get('shoop')+')\n　/shoopR' + numano+'\n'
        if esurut.get('klass','') != '':
            lista = lista +'Class: ('+esurut.get('klass')+')\n　/klassR' + numano+'\n'

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
                lista = lista + '[' + esurut.get('fromm','') + ']　/frommR' + numano + '\n'
            lista = lista + esurut.get('karen','___') + '　'
            lista = lista + esurut.get('price','') + ')\n'
            if esurut.get('karen','') != '':
                lista = lista + '　/karenR' + numano +'\n'
            if esurut.get('price','') != '':
                lista = lista + '　/priceR' + numano +'\n'

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
                lista = lista + '[' + esurut.get('toooo') + ']　/tooooR' + numano + '\n'
            lista = lista + '　' + esurut.get('tkare','___') + '　'
            lista = lista + esurut.get('tpric','') + ')\n'
            if esurut.get('tkare','') != '':
                lista = lista + '　/tkareR' + numano +'\n'
            if esurut.get('tpric','') != '':
                lista = lista + '　/tpricR' + numano +'\n'

        if esurut.get('desci','') != '':
            lista = lista +'\nDescription:\n　'+esurut.get('desci')+'\n'

        if lista == '':
            lista = '　No recomandation'
            resut = resut.replace('@recomnumano@',"")
        else:
            resut = resut.replace('@recomnumano@',"Replace All: \n"+"　/recom" + numano + "\n")

        resut = resut.replace('@lista@',lista)
        resut = resut.replace('@keywo@',esurut.get('keywo',''))

        return resut

    def savon(self,temra={}):
        resut = open('descri/creoSaved.'+self.lingua).read()
        for n in temra.keys():
            resut = resut.replace('@R' + n+'@',temra.get(n,"____"))
        return resut
