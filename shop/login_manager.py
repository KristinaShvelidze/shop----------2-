import flask_login # управління сеансами користувачів
from registration_page.models import User # взаємодія з таблицею зареєстрованих користувачів User у базі даних.
from .settings import shop # імпортуємо головний додаток

shop.secret_key = 'Задайте секретний ключ' # встановлюємо секретний ключ для головного-додатку. 
login_manager = flask_login.LoginManager(shop) # створюємо змінну від класу LoginManager, що керує станом входу користувачів у додатку.

login_manager.login_view = 'show_login' # вказуємо функцію відображення сторінки авторизації

@login_manager.user_loader # декоратор, який реєструє функцію завантаження користувача

def load_user(id): # створюємо функцію, яка приймає параметр id, для отримання id користувача
    return User.query.get(id) # виконуємо запит до бази даних для отримання id користувача. Якщо користувач існує, він повертається, інакше повертається None.

