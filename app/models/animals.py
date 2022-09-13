from app.models.SqlExecuter import SqlExecuter
from app import app
import os

class Animal:

    @staticmethod
    def getAllAnimals():
        animals = SqlExecuter.getRowsPacked("SELECT * FROM animal;")
        for a in animals:
            if a["imageSrc"] is not None:
                a["imageSrc"] = app.config["URL_PIC"] + a["imageSrc"]
        return animals

    @staticmethod
    def insertAnimal(name, description, image, latitude, longitude):
        animalId = SqlExecuter.executeQuery("INSERT INTO animal (name, description, latitude, longitude) VALUES ('{}', '{}', '{}', '{}');".format(name, description, latitude, longitude))
        image.save(os.path.join(app.config["UPLOAD_FOLDER"], str(animalId) + ".jpg"))
        SqlExecuter.executeQuery("UPDATE animal SET imageSrc = '{}.jpg' WHERE id = {};".format(animalId, animalId))
        return animalId
