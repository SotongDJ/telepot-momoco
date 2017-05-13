def keywo(text):
    dicto= {
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
        'ssalk' : {
            "datte":"Date",
            "namma":"Name, e.g item", "shoop":"Place, e.g. Seller",
            'fromm':'Account','toooo':'Account[To]','dinco':'Account','dexpe':'Account','genis':'Account','ovede':'Account',
            'klass':'Category','tanfe':'Category','incom':'Category',
            'karen':'Currency','tkare':'Currency[To]',
            'price':'Price','tpric':'Price',
            'conda':'Top Class', 'conde':'Class',
            'targe':'Target Class', 'desci':'Description',
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
            'conda':'','conde':'',
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
            'ligua':'enMY',
            'natio':'',
        },
        'ligua':['enMY','zhTW'],
        'leve':{
            10:'Day',
            7:'Month',
            4:'Year',
            'Day':10,
            'Month':7,
            'Year':4,
        },
    }
    return dicto[text]
