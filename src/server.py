"""
This flask server must be run on the stations connected to the servers.
"""
from flask import Flask, jsonify
import reader

app = Flask(__name__)

@app.route("/data", methods=["get"])
def read():
    temperature, humidity = reader.read_from_sensor()
    return jsonify({
            "temperature" : temperature,
            "humidity" : humidity,
    })

if __name__ == '__main__':
    # host = 0.0.0.0 to be accesable on the local network
    app.run(debug=True, host="0.0.0.0")
