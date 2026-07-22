from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route("/")
def home():
    return "Webhook aktif!"
@app.route("/test")
def test():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(
        url,
        json={
            "chat_id": CHAT_ID,
            "text": "🧪 TEST MONEYCATOR AI\n\n✅ Railway Online\n✅ Webhook OK\n✅ Telegram OK"
        }
    )

    return "Test berhasil!"
@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        if request.is_json:
    data = request.get_json(silent=True)

    signal = data.get("signal", "-")
    symbol = data.get("symbol", "-")
    timeframe = data.get("timeframe", "-")
    price = data.get("price", "-")

    icon = "🟢" if signal == "BUY" else "🔴"

    message = f"""{icon} MONEYCATOR AI

📈 Signal : {signal}
📊 Symbol : {symbol}
⏰ Timeframe : {timeframe}
💰 Entry : {price}"""

else:
    message = request.data.decode("utf-8")

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        requests.post(
            url,
            json={
                "chat_id": CHAT_ID,
                "text": message
            }
        )

        return "OK", 200

    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
