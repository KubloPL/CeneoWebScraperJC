from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html.jinja")

@app.route('/extract')
def extract():
    return render_template("extract.html.jinja")

@app.route('/products')
def products():
    return render_template("products.htm.jinja")

@app.route('/author')
def author():
    return render_template("author.htm.jinja")

@app.route('/product/<product_id>')
def product():
    return render_template("product.htm.jinja", product_id=product_id)

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=""):
    return f"Hello, {name}!"