from flask import Flask
from extensions import db
from models import Category

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
db.init_app(app)

def add_categories():
    categories = [
        "Fruits & Vegetables",
        "Dairy & Eggs",
        "Meat & Fish",
        "Bakery",
        "Beverages",
        "Snacks",
        "Pantry",
        "Household"
    ]

    with app.app_context():

        existing_categories = Category.query.all()
        if existing_categories:
            print("Categories already exist!")
            return


        for category_name in categories:
            category = Category(name=category_name)
            db.session.add(category)
        
        db.session.commit()
        print("Added the following categories:")
        for category_name in categories:
            print(f"- {category_name}")

if __name__ == '__main__':
    add_categories()
