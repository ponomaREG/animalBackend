from app import app
from flask import render_template, jsonify, request
from app.models.animals import Animal

@app.route("/", methods = ["GET"])
def main():
    return render_template("docs.html")


@app.route("/animal", methods = ["GET"])
def getAnimals():
    return jsonify(Animal.getAllAnimals())

@app.route("/animal/add", methods = ["POST"])
def addAnimals():
    args = request.form
    animalId = Animal.insertAnimal(args["name"], args["description"],request.files["image"], args["latitude"], args["longitude"])
    return jsonify({"newAnimalId" : animalId})