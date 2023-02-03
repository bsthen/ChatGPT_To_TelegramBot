# ChatGPT_To_TelegramBot

 Connect ChatGPT To Telegram Bot

## Requirement

- Python3
- OpenAI
- Telegram Bot

## How To Use

- create virtual enviroment follow command below:

```bash
python3 -m venv env
```

Then activate command for MacOS or Linux:

```bash
source env/bin/activate
```

or command for Windows:

```bash
env\Scripts\activate.bat
```

Next step install dependency:

```bash
pip install -r requirements.txt
```

Next rename env.sample to .env file.

## Get OpenAI Token

Register an account with OpenAI and then go to this link [<https://beta.openai.com/account/api-keys>](https://beta.openai.com/account/api-keys) and create token.
Paste Token to .env with OPENAI_API_KEY variable.

## Get Telegram Bot Token

Open Telegram App and search for [@BotFather](https://t.me/@BotFather)
Send /newbot to BotFather and follow the instruction with BotFather.

Finally, Copy bot token to .env file with TELEGRAM_API_KEY variable.

## Run The program

```bash
python3 main.py
```
