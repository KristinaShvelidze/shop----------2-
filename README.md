# **<h1 align="center">SHOP WEBSITE</h1>**
## Учасники команди: 
> Team members
- [Коцаба Анастасія / Kotsaba Anastasiia](https://github.com/AnastasiaKotsaba2010) 
- [Швелідзе Крістіна / Shvelidze Kristina ](https://github.com/KristinaShvelidze)
- [Федорова Христина / Fedorova Kristina](https://github.com/Krissfedor)
- [Сергієнко Валерія / Serhiienko Valeriia](https://github.com/Valeria2009Serhiienko)  
- [Легар Денис / Legar Denys](https://github.com/denysUwU)


## Опис проекту
> Description 
+ **Shop website** - це веб-застосунок, що надає змогу користувачам здійснювати онлайн покупки. На сайті можна переглядати товари, додавати у кошик та замовляти їх у потрібне місце. Якщо користувач є адміністратором, йому надається право редагувати опис продукту, а також додавати новий асортимент на сторінку. Усі дії відслідковуються
телеграм-ботом, доступ до якого має лише власник веб-магазину. Бот швидко допомагає знайти усіх користувачів та вміст їх кошиків, записаних у базу даних.

>Shop website - is a web application that enables users to make online purchases. On the website, you can view products, add them to the cart and order them at the right place. If the user is an administrator, he is given the right to edit the product description, as well as add a new assortment to the page. All actions are tracked by a
Telegram bot, which can only be accessed by the owner of the web store. The bot will quickly help you find all users and the contents of their carts stored in the database.

## [Демоверсія / Demo version](https://anastasiiakotcaba.pythonanywhere.com/)

## Корисність проекту 
> Usefulness
+ Цей проект корисний для новачків у веб-розробці, оскільки він охоплює всі основні аспекти створення повноцінного веб-сайту: від реалізації інтерфейсу користувача до роботи з базою даних. Він може бути використаний як основа для реальних проектів та замовлень, та є чудовою нагодою попрактикуватись у створенні flask-проектів. Отримавши знання, ви з легкістю зможете зробити повноцінний веб-магазин на замовлення.

> This project is useful for beginners in web development, as it covers all the main aspects of creating a full-fledged website: from implementing the user interface to working with the database. It can be used as a basis for real projects and orders, and is a great opportunity to practice creating flask projects. With the knowledge gained, you will easily be able to create a full-fledged customised web store.

## Як розпочати роботу з веб-магазином
> How to get started with a web store

 ### Необхідні модулі
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

### Інструкція по локальному запуску проекту
> Instructions for running the project locally

+ У терміналі папки з файлом setting.py варто прописати такі команди:
>In the terminal of the folder with the setting.py file, you should write the following commands:
   ```
   > flask --app settings db init
   > flask --app settings db migrate
   > flask --app settings db upgrade
   ```
### Інструкція по віддаленому запуску проекту
> Instructions for remote project launch

1. Виконати локальний запуск.
2. У браузері відкрити сайт **pythonanywhere**, створити аккаунт початківця (зареєструватись).
3. Підвердити email адресу.
4. Перейти у вкладку **Web**, створити новий веб-застосунок.
5. У модальному вікні, у розділі **Select a Python Web framework** обрати **Flask** та версію Python **3.10**.
6. Перейти у вкладку **Console** > **Bash**.
7. Створити віртуальне оточення, прописавши наступну команду у консолі:
   - ```mkvirtualenv (назва віртуального оточення) -- python = python 3.10```
8. Встановити усі необхідні модулі, які були використані у проекті:
   - ```pip install flask, flask_sqlalchemy, flask_migrate, flask_login, flask_mail, pandas, openpyxl, sqlite3, pyTelegramBotAPI```
9. Завантажити файли проекту: у bush-консолі прописати команди:
   
    -  ```pwd - дізнатись поточну директорію```
    - ```cd mysite - перейти у папку mysite```
    - ```git clone (посилання на git-репозиторій)```
     
 11. Перейти у вкладку **Web**, прогортати вниз до розділу **Code**:
     
     - ```У пунктах Source code та Working directory, вкінці шляху дописати: /mysite/(назва папки з проектом)```
     - ```Перейти на посилання у панкті WSGI configuration file```
     - ```У 16-ому рядку замінити flask_app на назаву папки з файлом setting.py, app замінити на назву змінної для створення усіх веб-додатків. Зберегти зміни```
     
13. У розділі **Virtualenv** вказати назву віртуального середовища.
14. Оновити сайт, натиснувши кнопку **Reload**.
15. Перейти за посиланням веб-додатку.
16. У випадку помилок запуску веб-застосунку, перейти у розділ **Log files**, у пункті **Error log** перейти за посиланням; виправити вказані помилки, оновити сайт.

> Perform a local run.
> In a browser, open the pythonanywhere website, create a beginner account (register).
> Verify your email address.
> Go to the Web tab, create a new web application.
> In the modal window that opens, in the Select a Python Web framework section, select Flask and Python 3.10.
> Go to the **Console** > **Bash** tab.
> Create a virtual environment by issuing the following command in the console:
 - mkvirtualenv (name of the virtual environment) -- python = python 3.10
> Install all the necessary modules used in the project:
  - pip install flask, flask_sqlalchemy, flask_migrate, flask_login, flask_mail, pandas, openpyxl, sqlite3, pyTelegramBotAPI
> Download the project files: write commands in the bush console:
 - pwd - find out the current directory
 - cd mysite - go to the mysite folder
 - git clone (link to the git repository)
 - Go to the Web tab, scroll down to the Code section:
> In the **Source code** and **Working directory** sections, at the end of the path add: **/mysite/(project folder name)**.
> Go to the link in the **WSGI configuration file** link
> In the 16th line, replace flask_app with the name of the folder with the setting.py file, and replace app with the name of the variable for creating all web applications. Save changes
> In the Virtualenv section, specify the name of the virtual environment.
> Refresh the site by clicking the Reload button.
> Follow the link of the web application.
> In case of errors in launching the web application, go to the Log files section, in the Error log item, click the link; correct the errors, refresh the site.

### Структура проекту 

- `shop`: **головний додаток**, у якому зберігається база даних з інформацією користувача. У файл urls.py підключають усі частини проекту - Blueprint-и, проводять міграції. У папці templates є головний html-шаблон - base.html 
- `registration_page`: логіка сторінки реєстрації, папка містить модель **User**, що зберагіє дані зареєстрованих користувачів, взятих з форми реєстрації у папці template.
- `authorization_page`: логіка сторінки авторизації, у папці template є шоблон з формою авторизації (логін та пароль). 
- `home_page`:  основна сторінка користувача, яка з'являється після реєстрації, містить посилання на усі інші сторінки веб-сайту.
- `shop_page`: сторінка з асортиментом товару, є модель **Product**, що зберігає усі товари на сторінці. Інформація про продукт зберігається в **excel-файлі** Product.xlsx.
- `cart`: сторінка корзини, у якій зберігаються усі бажані товари для оформлення замовлення. У файлі cart.html є форма для заповнення інформації про замовлення, дані зберігаються у моделі **Order**. Сторінка cart_2.html відображається лише після оформлення замовлення. Файл views.py відповідає за відправку листа на пошту, що оповіщає про оформлення нового замволення.
- `admin_page`: сторінка, що доступна лише користувачам, які мають у таблиці User **is_admin = 1**. Файл admin.html містить 4 форми, за допомогою них, на сторінці можна змінювати опис товару (картинку, ціну, ім'я, знижку продукту), додавати новий асортимент товару та видаляти продукт з бази даних.
- `contacts_page`: сторінка, що відповідає за контакти, де ви можете зв'язатись із розробником сайту.

### Створення головного додатку: Flask

1. Створити змінну з назвою вашого головного додатку, що приймає у собі клас Flask з модуля flask  
2. Вказати необхідні параметри, такі як:
   - `import_name`: вказати назву файлу, у якому створюється головний додаток
   - `template_folder`: вказати шлях до папки templates
   -  `instance_path`: вказати шлях, де буде зберігатись база даних
   -  `static_url_path`: вказати назву, за якою можна знайти сторінку на веб-сайті
3. Імпортувати створенну змінну до файлу __init__.py
   
Приклад коду:
```python
# Імортуємо потрібні модулі для створення бази даних та міграцій, головного додатку
import flask, flask_sqlalchemy, flask_migrate, os

shop = flask.Flask(
    import_name= "settings", # назва файлу, у якому знаходиться змінна 
    template_folder= "shop/templates", # шлях до папки templates
    instance_path= os.path.abspath(__file__ + "/.."), # шлях, де буде зберігатись база даних
    static_url_path= '/shop/' # назва, за якою можна знайти сторінку на веб-сайті
)
```

 ### Створення додатку сторінки: Blueprint

1. Імпортувати модуль **flask** для подальшої роботи
2. Створити змінну з назвою вашої сторінки
3. У змінну записати класс Blueprint з модулю flask. У классі потрібно задати ряд параметрів, таких як:
   - `name`: назва додатку сторінки 
   - `import_name`: назва пакету в якому створюєтся blueprint
   - `template_folder`: шлях до папки templates
   - `static_folder`: шлях до папки static
   - `static_url_path`: посилання за яким можна знайти сторінку на веб-сайті
4. Імпортувати створенну змінну до файлу _ _init_ _.py
     
Приклад коду:

```python
# Імпортуємо для подальшої роботи модуль flask
import flask

shop_page = flask.Blueprint(
    name = 'shop_page', # назва додатку сторінки 
    import_name= 'shop_page', # назва пакету, у якому створюється змінна (аби в наступних параметрах скоротити шлях)
    template_folder= 'templates', # папка з шаблоном сторінки (абсолютний шлях не варто вказувати через назву пакету)
    static_folder= 'static', # папка зі стилями сторінки
    static_url_path= '/shop_page/' # посилання за яким можна знайти сторінку на веб-сайті
)
```

### Спосіб налаштування Blueprint

1. До файлу urls.py імпортувати змінну з Blueprint-додатком та функцію відображення сторінки 
2. До імпортованої змінної додаємо функцію **add_url_rule**, що відповідає за маршрут до сторінки, з такими параметрами, як:
   - `rule`: шаблон URL, який буде оброблятися
   - `view_func`: функція обробки, яка буде викликана, коли запит буде надіслано за вказаним URL
   - `methods`: функція, що була записана у параметр **view_func**, буде викликана для методів, що вказані у цьому параметрі
3. Звернутись до змінної головного додатку та зареєструвати blueprint, за допомогою функції **register_blueprint**. У параметрах передати потрібний blueprint-додаток

Приклад коду:
```python
# З пакету потрібного Blueprint-додатку імпортуємо змінну та функцію відображення html-сторінки
from shop_page import shop_page, shop_render

# Імпортувати головний додаток
from .settings import shop

# До змінної головного додатку додаємо функцію add_url_rule, що відповідає за маршрут до сторінки (посилання)
shop_page.add_url_rule(
    rule='/shop_page/', # шаблон URL, який буде оброблятися
    view_func= shop_render, # функція відображення html-сторінки, яка буде викликана, коли запит буде надіслано за вказаним URL
    methods = ['GET', 'POST'] # функція, що була вказана у параметрі view_func буде викликатись за вказаними методами
)

# Реєструємо blueprint, за допомогою функції register_blueprint. У параметрах передати потрібний blueprint-додаток
shop.register_blueprint(blueprint= shop_page)
```

### Опис файлів setting, mail_config і login_manager

#### Settings.py

+ Файл **settings.py** налаштовує та ініціалізує веб-додаток за допомогою класу Flask, а також створює базу даних та проводить міграції.

1. Імпортуємо необхідні модулі: **flask**, **flask-SQLAlchemy** для роботи з базою даних, **flask-migrate** для керування міграціями та **os** для роботи з файловою системою.
2. Створюємо змінну головноо додатку. Та налаштовуємо її за інструкцією, вказаною у пункті **Створення головного додатку: Flask**.
3. Налаштовуємо підключення до бази данних **data.db** за допомогою модуля **flask_sqlalchemy**. 
4. Створюємо базу даних, яка буде прив'язана до головного додатку.
5. Створюємо міграції.

Приклад коду:
```python
# Імортуємо потрібні модулі для створення бази даних та міграцій, головного додатку
import flask, flask_sqlalchemy, flask_migrate, os

shop = flask.Flask(
    import_name= "settings", # назва файлу, у якому знаходиться змінна 
    template_folder= "shop/templates", # шлях до папки templates
    instance_path= os.path.abspath(__file__ + "/.."), # шлях, де буде зберігатись база даних
    static_url_path= '/shop/' # назва, за якою можна знайти сторінку на веб-сайті
)

# Налаштовуємо підключення до бази данних. Так як база даних є локальною у значення вказуємо лише назву бази
shop.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

# Створюємо базу даних та міграції, які будуть прив'язані до головного додатку.
db = flask_sqlalchemy.SQLAlchemy(app= shop)

# Міграції - успішний запис змін у базу даних (створення таблиць, їх редагування)
migrate = flask_migrate.Migrate(app= shop, db= db)
```

#### Mail_config.py

+ Файл **main_config** налаштовує автоматичну відправку листа до електронної пошти у веб-додатку, використовуючи flask-mail.

1. Імпортуємо головний додаток з файлу **settings.ру** та модуль **flask-mail** для роботи з ел.поштою
2. Створюємо змінну зі значенням пошти людини від якої буде відсилатись лист.
3. Налаштовуємо відправку листа: 
   - `['MAIL_SERVER']`: налаштування відправки ел. поштою з використанням модулю flask_mail через SMTP сервер gmail
   - `['MAIL_PORT']`: налаштовуємо порт для підключення до SMTP сервера.
   - `['MAIL_USE_TLS']`: надаємо можливість користуватись TLS.
   - `['MAIL_USERNAME']`: записуємо створенну змінну (відправник).
   - `['MAIL_PASSWORD']`: задаємо гугл пароль додатку.
4. Надсилаємо автоматичний лист за допомгою класу **Mail**. У параметраї вказуємо назву головного веб-застосунку, аби лист надсилався при запуску цього проекту

> [!IMPORTANT]
> **SMTP-сервер** використовується для отримання та надсилання листів на вказану адресу одержувача, використовуючи порт 25, 465 aбо 587.
> **TLS** — це протокол, який забезпечує безпеку зв'язку через комп'ютерну мережу.

Приклад коду:
```python
# Імпортуємо головний додаток 
from .settings import shop

# Імпортуємо модуль flask_mail для налаштування відправки листа на ел. пошту
import flask_mail

# У змінну address записуємо ел.пошту людини, від якої будуть надходити листи
address = 'vserhiienko212@gmail.com'

shop.config['MAIL_SERVER'] = 'smtp.gmail.com' # сервер, який здійснює надсилання ел. пошти через протокол SMTP
shop.config['MAIL_PORT'] = 587 # порт для підключення SMTP-серверу. У цьому випадку це 587

shop.config['MAIL_USE_TLS'] = True # сервер ел. пошти буде використовувати TLS для шифрування з'єднань.
shop.config['MAIL_USERNAME'] = address # вказуємо змінну зі збереженою поштою відправника
shop.config['MAIL_PASSWORD'] = 'wqwf xzgz eqrb ceyt' # задаємо пароль для облікового запису ел. пошти, який ваш додаток буде використовувати для відправки ел. листів через сервер ел. пошти.

mail = flask_mail.Mail(app=shop) # Надсилаємо автоматичний лист за допомгою класу **Mail**. У параметраї вказуємо назву головного веб-застосунку, аби лист надсилався при запуску цього проекту.
```

####  Login_manager.py

+ Файл **login_manager** використовується для налаштування системи авторизації користувачів у головному-додатку за допомогою пакету flask_login.

1. Імпортувати необхідний модуль **flask_login** для управління сеансами користувачів. Імпортувати головний додаток з файлу **settings.ру**, а також модель з усіма зареєстрованими користувачами, для взаємодії з таблицею користувачів у базі даних.
2. Задаємо секретний ключ. Він використовується для шифрування даних сеансів (безпечне з'єднання)
3. Створює об'єкт LoginManager і зв'язуємо його з головним додатком. LoginManager керує станом входу користувачів у додатку.
4.  Вказує Flask-Login, яку сторінку показувати, коли неавторизований користувач намагається отримати доступ до захищеної сторінки.
5.  Вказуємо декоратор, який реєструє функцію завантаження користувача. Функція повертає ID користувача, збереженого у сеансі.

Приклад коду:
```python
import flask_login # управління сеансами користувачів
from registration_page.models import User # взаємодія з таблицею зареєстрованих користувачів User у базі даних.
from .settings import shop # імпортуємо головний додаток

shop.secret_key = 'Задайте секретний ключ' # встановлюємо секретний ключ для головного-додатку. 
login_manager = flask_login.LoginManager(shop) # створюємо змінну від класу LoginManager, що керує станом входу користувачів у додатку.

login_manager.login_view = 'show_login' # вказуємо функцію відображення сторінки авторизації

@login_manager.user_loader # декоратор, який реєструє функцію завантаження користувача

def load_user(id): # створюємо функцію, яка приймає параметр id, для отримання id користувача
    return User.query.get(id) # виконуємо запит до бази даних для отримання id користувача. Якщо користувач існує, він повертається, інакше повертається None.
```






  
