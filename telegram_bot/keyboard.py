from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from core.constants import CARS_SIZE


def get_keyboard(hero_position: tuple) -> InlineKeyboardMarkup:

    # main keyboard
    keyboard = [
        [
            InlineKeyboardButton('🤺', callback_data='hero'),
            InlineKeyboardButton('⬆️', callback_data='top'),
            InlineKeyboardButton('📑', callback_data='todo'),
        ],
        [
            InlineKeyboardButton('⬅️', callback_data='left'),
            InlineKeyboardButton('👀', callback_data='see'),
            InlineKeyboardButton('➡️', callback_data='right'),
        ],
        [
            InlineKeyboardButton('🎒', callback_data='stock'),
            InlineKeyboardButton('⬇️', callback_data='down'),
            InlineKeyboardButton('🗺', callback_data='map'),
        ],
    ]

    # if the hero is on the edge of the map - block the button
    wall_button = InlineKeyboardButton('*️⃣', callback_data='well')

    if hero_position[0] == 0:  # top
        keyboard[0][1] = wall_button
    elif hero_position[0] == CARS_SIZE - 1:  # down
        keyboard[2][1] = wall_button

    if hero_position[1] == 0:  # left
        keyboard[1][0] = wall_button
    elif hero_position[1] == CARS_SIZE - 1:  # right
        keyboard[1][2] = wall_button

    return InlineKeyboardMarkup(keyboard)
