import logging

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
    hero_position = context.user_data['hero_position']

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I'm a bot, please talk to me!",
        reply_markup=get_keyboard(hero_position),
    )


async def new_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    new_map, hero_position = generate_map()
    context.user_data['map'] = new_map
    context.user_data['hero_position'] = hero_position

    map_ = preview_map(new_map, hero_position)

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=map_,
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    map_ = context.user_data['map']
    hero_position = context.user_data['hero_position']

    if query.data == 'top':
        hero_position[0] -= 1
    if query.data == 'down':
        hero_position[0] += 1

    if query.data == 'left':
        hero_position[1] -= 1
    if query.data == 'right':
        hero_position[1] += 1

    map_[hero_position[0]][hero_position[1]].was_visited = True

    preview_game_map = preview_map(map_, hero_position)

    logging.info(hero_position)

    await query.edit_message_text(
        text=preview_game_map,
        reply_markup=get_keyboard(hero_position),
    )


def start_bot(token: str):
    logging.info('бот стартовал')
    application = ApplicationBuilder().token(token).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('new', new_game))
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()
