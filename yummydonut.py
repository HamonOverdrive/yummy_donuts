from flask import Flask, render_template, flash, request, url_for, redirect
from flask_googlemaps import GoogleMaps


app = Flask(__name__)

# you can set key as config
app.config['GOOGLEMAPS_KEY'] = "AIzaSyAwLj0nhvO76-6-dBrpGAddGEKwE5MQKds"

# Initialize the extension
GoogleMaps(app)


@app.route('/')
def homepage():
    return render_template("main.html")

@app.route('/menu/')
def menupage():
    return render_template("menu.html")

@app.route('/location/')
def locationpage():
    return render_template("location.html")

@app.route('/aboutus/')
def aboutuspage():
    return render_template("aboutus.html")

@app.route('/contact/')
def contactpage():
    return render_template("contact.html")



if __name__ == '__main__':
    app.run()
