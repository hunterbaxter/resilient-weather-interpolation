import flask
from flask import request, jsonify
from kafka_tools import KafkaWeather

weather_center_names = [
    'Center1',
    'Center2',
    'Center3',
    'Center4',
    'Center5',
    'Center6',
    'Center7',
]

kafka = KafkaWeather()

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Resilient Weather Kriging</h1>
<p>A simple API for retrieving Weatherbit information to be used by Kepler.gl</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/kepler/data', methods=['GET'])
def api_all():
    return KafkaWeather.get_GeoJSON_data()


app.run()
