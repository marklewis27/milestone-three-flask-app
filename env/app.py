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
    gearboxes=mongo.db.gearboxes.find(),
    engines=mongo.db.engines.find(),
    fuels=mongo.db.fuels.find(),
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
    all_gearboxes = mongo.db.gearboxes.find()
    all_engines = mongo.db.engines.find()
    all_fuels = mongo.db.fuels.find()
    return render_template("update.html",car=the_car,
                            gearboxes=all_gearboxes,
                            engines=all_engines,
                            fuels=all_fuels,
                            categories=all_categories)

@app.route('/changes/<car_id>', methods=["POST"])
def changes(car_id):
    cars = mongo.db.cars
    cars.update( {'_id': ObjectId(car_id)},
    {
        'category_name':request.form.get('category_name'),
        'car_make':request.form.get('car_make'),
        'car_model':request.form.get('car_model'),
        'fuel_type':request.form.get('fuel_type'),
        'engine_size':request.form.get('engine_size'),
        'gearbox_type':request.form.get('gearbox_type'),
        'car_mileage':request.form.get('car_mileage'),
        'car_colour':request.form.get('car_colour')
    })
    return redirect(url_for("home"))


@app.route('/delete/<car_id>')
def delete(car_id):
    mongo.db.cars.remove( {'_id': ObjectId(car_id)})
    return redirect(url_for("home"))