from flask import Flask, redirect, request, url_for
from datetime import datetime
from flask import render_template
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

import re

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = 'mongodb+srv://Mark:Markpassword@cluster0-x6esz.mongodb.net/task_manager?retryWrites=true&w=majority'

mongo= PyMongo(app)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",
                          cars=mongo.db.cars.find())


@app.route("/new/")
def new():
    return render_template("new.html",
    categories=mongo.db.categories.find())

@app.route('/insert_car', methods=['POST'])
def insert_car():
    cars = mongo.db.cars
    cars.insert_one(request.form.to_dict())
    return redirect(url_for("home"))

@app.route('/update/<car_id>')
def update(car_id):
    the_car = mongo.db.cars.find_one({"_id": ObjectId(car_id)})
    all_categories = mongo.db.categories.find()
    return render_template("update.html",car=the_car,
                            categories=all_categories)

@app.route("/delete/")
def delete():
    return render_template("delete.html")