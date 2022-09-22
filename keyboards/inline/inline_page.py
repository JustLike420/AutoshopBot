# - *- coding: utf- 8 - *-
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.db_api.sqlite import *

count_page = 10


# Изменение подкатегории
def subcategory_open_edit_ap(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_all_subcategoriesx()
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"edit_subcategory_here:{get_categories[a][1]}:{remover}"))
        x += 1
    if len(get_categories) <= 10:
        pass
    elif len(get_categories) > count_page and remover < 10:
        nomer_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡", callback_data=f"edit_subcat_nextp:{remover + count_page}")
        keyboard.add(nomer_kb, next_kb)
    elif remover + count_page >= len(get_categories):
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅", callback_data=f"edit_subcat_prevp:{remover - count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        keyboard.add(prev_kb, nomer_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡", callback_data=f"edit_subcat_nextp:{remover + count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅", callback_data=f"edit_subcat_prevp:{remover - count_page}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
    return keyboard


# Следующая страница выбора подкатегории для изменения
def subcategory_edit_next_page_ap(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_all_subcategoriesx()
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"edit_subcategory_here:{get_categories[a][1]}:{remover}"))
        x += 1
    if remover + count_page >= len(get_categories):
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅", callback_data=f"edit_subcat_prevp:{remover - count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        keyboard.add(prev_kb, nomer_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡", callback_data=f"edit_subcat_nextp:{remover + count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅", callback_data=f"edit_subcat_prevp:{remover - count_page}")
        keyboard.add(prev_kb, nomer_kb, next_kb)

    return keyboard


# Предыдующая страница выбора подкатегории для изменения
def subcategory_edit_prev_page_ap(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_all_subcategoriesx()
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"edit_subcategory_here:{get_categories[a][1]}:{remover}"))
        x += 1
    if remover <= 0:
        nomer_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡", callback_data=f"edit_subcat_nextp:{remover + count_page}")
        keyboard.add(nomer_kb, next_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡", callback_data=f"edit_subcat_nextp:{remover + count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅", callback_data=f"edit_subcat_prevp:{remover - count_page}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
    return keyboard
################################################################################################
################################# СТРАНИЦЫ ИЗМЕНЕНИЯ КАТЕГОРИЙ #################################

# Стартовые страницы выбора категории для изменения
def category_open_edit_cat(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_all_subcategoriesx()
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"edit_cat_here:{get_categories[a][1]}:{remover}"))
        x += 1
    if len(get_categories) <= 10:
        pass
    elif len(get_categories) > count_page and remover < 10:
        nomer_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡", callback_data=f"edit_cat_nextp:{remover + count_page}")
        keyboard.add(nomer_kb, next_kb)
    elif remover + count_page >= len(get_categories):
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅", callback_data=f"edit_cat_prevp:{remover - count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        keyboard.add(prev_kb, nomer_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡", callback_data=f"edit_cat_nextp:{remover + count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅", callback_data=f"edit_cat_prevp:{remover - count_page}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
    return keyboard


# Следующая страница выбора категории для изменения
def category_edit_next_page_cat(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_all_subcategoriesx()
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"edit_cat_here:{get_categories[a][1]}:{remover}"))
        x += 1
    if remover + count_page >= len(get_categories):
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅", callback_data=f"edit_cat_prevp:{remover - count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        keyboard.add(prev_kb, nomer_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡", callback_data=f"edit_cat_nextp:{remover + count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅", callback_data=f"edit_cat_prevp:{remover - count_page}")
        keyboard.add(prev_kb, nomer_kb, next_kb)

    return keyboard


# Предыдующая страница выбора категории для изменения
def category_edit_prev_page_cat(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_all_subcategoriesx()
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"edit_cat_here:{get_categories[a][1]}:{remover}"))
        x += 1
    if remover <= 0:
        nomer_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡", callback_data=f"edit_cat_nextp:{remover + count_page}")
        keyboard.add(nomer_kb, next_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡", callback_data=f"edit_cat_nextp:{remover + count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅", callback_data=f"edit_cat_prevp:{remover - count_page}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
    return keyboard
# Стартовые страницы выбора категории для изменения
def category_open_edit_ap(remover, subcategory_id):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_categoriesx("*", subcategory_id=subcategory_id)
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"edit_category_here:{get_categories[a][1]}:{remover}"))
        x += 1
    if len(get_categories) <= 10:
        pass
    elif len(get_categories) > count_page and remover < 10:
        nomer_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡", callback_data=f"edit_catategory_nextp:{remover + count_page}")
        keyboard.add(nomer_kb, next_kb)
    elif remover + count_page >= len(get_categories):
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅", callback_data=f"edit_catategory_prevp:{remover - count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        keyboard.add(prev_kb, nomer_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡", callback_data=f"edit_catategory_nextp:{remover + count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅", callback_data=f"edit_catategory_prevp:{remover - count_page}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
    return keyboard


# Следующая страница выбора категории для изменения
def category_edit_next_page_ap(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_all_categoriesx()
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"edit_category_here:{get_categories[a][1]}:{remover}"))
        x += 1
    if remover + count_page >= len(get_categories):
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅", callback_data=f"edit_catategory_prevp:{remover - count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        keyboard.add(prev_kb, nomer_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡", callback_data=f"edit_catategory_nextp:{remover + count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅", callback_data=f"edit_catategory_prevp:{remover - count_page}")
        keyboard.add(prev_kb, nomer_kb, next_kb)

    return keyboard


# Предыдующая страница выбора категории для изменения
def category_edit_prev_page_ap(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_all_categoriesx()
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"edit_category_here:{get_categories[a][1]}:{remover}"))
        x += 1
    if remover <= 0:
        nomer_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡", callback_data=f"edit_catategory_nextp:{remover + count_page}")
        keyboard.add(nomer_kb, next_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡", callback_data=f"edit_catategory_nextp:{remover + count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅", callback_data=f"edit_catategory_prevp:{remover - count_page}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
    return keyboard

################################################################################################
################################### СТРАНИЦЫ СОЗДАНИЯ КАТЕГОРИИ ##################################
# Стартовые страницы выбора категории для добавления позиции
def category_open_create_ap(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_all_subcategoriesx()
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"create_category_here:{get_categories[a][1]}"))
        x += 1
    if len(get_categories) <= 10:
        pass
    elif len(get_categories) > count_page:
        nomer_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡", callback_data=f"create_category_nextp:{remover + count_page}")
        keyboard.add(nomer_kb, next_kb)
    return keyboard


# Следующая страница выбора категории для добавления позиции
def category_create_next_page_ap(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_all_subcategoriesx()
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"create_category_here:{get_categories[a][1]}"))
        x += 1
    if remover + count_page >= len(get_categories):
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅", callback_data=f"create_category_prevp:{remover - count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        keyboard.add(prev_kb, nomer_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡", callback_data=f"create_category_nextp:{remover + count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅", callback_data=f"create_category_prevp:{remover - count_page}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
    return keyboard


# Предыдующая страница выбора категории для добавления позиции
def category_create_previous_page_ap(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_all_subcategoriesx()
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"create_category_here:{get_categories[a][1]}"))
        x += 1
    if remover <= 0:
        nomer_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡", callback_data=f"create_category_nextp:{remover + count_page}")
        keyboard.add(nomer_kb, next_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡", callback_data=f"create_category_nextp:{remover + count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅", callback_data=f"create_category_prevp:{remover - count_page}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
    return keyboard

################################################################################################
################################### СТРАНИЦЫ СОЗДАНИЯ ПОЗИЦИЙ ##################################
# Стартовые страницы выбора категории для добавления позиции

def position_open_create_cat(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_all_subcategoriesx()
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"create_poscat_here:{get_categories[a][1]}"))
        x += 1
    if len(get_categories) <= 10:
        pass
    elif len(get_categories) > count_page:
        nomer_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡", callback_data=f"create_poscat_nextp:{remover + count_page}")
        keyboard.add(nomer_kb, next_kb)
    return keyboard


# Следующая страница выбора категории для добавления позиции
def position_create_next_page_cat(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_all_subcategoriesx()
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"create_poscat_here:{get_categories[a][1]}"))
        x += 1
    if remover + count_page >= len(get_categories):
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅", callback_data=f"create_poscat_prevp:{remover - count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        keyboard.add(prev_kb, nomer_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡", callback_data=f"create_poscat_nextp:{remover + count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅", callback_data=f"create_poscat_prevp:{remover - count_page}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
    return keyboard


# Предыдующая страница выбора категории для добавления позиции
def position_create_previous_page_cat(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_all_subcategoriesx()
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"create_poscat_here:{get_categories[a][1]}"))
        x += 1
    if remover <= 0:
        nomer_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡", callback_data=f"create_poscat_nextp:{remover + count_page}")
        keyboard.add(nomer_kb, next_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡", callback_data=f"create_poscat_nextp:{remover + count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅", callback_data=f"create_posact_prevp:{remover - count_page}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
    return keyboard

def position_open_create_ap(remover, subcategory_id):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_categoriesx("*", subcategory_id=subcategory_id)
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"create_position_here:{get_categories[a][1]}"))
        x += 1
    if len(get_categories) <= 10:
        pass
    elif len(get_categories) > count_page:
        nomer_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡", callback_data=f"create_position_nextp:{remover + count_page}:{subcategory_id}")
        keyboard.add(nomer_kb, next_kb)
    return keyboard


# Следующая страница выбора категории для добавления позиции
def position_create_next_page_ap(remover, subcategory_id):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_categoriesx("*", subcategory_id=subcategory_id)
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"create_position_here:{get_categories[a][1]}"))
        x += 1
    if remover + count_page >= len(get_categories):
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅", callback_data=f"create_position_prevp:{remover - count_page}:{subcategory_id}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        keyboard.add(prev_kb, nomer_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡", callback_data=f"create_position_nextp:{remover + count_page}:{subcategory_id}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅", callback_data=f"create_position_prevp:{remover - count_page}:{subcategory_id}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
    return keyboard


# Предыдующая страница выбора категории для добавления позиции
def position_create_previous_page_ap(remover, subcategory_id):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_categoriesx("*", subcategory_id=subcategory_id)
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"create_position_here:{get_categories[a][1]}"))
        x += 1
    if remover <= 0:
        nomer_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡", callback_data=f"create_position_nextp:{remover + count_page}:{subcategory_id}")
        keyboard.add(nomer_kb, next_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡", callback_data=f"create_position_nextp:{remover + count_page}:{subcategory_id}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅", callback_data=f"create_position_prevp:{remover - count_page}:{subcategory_id}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
    return keyboard


################################################################################################
################################## СТРАНИЦЫ ИЗМЕНЕНИЯ ПОЗИЦИЙ ##################################
########################################### Категории ##########################################
# Стартовые страницы категорий при изменении позиции
def position_open_edit_category_cat(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_all_subcategoriesx()
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"position_edit_subcat:{get_categories[a][1]}"))
        x += 1
    if len(get_categories) <= 10:
        pass
    elif len(get_categories) > count_page and remover < 10:
        nomer_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"edit_position_subcat_nextp:{remover + count_page}")
        keyboard.add(nomer_kb, next_kb)
    elif remover + count_page >= len(get_categories):
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"edit_position_subcat_prevp:{remover - count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        keyboard.add(prev_kb, nomer_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"edit_position_subcat_nextp:{remover + count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"edit_position_subcat_prevp:{remover - count_page}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
    return keyboard


# Следующая страница категорий при изменении позиции
def position_edit_next_page_category_cat(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_all_subcategoriesx()
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"position_edit_subcat:{get_categories[a][1]}"))
        x += 1
    if remover + count_page >= len(get_categories):
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"edit_position_subcat_prevp:{remover - count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        keyboard.add(prev_kb, nomer_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"edit_position_subcat_nextp:{remover + count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"edit_position_subcat_prevp:{remover - count_page}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
    return keyboard


# Предыдующая страница категорий при изменении позиции
def position_edit_previous_page_category_cat(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_all_subcategoriesx()
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"position_edit_subcat:{get_categories[a][1]}"))
        x += 1
    if remover <= 0:
        nomer_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"edit_position_subcat_nextp:{remover + count_page}")
        keyboard.add(nomer_kb, next_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"edit_position_subcat_nextp:{remover + count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"edit_position_subcat_prevp:{remover - count_page}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
    return keyboard
# Стартовые страницы категорий при изменении позиции
def position_open_edit_category_ap(remover, subcategory_id):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_categoriesx("*", subcategory_id=subcategory_id)
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"position_edit_category:{get_categories[a][1]}"))
        x += 1
    if len(get_categories) <= 10:
        pass
    elif len(get_categories) > count_page and remover < 10:
        nomer_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"edit_position_category_nextp:{remover + count_page}")
        keyboard.add(nomer_kb, next_kb)
    elif remover + count_page >= len(get_categories):
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"edit_position_category_prevp:{remover - count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        keyboard.add(prev_kb, nomer_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"edit_position_category_nextp:{remover + count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"edit_position_category_prevp:{remover - count_page}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
    return keyboard


# Следующая страница категорий при изменении позиции
def position_edit_next_page_category_ap(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_all_categoriesx()
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"position_edit_category:{get_categories[a][1]}"))
        x += 1
    if remover + count_page >= len(get_categories):
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"edit_position_category_prevp:{remover - count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        keyboard.add(prev_kb, nomer_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"edit_position_category_nextp:{remover + count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"edit_position_category_prevp:{remover - count_page}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
    return keyboard


# Предыдующая страница категорий при изменении позиции
def position_edit_previous_page_category_ap(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_all_categoriesx()
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"position_edit_category:{get_categories[a][1]}"))
        x += 1
    if remover <= 0:
        nomer_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"edit_position_category_nextp:{remover + count_page}")
        keyboard.add(nomer_kb, next_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"edit_position_category_nextp:{remover + count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"edit_position_category_prevp:{remover - count_page}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
    return keyboard


########################################### ПОЗИЦИИ ##########################################
# Стартовые страницы позиций для их изменения
def position_open_edit_ap(remover, category_id):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_positions = get_positionsx("*", category_id=category_id)
    for a in range(remover, len(get_positions)):
        if x < count_page:
            get_items = get_itemsx("*", position_id=get_positions[a][1])
            keyboard.add(InlineKeyboardButton(f"{get_positions[a][2]} | {get_positions[a][3]}руб | {len(get_items)}шт",
                                              callback_data=f"position_edit:{get_positions[a][1]}:{remover}:{category_id}"))
        x += 1
    if len(get_positions) <= 10:
        pass
    elif len(get_positions) > count_page and remover < 10:
        nomer_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"edit_position_nextp:{remover + count_page}:{category_id}")
        keyboard.add(nomer_kb, next_kb)
    elif remover + count_page >= len(get_positions):
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"edit_position_prevp:{remover - count_page}:{category_id}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        keyboard.add(prev_kb, nomer_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"edit_position_nextp:{remover + count_page}:{category_id}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"edit_position_prevp:{remover - count_page}:{category_id}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
    # keyboard.add(InlineKeyboardButton("⬅ Вернуться ↩",
    #                                   callback_data=f"back_to_category"))
    return keyboard


# Следующая страница позиций для их изменения
def position_edit_next_page_ap(remover, category_id):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_positions = get_positionsx("*", category_id=category_id)
    for a in range(remover, len(get_positions)):
        if x < count_page:
            get_items = get_itemsx("*", position_id=get_positions[a][1])
            keyboard.add(InlineKeyboardButton(f"{get_positions[a][2]} | {get_positions[a][3]}руб | {len(get_items)}шт",
                                              callback_data=f"position_edit:{get_positions[a][1]}:{remover}:{category_id}"))
        x += 1
    if remover + count_page >= len(get_positions):
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"edit_position_prevp:{remover - count_page}:{category_id}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        keyboard.add(prev_kb, nomer_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"edit_position_nextp:{remover + count_page}:{category_id}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"edit_position_prevp:{remover - count_page}:{category_id}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
    keyboard.add(InlineKeyboardButton("⬅ Вернуться ↩",
                                      callback_data=f"back_to_category"))
    return keyboard


# Предыдующая страница позиций для их изменения
def position_edit_previous_page_ap(remover, category_id):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_positions = get_positionsx("*", category_id=category_id)
    for a in range(remover, len(get_positions)):
        if x < count_page:
            get_items = get_itemsx("*", position_id=get_positions[a][1])
            keyboard.add(InlineKeyboardButton(f"{get_positions[a][2]} | {get_positions[a][3]}руб | {len(get_items)}шт",
                                              callback_data=f"position_edit:{get_positions[a][1]}:{remover}:{category_id}"))
        x += 1
    if remover <= 0:
        nomer_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"edit_position_nextp:{remover + count_page}:{category_id}")
        keyboard.add(nomer_kb, next_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"edit_position_nextp:{remover + count_page}:{category_id}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"edit_position_prevp:{remover - count_page}:{category_id}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
    keyboard.add(InlineKeyboardButton("⬅ Вернуться ↩",
                                      callback_data=f"back_to_category"))
    return keyboard


################################################################################################
################################## СТРАНИЦЫ ДОБАВЛЕНИЯ ТОВАРОВ #################################
# подкатегории
def item_open_add_category_cat(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_all_subcategoriesx()
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"item_add_subcat:{get_categories[a][1]}"))
        x += 1
    if len(get_categories) <= 10:
        pass
    elif len(get_categories) > count_page and remover < 10:
        nomer_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"add_item_subcat_nextp:{remover + count_page}")
        keyboard.add(nomer_kb, next_kb)
    elif remover + count_page >= len(get_categories):
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"add_item_subcat_prevp:{remover - count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        keyboard.add(prev_kb, nomer_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"add_item_subcat_nextp:{remover + count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"add_item_subcat_prevp:{remover - count_page}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
    return keyboard


# Следующая страница категорий при добавлении товара
def item_add_next_page_category_cat(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_all_subcategoriesx()
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"item_add_subcat:{get_categories[a][1]}"))
        x += 1
    if remover + count_page >= len(get_categories):
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"add_item_subcat_prevp:{remover - count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        keyboard.add(prev_kb, nomer_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"add_item_subcat_nextp:{remover + count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"add_item_subcat_prevp:{remover - count_page}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
    return keyboard


# Предыдующая страница категорий при добавлении товара
def item_add_previous_page_category_cat(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_all_subcategoriesx()
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"item_add_subcat:{get_categories[a][1]}"))
        x += 1
    if remover <= 0:
        nomer_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"add_item_subcat_nextp:{remover + count_page}")
        keyboard.add(nomer_kb, next_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"add_item_subcat_nextp:{remover + count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"add_item_subcat_prevp:{remover - count_page}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
    return keyboard
# Стартовые страницы категорий при добавлении товара
def item_open_add_category_ap(remover, category_id):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_categoriesx("*", subcategory_id=category_id)
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"item_add_category:{get_categories[a][1]}"))
        x += 1
    if len(get_categories) <= 10:
        pass
    elif len(get_categories) > count_page and remover < 10:
        nomer_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"add_item_category_nextp:{remover + count_page}")
        keyboard.add(nomer_kb, next_kb)
    elif remover + count_page >= len(get_categories):
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"add_item_category_prevp:{remover - count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        keyboard.add(prev_kb, nomer_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"add_item_category_nextp:{remover + count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"add_item_category_prevp:{remover - count_page}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
    return keyboard


# Следующая страница категорий при добавлении товара
def item_add_next_page_category_ap(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_all_categoriesx()
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"item_add_category:{get_categories[a][1]}"))
        x += 1
    if remover + count_page >= len(get_categories):
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"add_item_category_prevp:{remover - count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        keyboard.add(prev_kb, nomer_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"add_item_category_nextp:{remover + count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"add_item_category_prevp:{remover - count_page}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
    return keyboard


# Предыдующая страница категорий при добавлении товара
def item_add_previous_page_category_ap(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_all_categoriesx()
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"item_add_category:{get_categories[a][1]}"))
        x += 1
    if remover <= 0:
        nomer_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"add_item_category_nextp:{remover + count_page}")
        keyboard.add(nomer_kb, next_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"add_item_category_nextp:{remover + count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"add_item_category_prevp:{remover - count_page}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
    return keyboard


########################################### ПОЗИЦИИ ##########################################
# Стартовые страницы позиций для добавления товаров
def position_add_item_position_ap(remover, category_id):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_positions = get_positionsx("*", category_id=category_id)
    for a in range(remover, len(get_positions)):
        if x < count_page:
            get_items = get_itemsx("*", position_id=get_positions[a][1])
            keyboard.add(InlineKeyboardButton(f"{get_positions[a][2]} | {get_positions[a][3]}руб | {len(get_items)}шт",
                                              callback_data=f"item_add_position:{get_positions[a][1]}:{remover}:{category_id}"))
        x += 1
    if len(get_positions) <= 10:
        pass
    elif len(get_positions) > count_page and remover < 10:
        nomer_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"add_item_position_nextp:{remover + count_page}:{category_id}")
        keyboard.add(nomer_kb, next_kb)
    elif remover + count_page >= len(get_positions):
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"add_item_position_prevp:{remover - count_page}:{category_id}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        keyboard.add(prev_kb, nomer_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"add_item_position_nextp:{remover + count_page}:{category_id}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"add_item_position_prevp:{remover - count_page}:{category_id}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
    # keyboard.add(InlineKeyboardButton("⬅ Вернуться ↩", callback_data=f"back_add_item_to_category:{category_id}"))
    return keyboard


# Следующая страница позиций для добавления товаров
def position_edit_next_page_position_ap(remover, category_id):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_positions = get_positionsx("*", category_id=category_id)
    for a in range(remover, len(get_positions)):
        if x < count_page:
            get_items = get_itemsx("*", position_id=get_positions[a][1])
            keyboard.add(InlineKeyboardButton(f"{get_positions[a][2]} | {get_positions[a][3]}руб | {len(get_items)}шт",
                                              callback_data=f"item_add_position:{get_positions[a][1]}:{remover}:{category_id}"))
        x += 1
    if remover + count_page >= len(get_positions):
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"add_item_position_prevp:{remover - count_page}:{category_id}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        keyboard.add(prev_kb, nomer_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"add_item_position_nextp:{remover + count_page}:{category_id}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"add_item_position_prevp:{remover - count_page}:{category_id}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
    keyboard.add(InlineKeyboardButton("⬅ Вернуться ↩", callback_data=f"back_add_item_to_category"))
    return keyboard


# Предыдующая страница позиций для добавления товаров
def position_edit_previous_page_position_ap(remover, category_id):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_positions = get_positionsx("*", category_id=category_id)
    for a in range(remover, len(get_positions)):
        if x < count_page:
            get_items = get_itemsx("*", position_id=get_positions[a][1])
            keyboard.add(InlineKeyboardButton(f"{get_positions[a][2]} | {get_positions[a][3]}руб | {len(get_items)}шт",
                                              callback_data=f"item_add_position:{get_positions[a][1]}:{remover}:{category_id}"))
        x += 1
    if remover <= 0:
        nomer_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"add_item_position_nextp:{remover + count_page}:{category_id}")
        keyboard.add(nomer_kb, next_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"add_item_position_nextp:{remover + count_page}:{category_id}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"add_item_position_prevp:{remover - count_page}:{category_id}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
    keyboard.add(InlineKeyboardButton("⬅ Вернуться ↩", callback_data=f"back_add_item_to_category"))
    return keyboard


################################################################################################
################################## СТРАНИЦЫ ПОКУПКИ ТОВАРОВ #################################
# Стартовые страницы подкатегорий при покупке товара
def buy_item_open_subcategory_ap(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    # get_categories = get_all_categoriesx()
    get_subcategories = get_all_subcategoriesx()
    for a in range(remover, len(get_subcategories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_subcategories[a][2]}",
                                              callback_data=f"buy_open_subcategory:{get_subcategories[a][1]}"))
        x += 1
    if len(get_subcategories) <= 10:
        pass
    elif len(get_subcategories) > count_page and remover < 10:
        nomer_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"buy_subcategory_nextp:{remover + count_page}")
        keyboard.add(nomer_kb, next_kb)
    elif remover + count_page >= len(get_subcategories):
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"buy_subcategory_prevp:{remover - count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        keyboard.add(prev_kb, nomer_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"buy_subcategory_nextp:{remover + count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"buy_subcategory_prevp:{remover - count_page}")
        # back_kb = InlineKeyboardButton("⬅ Вернуться ↩",
        #                                         callback_data=f"back_category_edit:{remover}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
        # keyboard.add(back_kb)
    return keyboard


# Следующая страница категорий при покупке товара
def buy_item_next_page_subcategory_ap(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_all_subcategoriesx()
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"buy_open_subcategory:{get_categories[a][1]}"))
        x += 1
    if remover + count_page >= len(get_categories):
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"buy_subcategory_prevp:{remover - count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        keyboard.add(prev_kb, nomer_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"buy_subcategory_nextp:{remover + count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"buy_subcategory_prevp:{remover - count_page}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
    return keyboard


# Предыдующая страница категорий при покупке товара
def buy_item_previous_page_subcategory_ap(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_all_subcategoriesx()
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"buy_open_subcategory:{get_categories[a][1]}"))
        x += 1
    if remover <= 0:
        nomer_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"buy_subcategory_nextp:{remover + count_page}")
        keyboard.add(nomer_kb, next_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"buy_subcategory_nextp:{remover + count_page}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"buy_subcategory_prevp:{remover - count_page}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
    return keyboard


########################################### КАТЕГОРИИ ##########################################

# Стартовые страницы категорий при покупке товара
def buy_item_open_category_ap(remover, subcategory_id):
    x = 0
    keyboard = InlineKeyboardMarkup()
    # get_categories = get_all_categoriesx()
    get_categories = get_categoriesx("*", subcategory_id=subcategory_id)
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"buy_open_category:{get_categories[a][1]}"))
        x += 1
    if len(get_categories) <= 10:
        pass
    elif len(get_categories) > count_page and remover < 10:
        nomer_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"buy_category_nextp:{remover + count_page}:{subcategory_id}")
        keyboard.add(nomer_kb, next_kb)
    elif remover + count_page >= len(get_categories):
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"buy_category_prevp:{remover - count_page}:{subcategory_id}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        keyboard.add(prev_kb, nomer_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"buy_category_nextp:{remover + count_page}:{subcategory_id}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"buy_category_prevp:{remover - count_page}:{subcategory_id}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
    keyboard.add(InlineKeyboardButton("⬅ Вернуться ↩",
                                      callback_data=f"back_buy_item_to_subcategory"))
    return keyboard


# Следующая страница категорий при покупке товара
def buy_item_next_page_category_ap(remover, subcategory_id):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_categoriesx("*", subcategory_id=subcategory_id)
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"buy_open_category:{get_categories[a][1]}"))
        x += 1
    if remover + count_page >= len(get_categories):
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"buy_category_prevp:{remover - count_page}:{subcategory_id}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        keyboard.add(prev_kb, nomer_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"buy_category_nextp:{remover + count_page}:{subcategory_id}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"buy_category_prevp:{remover - count_page}:{subcategory_id}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
    keyboard.add(InlineKeyboardButton("⬅ Вернуться ↩",
                                      callback_data=f"back_buy_item_to_subcategory"))
    return keyboard


# Предыдующая страница категорий при покупке товара
def buy_item_previous_page_category_ap(remover, subcategory_id):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_categoriesx("*", subcategory_id=subcategory_id)
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"buy_open_category:{get_categories[a][1]}"))
        x += 1
    if remover <= 0:
        nomer_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"buy_category_nextp:{remover + count_page}:{subcategory_id}")
        keyboard.add(nomer_kb, next_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"buy_category_nextp:{remover + count_page}:{subcategory_id}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"buy_category_prevp:{remover - count_page}:{subcategory_id}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
    keyboard.add(InlineKeyboardButton("⬅ Вернуться ↩",
                                      callback_data=f"back_buy_item_to_subcategory"))
    return keyboard


########################################### ПОЗИЦИИ ##########################################
# Стартовые страницы позиций для покупки товаров
def buy_item_item_position_ap(remover, category_id):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_positions = get_positionsx("*", category_id=category_id)
    for a in range(remover, len(get_positions)):
        if x < count_page:
            get_items = get_itemsx("*", position_id=get_positions[a][1])
            keyboard.add(InlineKeyboardButton(f"{get_positions[a][2]} | {get_positions[a][3]}руб | {len(get_items)}шт",
                                              callback_data=f"buy_open_position:{get_positions[a][1]}:{remover}:{category_id}"))
        x += 1
    if len(get_positions) <= 10:
        pass
    elif len(get_positions) > count_page and remover < 10:
        nomer_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"buy_position_nextp:{remover + count_page}:{category_id}")
        keyboard.add(nomer_kb, next_kb)
    elif remover + count_page >= len(get_positions):
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"buy_position_prevp:{remover - count_page}:{category_id}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        keyboard.add(prev_kb, nomer_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"buy_position_nextp:{remover + count_page}:{category_id}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"buy_position_prevp:{remover - count_page}:{category_id}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
    keyboard.add(InlineKeyboardButton("⬅ Вернуться ↩",
                                      callback_data=f"back_buy_item_to_category:{category_id}"))
    return keyboard


# Следующая страница позиций для покупки товаров
def item_buy_next_page_position_ap(remover, category_id):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_positions = get_positionsx("*", category_id=category_id)
    for a in range(remover, len(get_positions)):
        if x < count_page:
            get_items = get_itemsx("*", position_id=get_positions[a][1])
            keyboard.add(InlineKeyboardButton(f"{get_positions[a][2]} | {get_positions[a][3]}руб | {len(get_items)}шт",
                                              callback_data=f"buy_open_position:{get_positions[a][1]}:{remover}:{category_id}"))
        x += 1
    if remover + count_page >= len(get_positions):
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"buy_position_prevp:{remover - count_page}:{category_id}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        keyboard.add(prev_kb, nomer_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"buy_position_nextp:{remover + count_page}:{category_id}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"buy_position_prevp:{remover - count_page}:{category_id}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
    keyboard.add(InlineKeyboardButton("⬅ Вернуться ↩",
                                      callback_data=f"back_buy_item_to_category"))
    return keyboard


# Предыдующая страница позиций для покупки товаров
def item_buy_previous_page_position_ap(remover, category_id):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_positions = get_positionsx("*", category_id=category_id)
    for a in range(remover, len(get_positions)):
        if x < count_page:
            get_items = get_itemsx("*", position_id=get_positions[a][1])
            keyboard.add(InlineKeyboardButton(f"{get_positions[a][2]} | {get_positions[a][3]}руб | {len(get_items)}шт",
                                              callback_data=f"buy_open_position:{get_positions[a][1]}:{remover}:{category_id}"))
        x += 1
    if remover <= 0:
        nomer_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"buy_position_nextp:{remover + count_page}:{category_id}")
        keyboard.add(nomer_kb, next_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"buy_position_nextp:{remover + count_page}:{category_id}")
        nomer_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"buy_position_prevp:{remover - count_page}:{category_id}")
        keyboard.add(prev_kb, nomer_kb, next_kb)
    keyboard.add(InlineKeyboardButton("⬅ Вернуться ↩",
                                      callback_data=f"back_buy_item_to_category"))
    return keyboard
