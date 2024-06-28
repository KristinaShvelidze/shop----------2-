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


