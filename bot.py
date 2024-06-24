import telebot, sqlite3, os
from telebot import types

bot = telebot.TeleBot('7188110759:AAG5wYSv_W5MwDKrX5kE2hDrT8NDZWHJdGk')

connection = sqlite3.connect('data.db')
cursor = connection.cursor()


cursor.execute('SELECT * FROM user, product')

output = cursor.fetchall()
for row in output:
  print(row)



@bot.message_handler(commands=['start'])

def bot_start(message):
    keyboard = types.InlineKeyboardMarkup(row_width= 1)

    get_user = types.InlineKeyboardButton(text='Get Users', callback_data='get_users')
    get_product = types.InlineKeyboardButton(text='Get Product', callback_data='get_product')
    add_product = types.InlineKeyboardButton(text='Add Product', callback_data='add_product')

    keyboard.add(get_user, get_product, add_product)

    bot.send_message(
        chat_id=message.chat.id,
        text='BOT MENU: ',
        reply_markup=keyboard
    )

    print(message.message_thread_id)

get_user_keyboard = types.InlineKeyboardMarkup()

is_admin = types.InlineKeyboardButton(text='Provide administrator rights', callback_data= 'change_admin')
not_admin = types.InlineKeyboardButton(text='Remove admininstrator rights', callback_data='remove_admin')

if row[5] == 1:
    get_user_keyboard.add(not_admin)
else:
    get_user_keyboard.add(is_admin)

@bot.callback_query_handler(func= lambda callback: True)

def answer(callback):
    
    if callback.data == 'get_users':
        bot.send_message(
            callback.message.chat.id, 
            text= f'Імʼя користувача: {row[1]}\nEmail користувача: {row[2]}\nПароль користувача: {row[3]}\nIs_admin: {row[5]}\n ',
            message_thread_id= 2,
            reply_markup= get_user_keyboard
        )

    if callback.data == 'get_product':
        bot.send_message(
            callback.message.chat.id, 
            text= f'Імʼя продукту: {row[7]}\nЦіна продукту: {row[8]} грн\nКількість продукту: {row[9]} шт.\nЗнижка продукту: {row[10]}%\n ',
            message_thread_id= 3
        )
    
    if callback.data == 'add_product':
        bot.send_message(callback.message.chat.id, text='ok', message_thread_id= 4)

    if callback.data == 'change_admin':
        cursor.execute('SELECT is_admin FROM user WHERE is_admin = 0')
        print(row[5])

    if callback.data == 'remove_admin':
        cursor.execute('SELECT is_admin FROM user WHERE is_admin = 1')
        print(row[5])


 
    
connection.close()
bot.infinity_polling(none_stop = True)