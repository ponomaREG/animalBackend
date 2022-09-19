from os import abort
from app import app
from flask import render_template, jsonify, request, abort
from app.models.animals import Animal
from app.models.users import User


@app.route("/", methods = ["GET"])
def main():
    return render_template("docs.html")


@app.route("/animal", methods = ["GET"])
def getAnimals():
    return jsonify(Animal.getAllAnimals())

@app.route("/animal/<animalId>", methods = ["GET"])
def getAnimalInfo(animalId):
    return jsonify(Animal.getAnimaInfo(animalId))


@app.route("/animal/add", methods = ["POST"])
def addAnimals():
    args = request.form
    token = request.headers.get("token")
    if (token is None or not User.checkUserToken(token)):
        return abort(403)
    animalId = Animal.insertAnimal(args["name"], args["description"],request.files.get("image", None), args["latitude"], args["longitude"], token)
    return jsonify({"newAnimalId" : animalId})

@app.route("/auth", methods = ["POST"])
def authenticateUser():
    phone = request.form["phone"]
    login = request.form.get("login")
    otpCode = request.form["otpCode"]
    return jsonify({"token" : User.authenticateUser(phone, otpCode, login)})

@app.route("/auth/phone", methods=["POST"])
def checkIfPhoneExists():
    phone = request.form["phone"]
    isExists = User.checkUserPhone(phone)
    if (isExists):
        return jsonify({"status" : "Exists"})
    else:
        return jsonify({"status" : "Not exists"})


@app.route("/auth/login", methods=["POST"])
def checkIfLoginExists():
    login = request.form["login"]
    isExists = User.checkUserLogin(login)
    if (isExists):
        return jsonify({"status" : "Exists"})
    else:
        return jsonify({"status" : "Not exists"})

    