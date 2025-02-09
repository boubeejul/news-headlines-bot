import os
from api import get_headlines
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, CallbackContext, CallbackQueryHandler

load_dotenv(override=True)
NEWSAPI_KEY = os.getenv('NEWSAPI_KEY')
TELEGRAM_KEY = os.getenv('TELEGRAM_KEY')
BUTTONS = [
        [InlineKeyboardButton("General", callback_data="general")],
        [InlineKeyboardButton("Technology", callback_data="technology")],
        [InlineKeyboardButton("Science", callback_data="science")],
        [InlineKeyboardButton("Business", callback_data="business")],
        [InlineKeyboardButton("Entertainment", callback_data="entertainment")],
        [InlineKeyboardButton("Health", callback_data="health")],
        [InlineKeyboardButton("Sports", callback_data="sports")],
]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_markup = InlineKeyboardMarkup(BUTTONS)

    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                   text="Hi! I'm NewsHeadlinesBot your daily news headlines bot! 🤓 📰")
    
    await update.message.reply_text("What do you want to read about today? 🤔",
                                    reply_markup=reply_markup)
    
# topic buttons
async def button_click(update: Update, context: CallbackContext):
    query = update.callback_query
    
    await query.answer() 
    await query.message.reply_text("Alright! Let me see... 🔎🔎🔎")

    headlines = await get_headlines(query.data, NEWSAPI_KEY)

    await query.message.reply_text("Here we go ⤵️⤵️⤵️")
    message = ''

    for i in range(len(headlines)):
        message += f"<b>{i+1} - {headlines[i]['title']}</b>\n↪️ {headlines[i]['url']}\n\n"
    
    await query.message.reply_text(message, parse_mode="HTML")


async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


if __name__ == '__main__':
    application = ApplicationBuilder().token(TELEGRAM_KEY).build()
    
    start_handler = CommandHandler('start', start)
    unknown_handler = MessageHandler(filters.COMMAND, unknown_command)

    application.add_handler(start_handler)
    application.add_handler(CallbackQueryHandler(button_click))
    application.add_handler(unknown_handler)
    
    application.run_polling()
