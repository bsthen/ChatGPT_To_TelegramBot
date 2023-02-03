'''
OpenAI ChatGPT-3 To TelegramBot
'''


import os
import openai as ai
from telebot import TeleBot
from dotenv import load_dotenv

load_dotenv()

ai.api_key = os.getenv("OPENAI_API_KEY")

def generate_gpt3_response(user_text, print_output=False):
    """
    Query OpenAI GPT-3 for the specific key and get back a response
    :type user_text: str the user's text to query for
    :type print_output: boolean whether or not to print the raw output JSON
    """
    completions = ai.Completion.create(
        engine='text-davinci-003',  # Determines the quality, speed, and cost.
        temperature=0.5,            # Level of creativity in the response
        prompt=user_text,           # What the user typed in
        max_tokens=100,             # Maximum tokens in the prompt AND response
        n=1,                        # The number of completions to generate
        stop=None,                  # An optional setting to control response generation
    )

    # Displaying the output can be helpful if things go wrong
    if print_output:
        print(completions)

    # Return the first choice's text
    return completions.choices[0].text

## Path: Telegram
app = TeleBot(__name__)

@app.route('(?!/).+')
def chatgpt(message):
    '''
    Function to handle telegram messages
    '''
    chat_dest = message['chat']['id']
    print("ID is: ",message['chat']['id']) # Print the chat ID Of Telegram User
    print("Msg sent: ",message['text']) # Print the message sent by the user
    user_msg = generate_gpt3_response(message['text'])
    print("Bot Respone: ",user_msg) # Print the response of the ChatGPT
    msg = f"ChatGPT: {user_msg}"
    app.send_message(chat_dest, msg)

if __name__ == '__main__':
    app.config['api_key'] = os.getenv("TELEGRAM_API_KEY")
    app.poll(debug=True)
    