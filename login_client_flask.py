import requests
from flask import Flask, render_template, request

app = Flask(__name__, template_folder="./")

url = "http://localhost:8080/login"

@app.route("/")
def index():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    # getthe uername and password from the form
    username = request.form["username"]
    password = request.form["password"]

    data = {"username":username, "password":password}
    response = requests.post(url, json = data)

    if response.status_code == 200:
        return "Login successful"
    else:
        return "Login unseccessful"

if __name__ == "__main__":
    app.run(debug=True)
