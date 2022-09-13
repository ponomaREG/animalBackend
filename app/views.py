from app import app

@app.route("/", methods = ["GET"])
def main():
    return "Test commit"