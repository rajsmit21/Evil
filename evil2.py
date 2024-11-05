import telebot
import requests

# Replace with your actual Telegram Bot Token
TELEGRAM_TOKEN = '7754972192:AAH6iHnlnYYYx1nuZgwmCB2koOHWlCPZQEE'
bot = telebot.TeleBot(TELEGRAM_TOKEN)

def get_response_from_evilgpt(question):
    url = "https://white-evilgpt.ashlynn.workers.dev/"
    params = {
        "question": question,
        "state": "evilgpt"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        return data.get("message", "No message returned from API.")
    except requests.exceptions.RequestException as e:
        return f"Error connecting to API: {e}"
    except ValueError:
        return "Invalid response from API."

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome! Ask me anything.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    question = message.text
    response_message = get_response_from_evilgpt(question)

    # Check if the response message is empty
    if response_message:
        bot.reply_to(message, response_message)
    else:
        bot.reply_to(message, "Sorry, I didn't get a valid response.")

# Start polling
bot.polling()
