'''
OpenAI ChatGPT-3.5 To TelegramBot
'''


import os
import openai
from telebot import TeleBot
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

app = TeleBot(__name__)

@app.route('(?!/).+')

def chatgpt(message):
    '''
    Function to handle the chatgpt bot
    '''
    chat_dest = message['chat']['id']
    print("ID is: ",message['chat']['id'])
    print("Msg sent: ",message['text'])
    user_msg = chatgpt_response(message['text'])
    print("Bot Respone: ",user_msg)
    msg = f"ChatGPT🤖:  {user_msg}"
    app.send_message(chat_dest, msg)

if __name__ == '__main__':
    app.config['api_key'] = os.getenv("TELEGRAM_API_KEY")
    app.poll(debug=True)
    