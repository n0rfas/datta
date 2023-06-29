from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
)

from .keyboard import get_keyboard
from core.map import generate_map, preview_map


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I'm a bot, please talk to me!",
        reply_markup=get_keyboard([0, 1]),
    )


async def new_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    new_map, hero_position = generate_map()
    context.user_data['map'] = new_map
    context.user_data['hero_position'] = hero_position

    map_ = preview_map(new_map)

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=map_,
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    await query.edit_message_text(
        text=f"Selected option: {query.data}",
        reply_markup=get_keyboard([1, 1]),
    )


def start_bot(token: str):
    application = ApplicationBuilder().token(token).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('new', new_game))
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()
