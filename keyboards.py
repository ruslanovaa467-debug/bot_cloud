from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_start_menu_kb():
    builder = InlineKeyboardBuilder()
    builder.button(text="🎮 Приложения и игры", callback_data="main_menu")
    builder.button(text="🎧 Поддержка", callback_data="btn_support")
    builder.button(text="ℹ️ Информация", callback_data="btn_info")
    builder.adjust(1)
    return builder.as_markup()

def get_main_menu_kb(categories: dict):
    builder = InlineKeyboardBuilder()
    for key, data in categories.items():
        builder.button(text=data["title"], callback_data=f"cat_{key}")
    builder.button(text="🔙 В главное меню", callback_data="start_menu")
    builder.adjust(2) # 2 columns
    return builder.as_markup()

def get_category_items_kb(items: list, category_key: str):
    builder = InlineKeyboardBuilder()
    for item in items:
        # Truncate title if too long to fit nicely
        title = (item["title"][:25] + '..') if len(item["title"]) > 25 else item["title"]
        builder.button(text=title, callback_data=f"item_{item['id']}")
    
    builder.adjust(1)
    builder.button(text="🔙 Назад", callback_data="main_menu")
    return builder.as_markup()

def get_item_kb(category_key: str, item_id: str):
    builder = InlineKeyboardBuilder()
    builder.button(text="👉 ПОЛУЧИТЬ", callback_data=f"get_{item_id}")
    builder.button(text="🔙 Назад", callback_data=f"cat_{category_key}")
    builder.adjust(1)
    return builder.as_markup()
