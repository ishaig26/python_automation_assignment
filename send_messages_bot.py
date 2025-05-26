import pandas as pd
from telegram import Bot
import time

# 🛠️ Replace this with YOUR bot token from BotFather
TELEGRAM_BOT_TOKEN = "7512176088:AAE5rmB8gdAhh0Gh3eYBT8IDhGaXnTj39CA"

# 🧾 Load the messages (you already created this earlier)
df = pd.read_csv("personalized_messages.csv")  # must contain a 'message' column

# 🧠 Create a Telegram bot object
bot = Bot(token=TELEGRAM_BOT_TOKEN)

# 📣 Send message to each user manually (since we don't have Telegram user IDs in the CSV)
# 👶 Let's test with your own chat first — you need your own chat ID!

# 📌 Step: Find your Telegram chat ID
# Go to https://t.me/userinfobot and type /start — it will show your chat ID

YOUR_CHAT_ID = "Isha26_bot"  # ← Replace this with your actual chat ID from @userinfobot

# 🐍 Loop through each message and send to yourself (demo/test)
for index, row in df.iterrows():
    message = row['message']

    try:
        bot.send_message(chat_id=YOUR_CHAT_ID, text=message)
        print(f"Sent message: {message}")
        time.sleep(1)  # to be kind and slow down
    except Exception as e:
        print(f"Error sending message: {e}")
