from flask import Flask, request, abort  # flask 架設伺服器 #jango另一個架設伺服器的套件

from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)

app = Flask(__name__)

configuration = Configuration(access_token='/YR3W9vmWJzEwfyy+xK0rgpMg0hiu705MtUlDJrCJHy0IU2GpL/c43ibwIVYshsWkh7IAJ0t4zd1wy7aBIruHwSBEuT0pdra9WbJhxXN/Pq2a7C8RIaoqlddgZglTTBH2WnrkvUlfOg0sXQm1Vs4SQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('c47b8f87f2ef895add287e21581e2678')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=event.message.text)]
            )
        )

if __name__ == "__main__":
    app.run()