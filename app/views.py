from app import app
from flask import render_template, jsonify
from app.models.animals import Animal

@app.route("/", methods = ["GET"])
def main():
    return render_template("docs.html")


@app.route("/animal", methods = ["GET"])
def getAnimals():
    return jsonify(Animal.getAllAnimals())