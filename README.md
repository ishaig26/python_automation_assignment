# 🎯 Event Data Automation Project

This project is part of an intern-level automation assignment using Python and pandas. It processes event attendee data to:

- ✅ Clean the dataset (remove duplicates, normalize values)
- ✅ Generate personalized messages
- ✅ Send messages via Telegram Bot

---

## 📁 Project Structure

| File | Description |
|------|-------------|
|  event_data.csv  | Raw attendee dataset |
|  clean_data.py  | Cleans the data (deduplication, normalization, flagging) |
|  cleaned_output.csv | Output of the cleaned dataset |
|  personalized_messages.py  | Generates personalized messages |
|  personalized_messages.csv | Final email-message pairs |
|  send_messages_bot.py  | Sends messages via Telegram (bonus) |

---

## 🧹 Step 1: Clean the Data

### Script: `clean_data.py`

- Removes duplicate emails
- Converts `"Yes"` / `"No"` → `True` / `False` in `has_joined_event`
- Flags missing or invalid LinkedIn URLs
- Flags missing job titles

**How to run:**

```bash
python clean_data.py

✍️ Step 2: Generate Personalized Messages
Script: personalized_messages.py
Generates messages using:

1. Name (from first_name or fallback to name)

2. has_joined_event status

3. Job Title (or "professional" if missing)

4. LinkedIn presence

How to run:
python personalized_messages.py
📄 Output: personalized_messages.csv

🔍 Example messages:
Hey Venkatesh, thanks for joining our session! As a freelance developer, we think you’ll love our upcoming AI workflow tools. Want early access?

Hi Arushi, sorry we missed you at the last event! We’re preparing another session that might better suit your interests as a Product Manager.

🤖 Bonus: Send Messages via Telegram
Script: send_messages_bot.py
Uses the Telegram API to send messages to yourself (or others, if you have their chat IDs).

🔐 Setup:
step 1: Create a bot via @BotFather
 step 2: Get your bot token
step 3: Get your own chat ID via @userinfobot

Replace in send_messages_bot.py:
TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
YOUR_CHAT_ID = "YOUR_CHAT_ID_HERE"
How to run:
python send_messages_bot.py
⚠️ Make sure you have installed python-telegram-bot:
pip install python-telegram-bot

🧑‍💻 Author
GitHub: @ishaig26
Assignment: Python & Automation Intern Task —  25 May 2025
Linkedin: linkedin.com/in/isha-gupta2607

