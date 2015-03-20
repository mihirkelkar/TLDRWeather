from flask import Flask, send_from_directory
import pyowm
import json
from codes import codes, images
app = Flask(__name__)

owm = pyowm.OWM('513aad7ba88a01eb528abdccfbe02b5b')

@app.route("/")
def hello():
    return send_from_directory('..', 'index.html')
    

@app.route("/js/<path:path>")
def send_js(path):
    return send_from_directory('../js/', path)

@app.route("/images/<path:path>")
def send_images(path):
    return send_from_directory('../images/', path)
    
@app.route("/css/<path:path>")
def send_css(path):
    return send_from_directory('../css/', path)


@app.route("/weather/<place>", methods=['GET'])
def weatherByCity(place=None):
    if place:
        observation = owm.weather_at_place(place)
        w = observation.get_weather()
        x = getInterpretation(w)
        return json.dumps(x)
    else:
        return "Error"


def getInterpretation(w):
    code = w.get_weather_code()
    x = {}
    x["sentence"] = codes[code]
    x["image"] = images[code]
    return x

    


if __name__ == "__main__":
    app.run(port=8080, debug=True)
