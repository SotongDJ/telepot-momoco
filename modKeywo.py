from core import modDatabase
from core import tool

def listKeywo(usrdir):
    print('modKeywo.listKeywo: '+tool.mask(usrdir))
    keydb = modDatabase.opendb(usrdir).get('key',{})
    resut = {}
    for kas in keydb.keys():
        if kas not in ['datte','price','tpric','desci','karen','tkare']:
            for keywo in keydb.get(kas,{}).keys():
                numon = 0
                metdi = {}
                metse = []

                metdi = resut.get(keywo,{})
                metse = metdi.get(kas,[])
                metse.extend(keydb.get(kas,{}).get(keywo,[]))
                metdi.update({ kas : metse })
                resut.update({ keywo : metdi })
    return resut