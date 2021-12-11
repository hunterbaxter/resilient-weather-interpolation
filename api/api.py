import flask
from flask import request, jsonify
from kafka_tools import KafkaWeather

weather_center_names = [
    'center1',
    'center2',
    'center3'
]

kafka = KafkaWeather(weather_center_names, '1.1.1.1.1.2')

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Resilient Weather Kriging</h1>
<p>A simple API for retrieving Weatherbit information to be used by Kepler.gl</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/kepler/data', methods=['GET'])
def api_all():
    return kafka.get_GeoJSON_data()


app.run()
