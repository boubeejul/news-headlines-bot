# News Headlines Bot
A simple Telegram bot for news headlines made with Python 3.12.3, NewsAPI and python-telegram-bot.

With a simple `/start`, the bot retrieves the last 5 headlines about a topic of your choice.

## Preview
### Starting
![Start command](https://github.com/user-attachments/assets/0e7d069d-865b-4f43-a0d1-805d27cdb50c)

### Selecting a topic
![Headlines preview](https://github.com/user-attachments/assets/ded24c15-e755-441e-82a7-d5339344fe3a)

## Installing
Rename the file `.env.sample` to `.env` and add your Telegram Bot and NewsAPI tokens/keys.

Create a virtual environment with all dependencies:
```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

Run `main.py` and start the bot!

## References
- [NewsAPI Docs](https://newsapi.org/docs)
- [python-telegram-bot Wiki](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Bot-API-Forward-Compatibility)
