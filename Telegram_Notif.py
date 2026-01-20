import requests

BOT_TOKEN = "8427843416:AAEprI3gInXI4ynx-u5As8JcJW9nneIAyYM"
CHAT_ID = "1677264945"


def notify(text: str):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text
    }

    try:
        requests.post(url, data=data, timeout=5)
    except Exception as e:
        print("Ошибка отправки уведомления в Telegram:", e)

