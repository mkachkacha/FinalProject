from flask import Flask
from extensions import db
from models import User, Category, Product, CartItem, Order, OrderItem

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
db.init_app(app)

def recreate_database():
    with app.app_context():

        db.drop_all()
        print("Dropped all tables.")
        

        db.create_all()
        print("Created all tables.")
        

        admin = User(
            username='admin',
            email='admin@tbcshop.com',
            password_hash='admin123',
            is_admin=True
        )
        db.session.add(admin)
        db.session.commit()
        print("Created admin account:")
        print("Email: admin@tbcshop.com")
        print("Password: admin123")

if __name__ == '__main__':
    recreate_database()
