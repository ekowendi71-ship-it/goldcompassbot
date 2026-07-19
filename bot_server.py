from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "8465910626:AAFxaiz9IQm1-Uy4s183StUPBdLy7SB2XzM"
CHAT_ID = "@moneycator"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    pesan = data.get("message", "Tidak ada pesan")

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": pesan
    })

    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
