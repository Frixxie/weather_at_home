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
    app.run(debug=True, host="0.0.0.0")
