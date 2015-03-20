from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"



@app.route("/city")
def weatherByCity():
    return "WeatherByCity"



if __name__ == "__main__":
        app.run()
