from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")


@app.route("/")
def home():
    return "Moneycator Webhook Online"


@app.route("/test")
def test():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(
        url,
        json={
            "chat_id": CHAT_ID,
            "text": "🧪 TEST MONEYCATOR AI\n\n✅ Railway Online\n✅ Webhook OK"
        }
    )

    return "Test berhasil!"


@app.route("/webhook", methods=["POST"])
def webhook():
    try:

        if request.is_json:

            data = request.get_json(silent=True)

            signal = str(data.get("signal", "-")).upper()
            symbol = str(data.get("symbol", "-"))
            timeframe = str(data.get("timeframe", "-"))
            price = float(data.get("price", 0))

            # Ubah timeframe menjadi format Trading
            tf_map = {
                "1": "M1",
                "5": "M5",
                "15": "M15",
                "30": "M30",
                "45": "M45",
                "60": "H1",
                "120": "H2",
                "240": "H4",
                "D": "D1",
                "W": "W1",
                "M": "MN"
            }

            timeframe = tf_map.get(timeframe, timeframe)

            if signal == "BUY":
                icon = "🟢"
                tp1 = price + 5.00
                tp2 = price + 10.00
                sl = price - 8.00

            else:
                icon = "🔴"
                tp1 = price - 5.00
                tp2 = price - 10.00
                sl = price + 8.00

            message = f"""{icon} MONEYCATOR AI v2.0.1

📈 Signal : {signal}
📊 Symbol : {symbol}
⏰ Timeframe : {timeframe}

💰 Entry : {price:.2f}

🎯 TP1 : {tp1:.2f}
🎯 TP2 : {tp2:.2f}

🛑 Stop Loss : {sl:.2f}

━━━━━━━━━━━━━━
🤖 Powered by Moneycator AI"""

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
