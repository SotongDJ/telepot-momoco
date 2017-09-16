""" self.sender.sendMessage(mmcmsg.listMain(self._temra)) """
def main(lingua,datte,text):
    final = open('descrimmc/'+lingua+'/listMain.descri').read()
    final = final.replace('@datte@',datte)
    final = final.replace('@text@',text)
    return final

def change(lingua,keywo,text):
    final = open('descrimmc/'+lingua+'/listChange.descri').read()
    final = final.replace('@keywo@',keywo)
    final = final.replace('@text@',text)
    return final

""" self.sender.sendMessage(mmcmsg.listSect(uuid,usrid,libra)) """
def single(lingua,uuid,usrid,libra):
    final = open('descrimmc/'+lingua+'/listSingle.descri').read()
    final = final.replace('@uuid@',uuid)
    final = final.replace('@datte@',libra[uuid].get('datte',''))
    final = final.replace('@namma@',libra[uuid].get('namma',''))
    final = final.replace('@klass@',libra[uuid].get('klass',''))
    final = final.replace('@shoop@',libra[uuid].get('shoop',''))
    final = final.replace('@karen@',libra[uuid].get('karen',''))
    final = final.replace('@price@',libra[uuid].get('price',''))
    final = final.replace('@fromm@',libra[uuid].get('fromm',''))
    final = final.replace('@tkare@',libra[uuid].get('tkare',''))
    final = final.replace('@tpric@',libra[uuid].get('tpric',''))
    final = final.replace('@toooo@',libra[uuid].get('toooo',''))
    final = final.replace('@desci@',libra[uuid].get('desci',''))
    return final

""" self.sender.sendMessage(mmcmsg.listDisca()) """
def disca(lingua):
    final = open('descrimmc/'+lingua+'/listDisca.descri').read()
    return final
