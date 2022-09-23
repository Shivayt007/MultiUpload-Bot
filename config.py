import os

class Config(object):
   # The Telegram API things
   API_ID= int(2054877)
   API_HASH = '4227c1e45e462209a3dcc67ada88a44f'
   # get a token from @BotFather
   BOT_TOKEN = '5108987521:AAFzEtFz2HkP4FBYsyKkA9xyCfuGHWXn4EQ'
   # channel id = -100 (for logs)
   LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001690321915"))   
   # Array to store users who are authorized to use the bot 
   AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5650108471").split())    
   # force sub user to the channel (without @)
   CHNAME = os.environ.get("CHNAME", "hxbots")
