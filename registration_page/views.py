import flask, os, json
from shop.settings import db
from flask_login import current_user
from .models import User

def reg_render():
    is_registration = False

    if flask.request.method == "POST":
        try:
            user = User(
                name = flask.request.form['name'],
                email = flask.request.form['email'],
                password = flask.request.form['password'],
                password_confirmation = flask.request.form['password_confirmation'],

                is_admin = False
            )

            db.session.add(user)
            db.session.commit()
            is_registration = True
            # return flask.redirect('/authorization_page/')

        except Exception as e:
            print(e)

    path = os.path.abspath(__file__ + '/../static/json/reg.json')
    with open(path, 'r', encoding = 'utf-8') as file:
        data_dict = json.load(file)

    if not current_user.is_authenticated:
        return flask.render_template(template_name_or_list= 'reg.html', is_registration= is_registration, content = data_dict['content'])
    else:
        print('auth')
        return flask.redirect('/authorization_page/')
