
from flask import Flask, render_template

app = Flask(__name__)


# Homepage — keep your existing homepage
@app.route("/")
def home():
    return render_template("index.html")


# Services page
@app.route("/services")
def services():
    return render_template("page.html", page="services")


# Products page
@app.route("/products")
def products():
    return render_template("page.html", page="products")


# About page
@app.route("/about")
def about():
    return render_template("page.html", page="about")


# Contact page
@app.route("/contact")
def contact():
    return render_template("page.html", page="contact")


# Booking page
@app.route("/booking")
def booking():
    return render_template("page.html", page="booking")


if __name__ == "__main__":
    app.run(debug=True)
