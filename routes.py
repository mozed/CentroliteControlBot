from bottle import route, view, run, request
import telebot

TOKEN = 'AAFvOi0o7SbiuNrNk-T4rWD6McEtyQVUixQ'
APPNAME = 'CentCTB'

@route('/setWebhook')
def setWebhook():
    bot = telebot.Bot(TOKEN)
    botWebhookResult = bot.setWebhook(webhook_url='https://{}.azurewebsites.net/botHook'.format(APPNAME))
    return str(botWebhookResult)
@route('/botHook', method='POST')
def botHook():
    bot = telebot.Bot(TOKEN)
    update = telebot.update.Update.de_json(request.json, bot)
    bot.sendMessage(chat_id=update.message.chat_id, text=getSum(update.message.text, update.message.from_user.username))
    return 'OK'
def getSum(query, userName):
    try:
        splittedBySum = query.split('+')
        if len(splittedBySum) != 2:
            raise ValueError('Too complicated stuff')
        return str(int(splittedBySum[0]) + int(splittedBySum[1]))
    except:
        return  "I'm sorry, {}. I'm afraid I can't do that".format(userName)
