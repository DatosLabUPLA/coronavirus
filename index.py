from flask import Flask, render_template
import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd

app = Flask(__name__)

# Creating simple Routes 
@app.route('/test')
def test():
    return "Home Page"

@app.route('/test/about/')
def about_test():
    return "About Page"

# Routes to Render Something
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about', strict_slashes=False)
def about():
    return render_template("about.html")


@app.route('/casos')
def casos():
    return map_1._repr_html_()


# Make sure this we are executing this file
if __name__ == '__main__':
    app.run(debug=True)
