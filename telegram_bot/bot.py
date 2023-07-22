import logging

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
)

from core.constants import DirectionTravel
from core.description import get_description_of_location
from core.map import generate_map, preview_map
from core.moving import moving

from .keyboard import get_keyboard


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

    if query.data == 'map':
        text = f'Карта странствий:\n\n{preview_map(map_, hero_position)}'
        await query.edit_message_text(
            text=text,
            reply_markup=get_keyboard(hero_position),
        )
        return

    if query.data == 'see':
        chat_id = update.effective_message.chat_id
        st = map_[hero_position[0]][hero_position[1]].description
        photo = open(f'fields_image/{st}.jpeg', 'rb')
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=photo,
            caption=st,
            reply_markup=get_keyboard(hero_position),
        )

    if query.data in ['hero', 'todo', 'stock']:
        await query.edit_message_text(
            text='Это все пока в разработки.',
            reply_markup=get_keyboard(hero_position),
        )
        return

    if query.data == 'map':
        await query.edit_message_text(
            text=preview_map(map_, hero_position),
            reply_markup=get_keyboard(hero_position),
        )
        return

    direction = DirectionTravel(query.data)
    moving(map_, hero_position, direction)
    text = get_description_of_location(map_, hero_position)

    logging.info(hero_position)

    await query.edit_message_text(
        text=text,
        reply_markup=get_keyboard(hero_position),
    )


def start_bot(token: str):
    logging.info('бот стартовал')
    application = ApplicationBuilder().token(token).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('new', new_game))
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()
