from scraper import get_blue
from send_message import send_message
import os

CHAT_IDS = [os.environ.get("TELEGRAM_CHAT_ID")]

def main():
    #gets buy and sell values
    buy, sell = get_blue()
    #sends the message to the chat ids
    for chat_id in CHAT_IDS:
        send_message(buy, sell, chat_id)

if __name__ == "__main__":
    main()
