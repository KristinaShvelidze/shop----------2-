from .settings import shop
from home_page import home, home_render
from registration_page import registration, reg_render
from authorization_page import login, show_login

from cart import cart, cart_render
from admin_page import admin, admin_render
from contacts_page import contacts, contacts_render


home.add_url_rule(rule= "/", view_func= home_render, methods = ['GET', 'POST'])
registration.add_url_rule(rule= '/registration_page/', view_func= reg_render, methods = ['GET', 'POST'])
login.add_url_rule(rule= '/authorization_page/', view_func= show_login, methods = ['GET', 'POST'])
cart.add_url_rule(rule= '/cart/', view_func= cart_render, methods = ['GET', 'POST'])
admin.add_url_rule(rule= '/admin/', view_func= admin_render, methods = ['GET', 'POST'])
contacts.add_url_rule(rule= '/contacts/', view_func= contacts_render, methods = ['GET', 'POST'])



shop.register_blueprint(blueprint= home)
shop.register_blueprint(blueprint= registration)
shop.register_blueprint(blueprint= login)

shop.register_blueprint(blueprint= cart)
shop.register_blueprint(blueprint= admin)
shop.register_blueprint(blueprint= contacts)


# З пакету потрібного Blueprint-додатку імпортуємо змінну та функцію відображення html-сторінки
from shop_page import shop_page, shop_render

# До імпортованої змінної додаємо функцію add_url_rule, що відповідає за маршрут до сторінки (посилання)
shop_page.add_url_rule(
    rule='/shop_page/', # шаблон URL, який буде оброблятися
    view_func= shop_render, # функція відображення html-сторінки, яка буде викликана, коли запит буде надіслано за вказаним URL
    methods = ['GET', 'POST'] # функція, що була вказана у параметрі view_func буде викликатись за вказаними методами
)

# Реєструємо blueprint, за допомогою функції register_blueprint. У параметрах передати потрібний blueprint-додаток
shop.register_blueprint(blueprint= shop_page)