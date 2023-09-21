from flask import render_template, session,redirect,request
from flask_app import app
from flask_app.models.product_model import Product
from flask_app.models.user_model import User




@app.route("/dashboard")
def dashboard_new():
    the_products = Product.get_all()
    user_dict = {
        "id": session["user_id"]
    }
    user = User.get_by_id(user_dict)
    
    return render_template("dashboard.html", the_products=the_products, user=user)



@app.route("/dashboard/save")
def new_page():
    
    return render_template("add_inventory.html", this_user_id = session["user_id"])



@app.route("/dashboard/edit/<int:tv_show_id>")
def edit_page(product_id):
    the_product = Product.product_get_by_id(product_id)
    return render_template("edit_product.html",the_product=the_product)



@app.route("/dashboard/save", methods=["POST"])
def add_product():
    if not Product.validate_product(request.form):
        return redirect("/dashboard/save")
    else:
        data = request.form
        Product.save_product(data)
        return redirect("/dashboard")


@app.route("/update/<int:product_id>", methods=["POST"])
def update_product(product_id):
    data = request.form
    if not Product.validate_product(request.form):
        return redirect("/dashboard/save")
    else:
        Product.update(data)
        return redirect("/dashboard")


@app.route('/dashboard/delete/<int:product_id>')
def delete(product_id):
    data={
        "id": product_id
    }
    Product.delete(data)
    return redirect("/dashboard")



@app.route("/dashboard/view_product/<int:product_id>")
def product(product_id):
    user_data = {
        'id': session["user_id"]
    }
    product=Product.product_get_by_id(product_id)
    user= User.get_by_id(user_data)

    return render_template("details.html", product=product, user=user)