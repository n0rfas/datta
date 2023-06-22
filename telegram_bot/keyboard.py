from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def get_keyboard() -> InlineKeyboardMarkup:

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

    return InlineKeyboardMarkup(keyboard)