from importlib.machinery import SourceFileLoader
from importlib.util import module_from_spec, spec_from_loader
from pathlib import Path

from flask import Flask, redirect, render_template, request, session, url_for


cart_module_path = Path(__file__).with_name("E CART.PY")
cart_loader = SourceFileLoader("shopping_cart", str(cart_module_path))
cart_spec = spec_from_loader("shopping_cart", cart_loader)
shopping_cart_module = module_from_spec(cart_spec)
cart_loader.exec_module(shopping_cart_module)
ShoppingCart = shopping_cart_module.ShoppingCart

app = Flask(__name__)
app.config["SECRET_KEY"] = "replace-this-with-a-random-secret-key"

PRODUCTS = [
    {"name": "Canvas Weekender", "price": 68.00, "category": "Travel", "tag": "BESTSELLER", "color": "sand"},
    {"name": "Everyday Hoodie", "price": 54.00, "category": "Apparel", "tag": "NEW", "color": "blue"},
    {"name": "Studio Mug", "price": 22.00, "category": "Home", "tag": "POPULAR", "color": "clay"},
    {"name": "Field Notes Set", "price": 16.00, "category": "Stationery", "tag": "ESSENTIAL", "color": "green"},
]


def get_cart():
    cart = ShoppingCart()
    cart.items = session.get("cart", [])
    return cart


def save_cart(cart):
    session["cart"] = cart.items
    session.modified = True


@app.route("/", methods=["GET"])
def index():
    cart = get_cart()
    code = session.get("coupon", "")
    totals = cart.checkout(code)
    return render_template("index.html", products=PRODUCTS, items=cart.items, totals=totals, coupon=code, message=session.pop("message", None))


@app.post("/add")
def add_item():
    product_index = request.form.get("product", type=int)
    quantity = request.form.get("quantity", type=int) or 1
    if product_index is None or not 0 <= product_index < len(PRODUCTS) or quantity < 1:
        session["message"] = ("error", "Choose a valid product and quantity.")
        return redirect(url_for("index"))

    product = PRODUCTS[product_index]
    cart = get_cart()
    cart.additem(product["name"], product["price"], quantity)
    save_cart(cart)
    session["message"] = ("success", f"{product['name']} added to your bag.")
    return redirect(url_for("index"))


@app.post("/update")
def update_item():
    name = request.form.get("name", "")
    quantity = request.form.get("quantity", type=int)
    cart = get_cart()
    for item in cart.items:
        if item["name"] == name:
            if quantity and quantity > 0:
                item["quantity"] = quantity
            else:
                cart.items.remove(item)
            break
    save_cart(cart)
    return redirect(url_for("index"))


@app.post("/coupon")
def apply_coupon():
    code = request.form.get("code", "").strip()
    if code and code != "2005":
        session["message"] = ("error", "That code is not active. Try 2005 for 10% off.")
    else:
        session["coupon"] = code
        session["message"] = ("success", "10% discount applied.") if code else ("success", "Coupon removed.")
    return redirect(url_for("index"))


@app.post("/clear")
def clear_cart():
    session.pop("cart", None)
    session.pop("coupon", None)
    session["message"] = ("success", "Your bag is empty now.")
    return redirect(url_for("index"))


@app.post("/checkout")
def checkout():
    cart = get_cart()
    if not cart.items:
        session["message"] = ("error", "Add something to your bag before checking out.")
    else:
        session["message"] = ("success", "Order received. Thanks for shopping with Field & Form.")
        session.pop("cart", None)
        session.pop("coupon", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
