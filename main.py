from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent,
    TextMessage, TextSendMessage,
)

from ape import *


app = Flask(__name__)


CHANNEL_SECRET = 'fb6e0fff9b27729e93a220d6048a51b1'
CHANNEL_ACCESS_TOKEN = 'jVxX50wN25w5gYtU57BK/bUVIBDi9g3pYCXMwJQlE7TIm31V1aO2GlTNCP+EQG4u7/n1CslzQYh/xJ+pRV0ObzP/iyeWQT99GnB1ustodjhvmuFpoEHLMHWW8q4o0bCdAs7fu5PbZIF3VQdbwR9o5gdB04t89/1O/w1cDnyilFU='

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)



def RunApp(request):
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'



@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # USER_ID = event.source.user_id
    text = event.message.text
    # line_bot_api.push_message(USER_ID,messages='え～私は、ですね')
    if text:
        print('token',event.reply_token)
        line_bot_api.reply_message(
            event.reply_token,
            [TextSendMessage(text=ape(text))]
        )



















    #
