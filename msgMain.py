def msgMain(lingua='enMY',tasta='',keyse={}):
    waaad = {
        'enMY':{
            'start':"""　Welcome
——————————
This is Money Money Come Chatbot.
It can help you to trace your money flow moreeasily (Sure? )

Notes:
　/setting
　　Please Setup before using
——————————
　/help
""",
            'help':"""　Help card (Command List)
——————————
　/help
　　Show command list
　/whats_now
　　Show current unsaved work
　/new
　　Create new record
　/list
　　Show prevous record
　/statics
　　View statistics card
　/start
　　Welcome and Introduction
　/setting
　　View setting card
　/exit
　　Close conversation
""",
            'bored':"""My "Job"　[ I am free ~ ]
——————————
　/start
　　Welcome Card
　/new
　　Creating New Record
　/list
　　Review Card
　/statics
　　Analystic Card
　/setting
　　Setting Card
""",
            'selection':"""Select @titil@
——————————
@titil@ List:
@txt@
——————————
　/Discard /Save　/Back
Remind:
　Select above or type another selection
""",
            'home':"""Keyword Card
——————————
I received your keyword:
　@keywo@

What do you want to do?
　/new　/list

　/statics
——————————
　/setting　/help
""",
            'timesout':"""Time's Out
——————————
Previous unsave work was CLEAN OUT.
""",
            'error':"""Status
——————————
Received wrong message
Input:
　Undetactable content type
""",
        },

        'hanT':{
            'start':"""　歡迎（歡迎卡）
——————————
這是錢錢旺旺來記賬機器人。
你可以使用本機器人來追蹤消費習慣和現金流動

備注：
　/setting
　　在使用前，請先完成設置
——————————
　/help
""",
            'help':"""　指令列表（指南卡）
——————————
　/help
　　顯示 指令列表（指南卡）
　/whats_now
　　顯示 目前未保存工作
　/new
　　創建 新記錄（創建卡）
　/list
　　顯示 舊紀錄（列表卡）
　/statics
　　顯示 統計卡
　/start
　　顯示 歡迎卡
　/setting
　　顯示 設定卡
　/exit
　　結束本次對話
""",
            'bored':""" 我的能力　[ 我閑著沒事~ ]
——————————
　/start
　　顯示 歡迎卡
　/new
　　創建 新記錄（創建卡）
　/list
　　顯示 舊紀錄（列表卡）
　/statics
　　顯示 統計卡
　/setting
　　顯示 設定卡
""",
            'selection':""" @titil@ 選單
——————————
@titil@ 列表:
@txt@
——————————
　/Discard /Save　/Back
備注:
　選擇任意項 或 輸入新的選項
""",
            'home':""" 關鍵詞卡
——————————
我收到的你給的關鍵詞：
　@keywo@

你想做什麽？
　/new　創建新記錄
　列出舊紀錄　/list
　/statics　統計
——————————
　/setting　/help
""",
            'timesout':""" 時間到了
——————————
未保存的工作將會清除

備注：
　時間限制是爲了避免堆積
　太多未完成工作
""",
            'error':""" 狀態警示
——————————
我收到錯誤訊息

輸入錯誤：
　無法處理的訊息類型
""",
        }
    }

    resut = waaad.get(lingua,{}).get(tasta,'')
    for keywo in list(keyse.keys()):
        resut = resut.replace("@"+keywo+"@",keyse.get(keywo,''))

    return resut
