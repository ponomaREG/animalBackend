from operator import truediv
from app.models.SqlExecuter import SqlExecuter
from app.models.token import Token

class User:

    @staticmethod
    def authenticateUser(phone, code):
        newToken = Token.generateToken()
        existsPhone = SqlExecuter.getRowsPacked("SELECT * FROM user WHERE phone = '{}';".format(phone))
        if (len(existsPhone) > 0):
            SqlExecuter.executeQuery("UPDATE user SET token = '{}' WHERE phone = '{}';".format(newToken, phone))
        else:
            SqlExecuter.executeQuery("INSERT INTO user (phone, token) VALUES('{}', '{}');".format(phone, newToken))
        return newToken

    @staticmethod
    def sendOtpCode(phone):
        pass

    @staticmethod
    def checkUserToken(token):
        userRow = SqlExecuter.getRowsPacked("SELECT * FROM user WHERE token = '{}';".format(token))
        return len(userRow) > 0

        