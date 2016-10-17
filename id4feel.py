def idenFeel(msg):
    dicto={'good':1,'bad':-1,'sleep':-1,'lonely':-1,'dead':-3,'dying':-3,'loser':-1,'tired':-1,'hate':-1,'happy':1,'excited':1}
    dikta={'not':-1,'very':1.5,"not that":0.75,'super':2,'really':1.5,'better':1.25}
    keywos=[]
    level=0
    limit=0.5
    for keyword in dicto.keys():
        print("keyword: "+keyword)
        if keyword in msg:
            level=level+dicto[keyword]
            keywos.append(keyword)
            print(keyword+"+"+str(dicto[keyword]))
    for keyword in dikta.keys():
        print("keyword: "+keyword)
        if keyword in msg:
            level=level*dikta[keyword]
            keywos.append(keyword)
            print(keyword+"*"+str(dikta[keyword]))
    #print("level="+str(level)+", limit="+str(limit))
    return {"level":level,"limit":limit,"keyword":keywos}
