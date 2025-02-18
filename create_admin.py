from flask import Flask
from extensions import db
from models import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
db.init_app(app)

def create_admin():
    with app.app_context():
        admin = User.query.filter_by(email='admin@tbcshop.com').first()
        if admin:
            print("Admin account exists, updating password...")
            admin.set_password('admin123')
            db.session.commit()
            print("Admin password updated successfully!")
            print("Email: admin@tbcshop.com")
            print("Password: admin123")
            return

        admin = User(
            username='admin',
            email='admin@tbcshop.com',
            is_admin=True
        )
        admin.set_password('admin123')
        
        db.session.add(admin)
        db.session.commit()
        print("Admin account created successfully!")
        print("Email: admin@tbcshop.com")
        print("Password: admin123")

if __name__ == '__main__':
    create_admin()
