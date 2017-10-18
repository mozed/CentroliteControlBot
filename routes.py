"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime
import telebot

TOKEN = 'AAFvOi0o7SbiuNrNk-T4rWD6McEtyQVUixQ'
APPNAME = 'CentCTB'

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        message='Your contact page.',
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year
    )
@route('/setWebhook')
def setWebhook():
    bot = telebot.Bot(TOKEN)
    botWebhookResult = bot.setWebhook(webhook_url='https://{}.azurewebsites.net/botHook'.format(APPNAME))
    return str(botWebhookResult)
