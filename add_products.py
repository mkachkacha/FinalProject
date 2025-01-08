from flask import Flask
from extensions import db
from models import Category, Product

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
db.init_app(app)

def add_products():
    with app.app_context():

        fruits_veg = Category.query.filter_by(name="Fruits & Vegetables").first()
        dairy = Category.query.filter_by(name="Dairy & Eggs").first()
        meat = Category.query.filter_by(name="Meat & Fish").first()
        bakery = Category.query.filter_by(name="Bakery").first()
        beverages = Category.query.filter_by(name="Beverages").first()
        snacks = Category.query.filter_by(name="Snacks").first()
        pantry = Category.query.filter_by(name="Pantry").first()
        household = Category.query.filter_by(name="Household").first()


        products = [

            {
                "name": "Fresh Apples",
                "description": "Sweet and crispy red apples, price per kg",
                "price": 3.99,
                "stock": 100,
                "category": fruits_veg,
                "image_url": "https://images.unsplash.com/photo-1619546813926-a78fa6372cd2?ixlib=rb-4.0.3&q=85&w=500&auto=format"
            },
            {
                "name": "Organic Bananas",
                "description": "Ripe organic bananas, price per kg",
                "price": 4.99,
                "stock": 150,
                "category": fruits_veg,
                "image_url": "https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?ixlib=rb-4.0.3&q=85&w=500&auto=format"
            },
            {
                "name": "Fresh Tomatoes",
                "description": "Juicy red tomatoes, price per kg",
                "price": 2.99,
                "stock": 80,
                "category": fruits_veg,
                "image_url": "https://images.unsplash.com/photo-1561136594-7f68413baa99?ixlib=rb-4.0.3&q=85&w=500&auto=format"
            },
            {
                "name": "Organic Carrots",
                "description": "Fresh organic carrots, price per kg",
                "price": 1.99,
                "stock": 120,
                "category": fruits_veg,
                "image_url": "https://images.unsplash.com/photo-1598170845058-32b9d6a5da37?ixlib=rb-4.0.3&q=85&w=500&auto=format"
            },
            
            # Dairy & Eggs
            {
                "name": "Organic Milk",
                "description": "Fresh organic whole milk, 1 liter",
                "price": 4.49,
                "stock": 50,
                "category": dairy,
                "image_url": "https://images.unsplash.com/photo-1563636619-e9143da7973b?ixlib=rb-4.0.3&q=85&w=500&auto=format"
            },
            {
                "name": "Free Range Eggs",
                "description": "Farm fresh eggs, dozen",
                "price": 5.99,
                "stock": 40,
                "category": dairy,
                "image_url": "https://images.unsplash.com/photo-1582722872445-44dc5f7e3c8f?ixlib=rb-4.0.3&q=85&w=500&auto=format"
            },
            {
                "name": "Greek Yogurt",
                "description": "Creamy Greek yogurt, 500g",
                "price": 3.99,
                "stock": 60,
                "category": dairy,
                "image_url": "https://images.unsplash.com/photo-1488477181946-6428a0291777?ixlib=rb-4.0.3&q=85&w=500&auto=format"
            },
            {
                "name": "Cheddar Cheese",
                "description": "Aged cheddar cheese, 250g",
                "price": 6.99,
                "stock": 45,
                "category": dairy,
                "image_url": "https://images.unsplash.com/photo-1618164436241-4473940d1f5c?ixlib=rb-4.0.3&q=85&w=500&auto=format"
            },


            {
                "name": "Fresh Chicken",
                "description": "Whole chicken, free-range, price per kg",
                "price": 12.99,
                "stock": 30,
                "category": meat,
                "image_url": "https://images.unsplash.com/photo-1602470520998-f4a52199a3d6?ixlib=rb-4.0.3&q=85&w=500&auto=format"
            },
            {
                "name": "Salmon Fillet",
                "description": "Fresh Atlantic salmon fillet, price per kg",
                "price": 24.99,
                "stock": 25,
                "category": meat,
                "image_url": "https://images.unsplash.com/photo-1599084993091-1cb5c0721cc6?ixlib=rb-4.0.3&q=85&w=500&auto=format"
            },
            {
                "name": "Ground Beef",
                "description": "Lean ground beef, price per kg",
                "price": 15.99,
                "stock": 35,
                "category": meat,
                "image_url": "https://images.unsplash.com/photo-1588168333986-5078d3ae3976?ixlib=rb-4.0.3&q=85&w=500&auto=format"
            },
            {
                "name": "Pork Chops",
                "description": "Premium cut pork chops, price per kg",
                "price": 16.99,
                "stock": 28,
                "category": meat,
                "image_url": "https://images.unsplash.com/photo-1432139509613-5c4255815697?ixlib=rb-4.0.3&q=85&w=500&auto=format"
            },


            {
                "name": "Fresh Bread",
                "description": "Freshly baked sourdough bread",
                "price": 3.99,
                "stock": 40,
                "category": bakery,
                "image_url": "https://images.unsplash.com/photo-1549931319-a545dcf3bc73?ixlib=rb-4.0.3&q=85&w=500&auto=format"
            },
            {
                "name": "Croissants",
                "description": "Buttery croissants, pack of 4",
                "price": 5.99,
                "stock": 30,
                "category": bakery,
                "image_url": "https://images.unsplash.com/photo-1555507036-ab1f4038808a?ixlib=rb-4.0.3&q=85&w=500&auto=format"
            },
            {
                "name": "Chocolate Muffins",
                "description": "Double chocolate muffins, pack of 6",
                "price": 6.99,
                "stock": 25,
                "category": bakery,
                "image_url": "https://images.unsplash.com/photo-1604882406195-d94d4888567d?ixlib=rb-4.0.3&q=85&w=500&auto=format"
            },
            {
                "name": "Bagels",
                "description": "Fresh bagels, pack of 6",
                "price": 4.99,
                "stock": 35,
                "category": bakery,
                "image_url": "https://images.unsplash.com/photo-1585445490387-f47934b73b54?ixlib=rb-4.0.3&q=85&w=500&auto=format"
            },


            {
                "name": "Natural Spring Water",
                "description": "Pure spring water, 1.5L bottle",
                "price": 1.99,
                "stock": 100,
                "category": beverages,
                "image_url": "https://images.unsplash.com/photo-1560023907-5f339617ea30?ixlib=rb-4.0.3&q=85&w=500&auto=format"
            },
            {
                "name": "Orange Juice",
                "description": "Fresh squeezed orange juice, 1L",
                "price": 4.99,
                "stock": 45,
                "category": beverages,
                "image_url": "https://images.unsplash.com/photo-1600271886742-f049cd451bba?ixlib=rb-4.0.3&q=85&w=500&auto=format"
            },
            {
                "name": "Green Tea",
                "description": "Organic green tea, 20 bags",
                "price": 3.99,
                "stock": 60,
                "category": beverages,
                "image_url": "https://images.unsplash.com/photo-1627435601361-ec25f5b1d0e5?ixlib=rb-4.0.3&q=85&w=500&auto=format"
            },
            {
                "name": "Coffee Beans",
                "description": "Premium roasted coffee beans, 250g",
                "price": 8.99,
                "stock": 40,
                "category": beverages,
                "image_url": "https://images.unsplash.com/photo-1559525839-b184a4d698c7?ixlib=rb-4.0.3&q=85&w=500&auto=format"
            },


            {
                "name": "Potato Chips",
                "description": "Classic salted potato chips, 150g",
                "price": 2.99,
                "stock": 75,
                "category": snacks,
                "image_url": "https://images.unsplash.com/photo-1566478989037-eec170784d0b?ixlib=rb-4.0.3&q=85&w=500&auto=format"
            },
            {
                "name": "Mixed Nuts",
                "description": "Premium mixed nuts, 300g",
                "price": 7.99,
                "stock": 50,
                "category": snacks,
                "image_url": "https://images.unsplash.com/photo-1536591375315-1b8c0e19e2d2?ixlib=rb-4.0.3&q=85&w=500&auto=format"
            },
            {
                "name": "Dark Chocolate",
                "description": "70% dark chocolate bar, 100g",
                "price": 3.99,
                "stock": 60,
                "category": snacks,
                "image_url": "https://images.unsplash.com/photo-1587132137056-bfbf0166836e?ixlib=rb-4.0.3&q=85&w=500&auto=format"
            },
            {
                "name": "Popcorn",
                "description": "Microwave popcorn, pack of 3",
                "price": 2.49,
                "stock": 80,
                "category": snacks,
                "image_url": "https://images.unsplash.com/photo-1578849278002-014fa4a2f010?ixlib=rb-4.0.3&q=85&w=500&auto=format"
            },


            {
                "name": "Pasta",
                "description": "Italian spaghetti pasta, 500g",
                "price": 2.49,
                "stock": 90,
                "category": pantry,
                "image_url": "https://images.unsplash.com/photo-1551462147-37885acc36f1?ixlib=rb-4.0.3&q=85&w=500&auto=format"
            },
            {
                "name": "Rice",
                "description": "Premium jasmine rice, 1kg",
                "price": 4.99,
                "stock": 70,
                "category": pantry,
                "image_url": "https://images.unsplash.com/photo-1586201375761-83865001e31c?ixlib=rb-4.0.3&q=85&w=500&auto=format"
            },
            {
                "name": "Olive Oil",
                "description": "Extra virgin olive oil, 500ml",
                "price": 8.99,
                "stock": 40,
                "category": pantry,
                "image_url": "https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?ixlib=rb-4.0.3&q=85&w=500&auto=format"
            },
            {
                "name": "Tomato Sauce",
                "description": "Classic tomato sauce, 500g",
                "price": 2.99,
                "stock": 65,
                "category": pantry,
                "image_url": "https://images.unsplash.com/photo-1472476443507-c7a5948772fc?ixlib=rb-4.0.3&q=85&w=500&auto=format"
            },


            {
                "name": "Paper Towels",
                "description": "Premium paper towels, 6 rolls",
                "price": 5.99,
                "stock": 55,
                "category": household,
                "image_url": "https://images.unsplash.com/photo-1583947581924-860bda3c4083?ixlib=rb-4.0.3&q=85&w=500&auto=format"
            },
            {
                "name": "Dish Soap",
                "description": "Concentrated dish soap, 500ml",
                "price": 3.49,
                "stock": 70,
                "category": household,
                "image_url": "https://images.unsplash.com/photo-1622503441679-67be4e449d6f?ixlib=rb-4.0.3&q=85&w=500&auto=format"
            },
            {
                "name": "Laundry Detergent",
                "description": "Fresh scent laundry detergent, 2L",
                "price": 9.99,
                "stock": 45,
                "category": household,
                "image_url": "https://images.unsplash.com/photo-1610557892470-55d9e80c0bce?ixlib=rb-4.0.3&q=85&w=500&auto=format"
            },
            {
                "name": "Trash Bags",
                "description": "Heavy-duty trash bags, 30 count",
                "price": 6.99,
                "stock": 60,
                "category": household,
                "image_url": "https://images.unsplash.com/photo-1610557892271-4d698d2ed6ee?ixlib=rb-4.0.3&q=85&w=500&auto=format"
            }
        ]


        existing_products = Product.query.all()
        if existing_products:
            print("Products already exist!")
            return


        for product_data in products:
            product = Product(
                name=product_data["name"],
                description=product_data["description"],
                price=product_data["price"],
                stock=product_data["stock"],
                category_id=product_data["category"].id,
                image_url=product_data["image_url"]
            )
            db.session.add(product)
        
        db.session.commit()
        print("Added the following products:")
        for product in products:
            print(f"- {product['name']} (GEL {product['price']}) - {product['category'].name}")

if __name__ == '__main__':
    add_products()
