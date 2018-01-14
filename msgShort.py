class MsgShort:
    def __init__(self,lingua):
        if lingua == 'enMY' or lingua == 'SiMP':
            self.presys = 'This chatbot is UNDER CONSTRUCTING\nTelegram msg limit: 1 msg/s\n——————————\n'
            self.con = 'Create New Conversation'
            self.cof = '～～～～～～～～～～\nConversation Closed\n(Key word to start a new conv.)'
            self.refeson = 'This chatbot is UNDER CONSTRUCTING\n——————————\nRefreshing database...'
            self.refesfin = 'Refreshing Finished !\n～～～～～～～～～～\n'
            self.refka = 'Currency Rate Refreshing Finished !'
            self.rekeswd = '～～～～～～～～～～\nGive me a word or a number'
            self.kaDatte = 'Currency Rate Version: '
            self.bye = 'See you next time! Bye!\n(Conversation Closed !)'
            self.rgsWarn = "The keyword that you selected doesn't Exist or Expired\n～～～～～～～～～～\n"
            self.whatsnow = 'Try /whats_now '
            self.analitempo = 'abratio => btempo,ftempo,cokas,cokey,targe\natren => btempo,ftempo,leve,cokas,cokey'
            self.analiWarn = 'Fill in all the spaces'
            self.band = '～～～～～～～～～～\n'
            self.cband = '\n～～～～～～～～～～\n'
            self.spitpre = '--- PREV MSG ---\n'
            self.spitpost = '\n--- NEXT MSG ---'
            self.emptylist = 'Sorry, try fill in other blank before request list\n'
            self.emptysachi = 'Word? Search thing with /Search mode'
        elif lingua == 'hanT':
            self.presys = '本聊天機器人仍處於早期開發階段\nTelegram 訊息限制：每秒 1 封\n——————————\n'
            self.con = '建立新的對話'
            self.cof = '～～～～～～～～～～\n對話結束\n（輸入任意文字開始新的對話）'
            self.refeson = '本聊天機器人仍處於早期開發階段\n——————————\n更新資料庫'
            self.refesfin = '資料庫更新完畢！！\n～～～～～～～～～～\n'
            self.refka = '貨幣兌換率更新完畢！！\n'
            self.rekeswd = '～～～～～～～～～～\n給我一段 文字 或 數字'
            self.kaDatte = '貨幣兌換率版本：'
            self.bye = '後會有期！再見～\n（對話結束）'
            self.rgsWarn = "你打算選取的關鍵字似乎不存在或過期了\n～～～～～～～～～～\n",
            self.whatsnow = "試試看 /whats_now ",
            self.analitempo = 'abratio => btempo,ftempo,cokas,cokey,targe\natren => btempo,ftempo,leve,cokas,cokey'
            self.analiWarn = "請把所有空格填滿",
            self.band = '～～～～～～～～～～\n'
            self.cband = '\n～～～～～～～～～～\n'
            self.spitpre = '～文接上文～\n'
            self.spitpost = '\n～文接下文～'
            self.emptylist = '抱歉，請在索取項目列表前\n先嘗試填寫其他空格\n'
            self.emptysachi = '文字？如果要搜索，請使用搜索模式 /Search'
