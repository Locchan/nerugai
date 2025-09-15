import logging
import os
import random
import sys
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
LOTS = [
    "Григорий Лепс",
    "Три раза и палтарашка",
    "Спортик 20",
    "Беломорканал",
    "Наказан",
    "Не думай",
    "Голодовка",
    "У меня лапки",
    "Дневальный",
    "Закрой ебало 30",
    "Выселение",
    "Налог на говно",
    "Дискотека",
    "Президентский отдых"
]
MAT_COUNTER = 0
MAT_TOTAL = 0

if BOT_TOKEN is None:
    print("TOKEN DAI!")
    sys.exit(1)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Не ругайся!")

async def mat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global MAT_COUNTER, MAT_TOTAL
    MAT_COUNTER+=1
    MAT_TOTAL+=1
    if MAT_COUNTER == 5:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"КРУТИМ! Мат №{MAT_COUNTER} ({MAT_TOTAL} всего).")
        roulette_result = await roulette()
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Приз: {roulette_result}")
        MAT_COUNTER = 0
        return
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Мат №{MAT_COUNTER} ({MAT_TOTAL} всего).")

async def roulette():
    return random.choice(LOTS)

if __name__ == '__main__':
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    start_handler = CommandHandler('start', start)
    mat_handler = CommandHandler('mat', mat)
    application.add_handler(start_handler)
    application.add_handler(mat_handler)

    application.run_polling()