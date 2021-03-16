# coding=utf8
from flask import Flask, request, abort

app = Flask(__name__)


@app.route("/webhook", methods=['GET'])
def webhook():
    VERIFY_TOKEN = "BBQHungAALL156___54ds5a6dsa"
    print(request)
    mode = request.args.get('hub.mode')
    sendToken = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    if mode == "subscribe" and sendToken == VERIFY_TOKEN:
        return challenge
    else:
        return "error"
    

@app.route("/", methods=['GET'])
def index():
    return "hello word"

# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     message = TextSendMessage(text=event.message.text)
#     line_bot_api.reply_message(
#         event.reply_token,
#         message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
