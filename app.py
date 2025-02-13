from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import os

app = Flask(__name__)

# 从环境变量中获取 Line Bot 的信息
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
LINE_CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET")

# 如果没有环境变量，抛出异常
if not LINE_CHANNEL_ACCESS_TOKEN or not LINE_CHANNEL_SECRET:
    raise ValueError("LINE_CHANNEL_ACCESS_TOKEN or LINE_CHANNEL_SECRET is missing!")

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
lhandler = WebhookHandler(LINE_CHANNEL_SECRET)

@app.route("/", methods=["GET"])
def home():
    return "Line Bot is running on Vercel!"

# @app.route("/callback", methods=["POST"])
# def callback():
#     signature = request.headers.get("X-Line-Signature")
#     body = request.get_data(as_text=True)

#     try:
#         lhandler.handle(body, signature)
#     except InvalidSignatureError:
#         abort(400)

#     return "OK"

# @lhandler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     user_message = event.message.text
#     reply_message = f"你剛剛說: {user_message}"
#     line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply_message))
