from flask import Flask, send_from_directory
import pyowm
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
        x = w.get_wind() 
        x['image'] = "random.jpg"
        x['sentence'] = "Aai zawadya. Its so much colder today"
        return str(x)
    else:
        return "Error"


if __name__ == "__main__":
    app.run(port=8080, debug=True)
