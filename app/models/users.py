from lib2to3.pgen2 import token
from operator import truediv
from app.models.SqlExecuter import SqlExecuter
from app.models.token import Token

class User:

    @staticmethod
    def authenticateUser(phone, code, login):
        newToken = Token.generateToken()
        existsPhone = SqlExecuter.getRowsPacked("SELECT * FROM user WHERE phone = '{}';".format(phone))
        if (len(existsPhone) > 0):
            SqlExecuter.executeQuery("UPDATE user SET token = '{}' WHERE phone = '{}';".format(newToken, phone))
        else:
            SqlExecuter.executeQuery("INSERT INTO user (phone, token, login) VALUES('{}', '{}', '{}');".format(phone, newToken, login))
        return newToken

    @staticmethod
    def sendOtpCode(phone):
        pass

    @staticmethod
    def getUserByToken(token):
        userRow = SqlExecuter.getRowsPacked("SELECT * FROM user WHERE token = '{}';".format(token))
        return userRow[0]

    @staticmethod
    def checkUserToken(token):
        userRow = SqlExecuter.getRowsPacked("SELECT * FROM user WHERE token = '{}';".format(token))
        return len(userRow) > 0

        