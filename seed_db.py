from app import app
from extensions import db
from models import Category, Product, User
from werkzeug.security import generate_password_hash

def seed_database():

    admin = User(
        username='admin',
        email='admin@example.com',
        password_hash=generate_password_hash('admin123'),
        is_admin=True
    )
    db.session.add(admin)


    categories = {
        'Fruits': [
            {
                'name': 'Red Apple',
                'description': 'Fresh, crisp red apples. Rich in fiber and vitamin C.',
                'price': 0.50,
                'image_url': '/static/img/products/apple.jpg',
                'stock': 100
            },
            {
                'name': 'Banana',
                'description': 'Ripe yellow bananas. Excellent source of potassium.',
                'price': 0.30,
                'image_url': '/static/img/products/banana.jpg',
                'stock': 150
            }
        ],
        'Vegetables': [
            {
                'name': 'Carrot',
                'description': 'Fresh carrots. Rich in beta carotene and fiber.',
                'price': 0.40,
                'image_url': '/static/img/products/carrot.jpg',
                'stock': 200
            },
            {
                'name': 'Broccoli',
                'description': 'Fresh broccoli crowns. High in vitamin C and K.',
                'price': 1.99,
                'image_url': '/static/img/products/broccoli.jpg',
                'stock': 75
            }
        ],
        'Dairy': [
            {
                'name': 'Milk',
                'description': 'Fresh whole milk. Rich in calcium and protein.',
                'price': 3.99,
                'image_url': '/static/img/products/milk.jpg',
                'stock': 50
            },
            {
                'name': 'Cheese',
                'description': 'Cheddar cheese. Aged for perfect flavor.',
                'price': 4.99,
                'image_url': '/static/img/products/cheese.jpg',
                'stock': 40
            }
        ],
        'Bakery': [
            {
                'name': 'Bread',
                'description': 'Fresh baked whole wheat bread.',
                'price': 2.99,
                'image_url': '/static/img/products/bread.jpg',
                'stock': 30
            },
            {
                'name': 'Croissant',
                'description': 'Buttery, flaky croissants.',
                'price': 1.99,
                'image_url': '/static/img/products/croissant.jpg',
                'stock': 25
            }
        ]
    }

    for category_name, products in categories.items():
        category = Category(name=category_name)
        db.session.add(category)
        db.session.flush()  # This ensures the category has an ID

        for product_data in products:
            product = Product(
                name=product_data['name'],
                description=product_data['description'],
                price=product_data['price'],
                image_url=product_data['image_url'],
                stock=product_data['stock'],
                category_id=category.id
            )
            db.session.add(product)

    db.session.commit()

if __name__ == '__main__':
    with app.app_context():

        db.create_all()

        seed_database()
        print("Database seeded successfully!")
