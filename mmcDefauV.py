def keywo(text,lingua='enMY'):
    genar = {
        'sf' : {
            "dt":"datte",
            "nm":"namma", "kl":"klass", "sh":"shoop",
            "fr":"fromm", "pr":"price", "kr":"karen",
            "to":"toooo", "tp":"tpric", "tk":"tkare",

            "in":"dinco", "ex":"dexpe",
            "gi":"genis", "oe":"ovede",
            "tf":"tanfe", "ic":"incom",
        },
        'fs' : {
            "datte":"dt",
            "namma":"nm", "klass":"kl", "shoop":"sh",
            "fromm":"fr", "price":"pr", "karen":"kr",
            "toooo":"to", "tpric":"tp", "tkare":"tk",

            "dinco":"in", "dexpe":"ex",
            "genis":"gi", "ovede":"oe",
            "tanfe":"tf", "incom":"ic",
        },
        'klass' : {
            'Acc':['fr','to','in','ex','gi','oe'],
            'Kas':['kl','tf','ic'],
            'Ken':['kr','tk'],
            'Pis':['pr','tp'],
        },
        'temra' : {
            "datte":"",
            "namma":"", "klass":"", "shoop":"",
            "fromm":"", "price":"", "karen":"",
            "toooo":"", "tpric":"", "tkare":"",
            "desci":"",
        },
        'statics':{
            'mode':'',
            'leve':10,
            'dtempo':'','utempo':'',
            'cokas':'','cokey':'',
            'targe':'',
        },
        'list' : {
            'datte': '',
            'uuid' : ''
        },
        'setting' : {
            'dinco':'Bank', 'dexpe':'Cash',
            'genis':'Income', 'ovede':'Expense',
            'tanfe':'Transfer', 'incom':'Income',
            'karen':'MYR',
            'defSettWarn':0,
            'screen':13,
            'limit':'',
            'krset':{},
            'lingua':'enMY',
            'natio':'',
        },
        'lingua':['enMY','hanT'],
        'leve':{
            10:'Day',
            7:'Month',
            4:'Year',
            'Day':10,
            'Month':7,
            'Year':4,
        },
        'recset':['namma', 'klass', 'shoop', 'price'],
    }
    woood = {
        'enMY' : {
            'ssalk' : {
                "datte":"Date",
                "namma":"Name, e.g item", "shoop":"Agent, e.g. Seller",
                'fromm':'Account','toooo':'Account[To]','dinco':'Account','dexpe':'Account','genis':'Account','ovede':'Account',
                'klass':'Category','tanfe':'Category','incom':'Category',
                'karen':'Currency','tkare':'Currency[To]',
                'price':'Price','tpric':'Price',
                'cokas':'Top Class', 'cokey':'Class',
                'targe':'Target Class', 'desci':'Description',
                'lingua':'Language',
            },
        },
        'hanT' : {
            'ssalk' : {
                "datte":"日期",
                "namma":"名稱，例：品名", "shoop":"中介，例：商家",
                'fromm':'賬號','toooo':'賬戶［目標］','dinco':'賬號','dexpe':'賬號','genis':'賬號','ovede':'賬號',
                'klass':'類別','tanfe':'類別','incom':'類別',
                'karen':'幣種','tkare':'幣種［目標］',
                'price':'價格','tpric':'價格［目標］',
                'cokas':'類型', 'cokey':'類別',
                'targe':'目標類型', 'desci':'註釋',
                'lingua':'語言',
            },
        },
    }
    if text in genar.keys():
        resut = genar.get(text,{})
    elif text in woood[lingua].keys():
        resut = woood[lingua].get(text,{})
    return resut
