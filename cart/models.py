from shop.settings import db

class Order(db.Model):  

    id = db.Column(db.Integer, primary_key = True)

    name = db.Column(db.String(60), nullable = False)
    last_name =  db.Column(db.String(60), nullable = False)
    phone =  db.Column(db.Integer, nullable = False)
    email = db.Column(db.String(60), nullable = False)
    city = db.Column(db.String(60), nullable = False)
    post_office = db.Column(db.String(60), nullable = False)
    preferences = db.Column(db.String(60), nullable = False)

    id_product = db.Column(db.String(60), nullable = False)
    
    def __repr__(self):
        return f'id: {self.id}'

    
    


