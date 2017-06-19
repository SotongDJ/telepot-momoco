import mmcDefauV, mmctool, pprint

""" self.sender.sendMessage(mmcmsg.listMain(self._temra)) """
def listMain(lingua,dicto):
    final = open('descrimmc/'+lingua+'/sachiListMain.descri').read()
    final = final.replace('@dtempo@',mmctool.ul(dicto.get('dtempo','')))
    final = final.replace('@utempo@',mmctool.ul(dicto.get('utempo','')))
    final = final.replace('@keywo@',mmctool.ul(dicto.get('keywo','')))
    final = final.replace('@cokas@',mmctool.ul(dicto.get('cokas',''),modda='klass',lingua=lingua))
    return final

def listKeywo(lingua,keywo):
    final = open('descrimmc/'+lingua+'/sachiListKeywo.descri').read()
    final = final.replace('@keywo@',keywo)
    return final
