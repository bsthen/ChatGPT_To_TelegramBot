'''
OpenAI ChatGPT-3.5 To TelegramBot
'''
import os
import openai
import telebot
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def chatgpt_response(user_message):
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{
            "role":"user",
            "content":user_message
        }]
    )
    return completion.choices[0].message['content']

app = telebot.TeleBot(os.getenv("TELEGRAM_API_KEY"))

@app.message_handler(content_types=['text'])

def chatgpt(message):
    '''
    Function to handle the chatgpt bot
    '''
    user_msg = chatgpt_response(message.text)
    print("User Message: ",message.text)
    print("Bot Respone: ",user_msg)
    msg = f"ChatGPT🤖:  {user_msg}"
    app.reply_to(message, msg, parse_mode='Markdown')

if __name__ == '__main__':
    app.polling()