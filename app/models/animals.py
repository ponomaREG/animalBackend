import sqlite3
from app.models.SqlExecuter import SqlExecuter
from app import app

class Animal:

    @staticmethod
    def getAllAnimals():
        animals = SqlExecuter.getRowsPacked("SELECT * FROM animal;")
        for a in animals:
            a["imageSrc"] = app.config["URL_PIC"] + a["imageSrc"]
        return animals