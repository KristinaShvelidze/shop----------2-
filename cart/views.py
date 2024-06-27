import flask, flask_mail
from flask_login import current_user
from shop_page.models import Product
from .models import Order
from shop.settings import db
from shop.mail_config import mail

def cart_render():
    is_admin = False
    products_cookie = flask.request.cookies.get('products')
    
    if products_cookie:
        products = products_cookie.split(' ')
        list_products = []
        repeate_id = []

        for id_product in products:
            count_products = products.count(id_product)
            if id_product not in repeate_id:
                product = Product.query.get(id_product)
                if product:
                    product.count = count_products
                    list_products.append(product)
                    repeate_id.append(id_product)
    else:
        print("No products found in cookies.")
        return flask.render_template('cart.html', name=current_user.name)

    if flask.request.method == 'POST':
        print('POST')
        if flask.request.form.get('send-order'):
            print('send-order')
            
            order = Order(
                name=flask.request.form['name'],
                last_name=flask.request.form['last-name'],
                phone=flask.request.form['phone'],
                email=flask.request.form['email'],
                city=flask.request.form['city'],
                post_office=flask.request.form['post-office'],
                preferences=flask.request.form['preferences'],
                id_product=str(list_products)
            )

            db.session.add(order)
            db.session.commit()

            message_text = f'Order № {order.id}: \n\n'
            message_text += f'First name: {order.name}\n'
            message_text += f'Last name: {order.last_name}\n'
            message_text += f'Phone number: {order.phone}\n'
            message_text += f'Email: {order.email}\n'
            message_text += f'City: {order.city}\n'
            message_text += f'Post office: {order.post_office}\n'
            message_text += f'Preferences: {order.preferences}\n'

            for product in list_products:
                message_text += f'Products: {product.name}\n'

            message = flask_mail.Message(
                subject=f'Order № {order.id}',
                sender='vserhiienko212@gmail.com',
                recipients=[f'{order.email}'],
                body=message_text
            )
            mail.send(message)

            return flask.render_template(
                template_name_or_list='cart_2.html',
                is_admin=current_user.is_admin,
                name=current_user.name,
                products=list_products,
                is_authenticated=current_user.is_authenticated
            )

        elif flask.request.form.get('cancel-order'):

            cancelled_message_text = f'Order was cancelled'

            cancelled_message = flask_mail.Message(
                subject=f'Order',
                sender='vserhiienko212@gmail.com',
                recipients=[current_user.email],
                body=cancelled_message_text
            )
            mail.send(cancelled_message)
            print('order was cancelled')

            return flask.render_template(
                template_name_or_list='cart.html',
                is_admin=current_user.is_admin,
                name=current_user.name,
                products=list_products,
                is_authenticated=current_user.is_authenticated
            )

    print('no_post')


    if current_user.is_authenticated:
        return flask.render_template(
            template_name_or_list = 'cart.html',
            products= list_products,
            is_authenticated = current_user.is_authenticated,
            name = current_user.name,
            is_admin = current_user.is_admin
    )
        
        # print('no auth')
    return flask.render_template(
        template_name_or_list = 'cart.html',
        is_admin = current_user.is_admin
    )
        
    
