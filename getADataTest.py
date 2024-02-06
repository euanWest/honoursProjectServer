# import fastf1 and json
import fastf1
import json
from flask import Flask, jsonify

# Create session to get telemetry data
session = fastf1.get_session(2023, 'Silverstone', 'Q')
session.load()

# Get data on driver
hamilton = session.laps.pick_driver('HAM').pick_fastest().get_pos_data()

# Make new dictionary
telemetryData = []

# Add data to new dictionary
for i in range (0, 335):
    telemetryData.append({'time' : int(hamilton.Time[i].total_seconds()), 'x' : hamilton.X[i], 'y' : hamilton.Y[i], 'z' : hamilton.Z[i]})

# Flask app to serve Json
app = Flask(__name__)
app.debug = True

@app.route("/downloadTel")
def updateCheck():
     # IF Change in github repo
    return jsonify(json.dumps(telemetryData, indent=1))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)

