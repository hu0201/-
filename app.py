from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import os

app = Flask(__name__)

# 環境變數設定（Vercel 會從 Dashboard 設定這些變數）
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("x0/nMdJXcLnnzTuAWl9/ycB/OxX3Xit27KcGqLqL2+65+SADnpgdfkXljpN8YM19IO2aHN71koZXs+uA9TUDnenR4oq4CPCjB8qBRs+GB8A4bVsfyAypujqukiflcHbBA4eij6NAMvip0Kgzvro5VwdB04t89/1O/w1cDnyilFU=")
LINE_CHANNEL_SECRET = os.getenv("9e858e8ace715a2e717f772558445bde")

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
lhandler = WebhookHandler(LINE_CHANNEL_SECRET)

@app.route("/", methods=["GET"])
def home():
    return "Line Bot is running on Vercel!"

@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers.get("X-Line-Signature")
    body = request.get_data(as_text=True)

    try:
        lhandler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return "OK"

@lhandler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text
    reply_message = f"你剛剛說: {user_message}"
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply_message))

# Vercel 會自動執行 `index.py` 內的 `app`
if __name__ == "__main__":
    app.run()
