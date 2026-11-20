import requests
import time
import os

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_message(text):
    if not TOKEN or not CHAT_ID:
        print("Ошибка: не заданы TOKEN или CHAT_ID в секретах!")
        return
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("Сообщение отправлено!")
        else:
            print(f"Ошибка отправки: {response.status_code}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    print("Бот запускается...")
    send_message("✅ Бот на GitHub Actions успешно запустился! Время: " + time.strftime("%Y-%m-%d %H:%M:%S"))
    print("Готово.")
