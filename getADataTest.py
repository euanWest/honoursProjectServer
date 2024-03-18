# import fastf1 and json
import fastf1
import json
from flask import Flask, jsonify

# Create session to get telemetry data
session = fastf1.get_session(2023, 'Silverstone', 'R')
session.load()

telemetryData = []

# Creates array for all the drivers in the race
drivers = session.drivers

# For every driver in the race, create a record with their name and telemetry data.
for driver in drivers:
    dataFromApi = session.laps.pick_driver(driver)
    driverData = []
    end = False
    i = 0
    while end == False:
        if dataFromApi.Time[i].total_seconds == None:
            end = True
        else:
            # swap X and Z axis so that it matches Unity.
            driverData.append({'time' : str(dataFromApi.Time[i].total_seconds()), 'x' : str(dataFromApi.X[i]), 'y' : str(dataFromApi.Z[i]), 'z' : str(dataFromApi.Y[i])})
            ++i
    telemetryData.append({'name' : str(driver), 'data' : str(driverData)})


# Flask app to serve Json
app = Flask(__name__)
app.debug = True

@app.route("/downloadTel")
def updateCheck():
     # IF Change in github repo
    return jsonify(telemetryData)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)

