# import telebot, sqlite3, os
# from telebot import types


# import os.path


# telegram_bot = telebot.TeleBot('7188110759:AAG5wYSv_W5MwDKrX5kE2hDrT8NDZWHJdGk')

# connection = sqlite3.connect('data.db', check_same_thread= False)
# cursor = connection.cursor()


# @telegram_bot.message_handler(commands=['start'])

# def bot_start(message):
#     keyboard = types.InlineKeyboardMarkup(row_width= 1)

#     get_user = types.InlineKeyboardButton(text='Get Users', callback_data='get_users')
#     get_product = types.InlineKeyboardButton(text='Get Product', callback_data='get_product')
#     add_product = types.InlineKeyboardButton(text='Add Product', callback_data='add_product')

#     keyboard.add(get_user, get_product, add_product)

#     telegram_bot.send_message(
#         chat_id=message.chat.id,
#         text='BOT MENU: ',
#         reply_markup=keyboard
#     )

#     print(message.message_thread_id)

# get_user_keyboard = types.InlineKeyboardMarkup()

# is_admin = types.InlineKeyboardButton(text='Provide administrator rights', callback_data= 'change_admin')
# not_admin = types.InlineKeyboardButton(text='Remove admininstrator rights', callback_data='remove_admin')

# # if row[5] == 1:
# #     get_user_keyboard.add(not_admin)
# # else:
# #     get_user_keyboard.add(is_admin)

# get_user_keyboard.add(not_admin, is_admin)

# @telegram_bot.callback_query_handler(func= lambda callback: True)

# def answer(callback):
#     if callback.data == 'get_users':
#         cursor.execute('SELECT * FROM user')
#         users = cursor.fetchall()
#         for user in users:
#             telegram_bot.send_message(
#                 callback.message.chat.id,
#                 text=f'Імʼя користувача: {user[1]}\nEmail користувача: {user[2]}\nПароль користувача: {user[3]}\nIs_admin: {user[5]}\n ',
#                 reply_markup=get_user_keyboard, 
#                 message_thread_id= 2
#             )


#     if callback.data == 'get_product':
#         cursor.execute('SELECT * FROM product')
#         products = cursor.fetchall()
        
#         for product in products:
#             telegram_bot.send_message(
#                 callback.message.chat.id, 
#                 text= f'Імʼя продукту: {product[1]}\nЦіна продукту: {product[2]} грн\nКількість продукту: {product[3]} шт.\nЗнижка продукту: {product[4]}%\n ',
#                 message_thread_id= 3
#             )

#     if callback.data == 'add_product':
#         telegram_bot.send_message(callback.message.chat.id, text='ok', message_thread_id= 4)

#     if callback.data == 'change_admin':
#         cursor.execute('SELECT is_admin FROM user WHERE is_admin = 1')
#         print('change_admin')
#         # telegram_bot.send_message(callback.message.chat.id, text= f'Користувач: {user[1]}\n Is_admin: {user[5]}')

#     if callback.data == 'remove_admin':
#         cursor.execute('SELECT is_admin FROM user WHERE is_admin = 0')
#         print('remove_admin')

 
# telegram_bot.infinity_polling(none_stop = True)

import telebot, sqlite3
from telebot import types

telegram_bot = telebot.TeleBot('7188110759:AAG5wYSv_W5MwDKrX5kE2hDrT8NDZWHJdGk')

connection = sqlite3.connect('data.db', check_same_thread = False)
cursor = connection.cursor()

@telegram_bot.message_handler(commands=['start'])

def bot_start(message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)

    get_user = types.InlineKeyboardButton(text='Get Users', callback_data='get_users')
    get_product = types.InlineKeyboardButton(text='Get Product', callback_data='get_product')
    add_product = types.InlineKeyboardButton(text='Add Product', callback_data='add_product')

    keyboard.add(get_user, get_product, add_product)

    telegram_bot.send_message(
        chat_id= message.chat.id,
        text= 'BOT MENU:',
        reply_markup= keyboard
    )

def admin_changes(user_id, is_admin):
    is_admin_keyboard = types.InlineKeyboardMarkup()

    if is_admin:
        change_admin_button = types.InlineKeyboardButton(text='Remove admin rights', callback_data=f'remove_admin:{user_id}')
    else:
        change_admin_button = types.InlineKeyboardButton(text='Provide admin rights', callback_data=f'change_admin:{user_id}')

    delete_user_btn = types.InlineKeyboardButton(text='Delete User', callback_data=f'delete_user:{user_id}')

    is_admin_keyboard.add(change_admin_button, delete_user_btn)
    return is_admin_keyboard

def delete_product(product_id):
    del_product_keyboard = types.InlineKeyboardMarkup()
    del_product_btn = types.InlineKeyboardButton(text='Delete product', callback_data=f'product_del: {product_id}')
    del_product_keyboard.add(del_product_btn)

    return del_product_keyboard

@telegram_bot.callback_query_handler(func=lambda callback: True)

def answer(callback):
    if callback.data == 'get_users':
        cursor.execute('SELECT * FROM user')
        users = cursor.fetchall()

        for user in users:
            user_id = user[0]
            is_admin = user[5]

            telegram_bot.send_message(
                callback.message.chat.id,
                text=f'Імʼя користувача: {user[1]}\nEmail користувача: {user[2]}\nПароль користувача: {user[3]}\nIs_admin: {is_admin}\n ',
                reply_markup= admin_changes(user_id, is_admin),
                message_thread_id= 2
            )

    elif callback.data == 'get_product':
        cursor.execute('SELECT * FROM product')
        products = cursor.fetchall()

        for product in products:

            product_id = product[0]

            telegram_bot.send_message(
                callback.message.chat.id,
                text= f'Імʼя продукту: {product[1]}\nЦіна продукту: {product[2]} грн\nКількість продукту: {product[3]} шт.\nЗнижка продукту: {product[4]}%\n ',
                message_thread_id= 3,
                reply_markup= delete_product(product_id)
            )

    elif callback.data == 'add_product':
        telegram_bot.send_message(
            callback.message.chat.id, 
            text='ok',
            message_thread_id= 4
        )

    elif 'change_admin' in callback.data:
        user_id = callback.data.split(':')[1]

        cursor.execute('UPDATE user SET is_admin = 1 WHERE id = ?', (user_id))
        connection.commit()

        telegram_bot.send_message(callback.message.chat.id, text='Admin rights provided.', message_thread_id= 2)

    elif 'remove_admin' in callback.data:
        user_id = callback.data.split(':')[1]
        cursor.execute('UPDATE user SET is_admin = 0 WHERE id = ?', (user_id))
        connection.commit()

        telegram_bot.send_message(callback.message.chat.id, text='Admin rights removed.', message_thread_id= 2)

    elif 'delete_user' in callback.data:
        user_id = callback.data.split(':')[1]

        confirm_keyboard = types.InlineKeyboardMarkup()

        confirm_button = types.InlineKeyboardButton(text='Confirm Delete', callback_data=f'confirm_delete:{user_id}')
        cancel_button = types.InlineKeyboardButton(text='Cancel', callback_data='cancel')

        confirm_keyboard.add(confirm_button, cancel_button)

        telegram_bot.send_message(callback.message.chat.id, text='Видалити цього користувача?', reply_markup=confirm_keyboard, message_thread_id= 2)

    elif 'confirm_delete' in callback.data:
        user_id = callback.data.split(':')[1]
        cursor.execute('DELETE FROM user WHERE id = ?', (user_id, ))

        connection.commit()

        telegram_bot.send_message(callback.message.chat.id, text='Користувача видалено з бази даних.', message_thread_id= 2)

    elif callback.data == 'cancel':
        telegram_bot.send_message(callback.message.chat.id, text='Дію скасовано.', message_thread_id= 2)

    elif 'product_del' in callback.data:
        product_id = callback.data.split(':')[1]
        cursor.execute('DELETE FROM product WHERE id = ?', (product_id, ))

        connection.commit()

        telegram_bot.send_message(callback.message.chat.id, text='Продукт видалено з бази даних.', message_thread_id= 3)

# telegram_bot.infinity_polling(none_stop=True)
