# import fastf1 and json
import fastf1
import json

# Create session to get telemetry data
session = fastf1.get_session(2023, 'Silverstone', 'Q')
session.load()

# Get data on driver
hamilton = session.laps.pick_driver('HAM').pick_fastest().get_pos_data()

# Make new dictionary
telemetryData = {
    "time" : float,
    "x" : int,
    "y" : int,
    "z" : int
}

# Add data to new dictionary
for record in hamilton:
    telemetryData.update({time = record.Time, x = record.X, y = record.Y, z = record.Z})

# Test print
print(telemetryData)
with open('telData.json', 'w') as file:
    json.dump(telemetryData, file)
