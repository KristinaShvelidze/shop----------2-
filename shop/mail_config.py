from .settings import shop
import flask_mail

address = 'vserhiienko212@gmail.com'

shop.config['MAIL_SERVER'] = 'smtp.gmail.com'
shop.config['MAIL_PORT'] = 587
shop.config['MAIL_USE_TLS'] = True
shop.config['MAIL_USERNAME'] = address
shop.config['MAIL_PASSWORD'] = 'wqwf xzgz eqrb ceyt'

mail = flask_mail.Mail(app=shop)
