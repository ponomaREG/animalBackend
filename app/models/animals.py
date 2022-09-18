from app.models.SqlExecuter import SqlExecuter
from app.models.users import User
from app import app
import os

class Animal:

    @staticmethod
    def getAllAnimals():
        animals = SqlExecuter.getRowsPacked("SELECT * FROM animal;")
        for a in animals:
            if a["imageSrc"] is not None:
                a["imageSrc"] = app.config["URL_PIC"] + a["imageSrc"]
                
            a.pop("id_user")
        return animals

    @staticmethod
    def insertAnimal(name, description, image, latitude, longitude, token):
        userId = User.getUserByToken(token)["id"]
        animalId = SqlExecuter.executeQuery("INSERT INTO animal (name, description, latitude, longitude, id_user) VALUES ('{}', '{}', '{}', '{}', {});".format(name, description, latitude, longitude, userId))
        if (image is not None):
            image.save(app.config["UPLOAD_FOLDER"] + "/" + str(animalId) + ".jpg")
            SqlExecuter.executeQuery("UPDATE animal SET imageSrc = '{}.jpg' WHERE id = {};".format(animalId, animalId))
        return animalId

    @staticmethod
    def getAnimaInfo(animalId):
        animal = SqlExecuter.getRowPacked("SELECT * FROM animal WHERE id = {};".format(animalId))
        
        if animal["imageSrc"] is not None:
            animal["imageSrc"] = app.config["URL_PIC"] + animal["imageSrc"]
        userId = animal["id_user"]
        animal.pop("id_user")
        userLogin = SqlExecuter.getRowPacked("SELECT * FROM user where id = {};".format(userId))["login"]
        animal["userLogin"] = userLogin
        return animal
