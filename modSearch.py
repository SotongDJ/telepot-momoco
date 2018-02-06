from core import modDatabase
from core import tool

import modKeywo,pprint

def exper(usrdir,mesag):
    """Grab word from msg"""
    print('modRecom.exper: '+tool.mask(usrdir))
    keydb = modDatabase.opendb(usrdir).get('key',{})
    rawdb = modDatabase.opendb(usrdir).get('raw',{})
    kewulista = modKeywo.listKeywo(usrdir)
    # kewulista = {keywo: {class : [ uuid ]}}

    mesalista = mesag.split(' ')
    mesdik = {} # {keywo: {class : [ uuid ]}}
    udilis = [] # [uuid]

    pprint.pprint(mesalista)
    for mesol in mesalista:
        if '@' not in mesol:
            for keywo in kewulista.
    pprint.pprint(mesdik)
    # pprint.pprint(udilis)
