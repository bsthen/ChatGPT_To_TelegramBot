'''
OpenAI ChatGPT-3.5 To TelegramBot
'''
import os
import openai
import telebot
from dotenv import load_dotenv
import time

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def chatgpt_response(user_message):
    while True:
        try:
            completion = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messages = [{
                    "role":"user",
                    "content":user_message
                }]
            )
            break
        except Exception:
            print("Bot is sleeping...")
            time.sleep(15)
    return completion.choices[0].message['content']

app = telebot.TeleBot(os.getenv("TELEGRAM_API_KEY"))

@app.message_handler(content_types=['text'])

def chatgpt(message):
    '''
    Function to handle the chatgpt with telegram bot
    '''
    app.send_chat_action(message.chat.id, 'typing')
    user_msg = chatgpt_response(message.text)
    app.reply_to(message, user_msg, parse_mode='Markdown')

if __name__ == '__main__':
    while True:
        try:
            app.polling(none_stop=True)
            print("Bot is running...")
        except Exception:
            time.sleep(15)
            print("Bot is sleeping...")