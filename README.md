# **<h1 align="center">SHOP WEBSITE</h1>**
## Учасники команди: 
> Team members
- Коцаба Анастасія
    https://github.com/AnastasiaKotsaba2010
- Швелідзе Крістіна
    https://github.com/KristinaShvelidze
- Сергієнко Валерія
    https://github.com/Valeria2009Serhiienko
- Федорова Христина
    https://github.com/Krissfedor
- Легар Денис
    https://github.com/denysUwU

## Опис проекту
> Description 
+ **Shop website** - це веб-застосунок, що надає змогу користувачам здійснювати онлайн покупки. На сайті можна переглядати товари, додавати у кошик та замовляти їх у потрібне місце. Якщо користувач є адміністратором, йому надається право редагувати опис продукту, а також додавати новий асортимент на сторінку. Усі дії відслідковуються
телеграм-ботом,доступ до якого має лише власник веб-магазину. Бот швидко допоможе вам знайти усіх користувачів та вміст їх кошиків, записаних у базу даних.

>Shop website - is a web application that enables users to make online purchases. On the website, you can view products, add them to the cart and order them at the right place. If the user is an administrator, he is given the right to edit the product description, as well as add a new assortment to the page. All actions are tracked by a
Telegram bot, which can only be accessed by the owner of the web store. The bot will quickly help you find all users and the contents of their carts stored in the database.

## [Демоверсія](https://anastasiiakotcaba.pythonanywhere.com/)/[Demo version](https://anastasiiakotcaba.pythonanywhere.com/)

## Корисність проекту 
> Usefulness
+ Цей проект корисний для новачків у веб-розробці, оскільки він охоплює всі основні аспекти створення повноцінного веб-сайту: від реалізації інтерфейсу користувача до роботи з базою даних. Він може бути використаний як основа для реальних проектів та замовлень, та є чудовою нагодою попрактикуватись у створенні flask-проектів. Отримавши знання, ви з легкістю зможете зробити повноцінний веб-магазин на замовлення.

> This project is useful for beginners in web development, as it covers all the main aspects of creating a full-fledged website: from implementing the user interface to working with the database. It can be used as a basis for real projects and orders, and is a great opportunity to practice creating flask projects. With the knowledge gained, you will easily be able to create a full-fledged customised web store.

## Як розпочати роботу з веб-магазином
> How to get started with a web store

 ### Необхідні моулі
> Required modules

- `flask`: фреймворк для створення веб-застосунків мовою програмування Python, що використовує шаблонізатор Jinja2. Модуль надає змогу створити 'каркас' веб-сайту з базовими можливостями.
> A framework for creating web applications in the Python programming language that uses the Jinja2 templating tool. The module allows you to create a 'shell' website with basic features.

- `flask_SQLAlchemy, sqlite3`: робота з базою даних. Модулі дозволяють створювати нові бази даних та вносити у них змінити.
> Working with the database. Modules allow you to create new databases and make changes to them.

- `flask_migrate`: модуль, що дозволяє проводити міграції (забезпечує успішне створення таблиць у базі даних). При записі даних у базу, обов'язково варто проводити міграції.
> Allows you to carry out migrations (ensures the successful creation of tables in the database). When recording data in the database, it is absolutely necessary to carry out migrations.

- `flask_login`: управління сесіями зареєстованого користувача.
> Management of registered user sessions.

- `flask_mail`: модуль, що надає можливості автоматичної відправки листа до електронної пошти користувача.
> Provides the ability to automatically send a letter to the user's e-mail.

- `pandas`: модуль для читання excel файлу, де зберігаються дані про асортимент продуктів.
> Reads an excel file, which stores data on the range of products.

- `openpyxl`: модуль надає можливість зручно додавати дані в кінець аркуша електронної таблиці.
> Provides an opportunity to conveniently add data to the end of a spreadsheet sheet.
 
- `os`: модуль, що швидко знаходить абсолютний шлях до потрібного файлу.
>  Quickly finds the absolute path to the desired file.

- `pyTelegramBotAPI (telebot)`: модуль, що дозволяє створювати телеграм бота за допомогою token-ключа, який генерує телеграм канал BotFather.
> Allows you to create bot telegrams using a token key that generates telegram channel BotFather.

  
