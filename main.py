from scraper import get_blue
from send_message import send_message

CHAT_IDS = ["5586625183"]

def main():
    #gets buy and sell values
    buy, sell = get_blue()
    #sends the message to the chat ids
    for chat_id in CHAT_IDS:
        send_message(buy, sell, chat_id)
if __name__ == "__main__":
    main()
