from pyrogram import Client, idle
from plugins.cb_data import app as Client2
from config import *



bot = Client(

           "Renamer",

           bot_token=7055338137:AAFgB8eDvyEo4JZQbgtmGoz4P8lngDgRHsc,

           api_id=23163380,

           api_hash=2dca155e786c7db2d295e5b4ab10783b,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
