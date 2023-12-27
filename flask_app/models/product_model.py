from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user_model
from flask import flash


class Product:
    DB = "amazon_users"

    def __init__(self,data):
        self.id = data["id"]
        self.product_name = data["product_name"]
        self.asin= data["asin"]
        self.quantity = data["quantity"]
        self.buy_cost = data["buy_cost"]
        self.selling_price = data["selling_price"]
        self.user_id = data["user_id"]
        # self.remaining_qty = data["remaining_qty"]
        # self.starting_qty - data['starting_qty']
        self.created_by=None


    @classmethod
    def save_product(cls,data):
        query = """INSERT INTO products (product_name, asin, quantity, buy_cost, selling_price,
        created_at, updated_at,user_id) VALUES (%(product_name)s, %(asin)s, %(quantity)s, %(buy_cost)s,%(selling_price)s,
        NOW(), NOW(), %(user_id)s)"""
        return connectToMySQL(cls.DB).query_db(query,data)


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM products JOIN users ON users.id = products.user_id;"
        product_data = connectToMySQL(cls.DB).query_db(query)
        print("product data:", product_data)
        products = []

        for row in product_data:
            this_product = cls(row)
            user_dict = {
            "id":row["users.id"],
            "first_name": row["first_name"],
            "last_name":row["last_name"],
            "email":row["email"],
            "password":row["password"],
            "created_at": row["users.created_at"],
            "updated_at":row["users.updated_at"]

            }
            creator = user_model.User(user_dict)

            this_product.created_by = creator
            products.append(this_product)
        
        print('products',products)
        return products



    @classmethod
    def product_get_by_id(cls,product_id):
        query = """SELECT * FROM products LEFT  JOIN users
        ON products.user_id = users.id
        WHERE products.id = %(id)s;"""
        data={
            "id": product_id
        }

        results = connectToMySQL(cls.DB).query_db(query,data)
        print(results[0])
        one_product = cls(results[0])
        row = results[0]
        one_product_creators_info= {
            "id": row['users.id'], 
            "first_name": row['first_name'],
            "last_name": row['last_name'],
            "email": row['email'],
            "password": row['password'],
            "created_at": row['users.created_at'],
            "updated_at": row['users.updated_at']
        }
        creator = user_model.User(one_product_creators_info)
        one_product.created_by = creator

        return one_product


    @classmethod
    def create(cls, create_product):

        query = """INSERT INTO products (product_name, asin, quantity, buy_cost, selling_price) 
                Values (%(product_name)s, %(asin)s, %(quantity)s, %(buy_cost)s, %(selling_price)s);"""

        results = connectToMySQL(cls.DB).query_db(query,create_product)
        return results



    @classmethod
    def update(cls,data):
        query = """UPDATE products SET product_name = %(product_name)s, asin = %(asin)s, quantity =
            %(quantity)s, buy_cost = %(buy_cost)s, selling_price= %(selling_price)s 
            WHERE id= %(id)s"""

        result = connectToMySQL(cls.DB).query_db(query,data)
        return result



    @classmethod
    def delete(cls,data):
        query = "DELETE FROM products WHERE id = %(id)s;"

        return connectToMySQL(cls.DB).query_db(query,data)


    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM products WHERE products.id= %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query,data)
        return cls(results[0])

    @staticmethod
    def validate_product(product):
        is_valid = True
        query = "SELECT * FROM products WHERE product_name = %(product_name)s;"
        results = connectToMySQL(Product.DB).query_db(query,product)
        if len(product["product_name"]) < 3:
            flash("Product Name Can Not be less than 3 Characters!")
        if len(product["product_name"])==0:
            flash("Product Name can not be blank")
            is_valid= False
        if len(product["asin"]) < 3:
            flash("ASIN Must Be More Than 3 Characters")
        if len(product["asin"])== 0:
            flash("ASIN Can Not be blank")
            is_valid= False
        if len(product["quantity"]) == 0:
            flash("Select Valid Quantity")
            is_valid= False
        if len(product["buy_cost"]) == 0:
            flash("Select Valid Buy Cost")
            is_valid= False
        if len(product["selling_price"]) == 0:
            flash("Select Valid Selling Price")
            is_valid= False
        return is_valid