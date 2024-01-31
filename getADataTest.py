# import fastf1 and json
import fastf1
import json

# Create session to get telemetry data
session = fastf1.get_session(2023, 'Silverstone', 'Q')
session.load()

# Get data on driver
hamilton = session.laps.pick_driver('HAM').pick_fastest().get_pos_data()

# Make new dictionary
telemetryData = []

# Add data to new dictionary
for i in range (0, 335):
    telemetryData.append({'time' : hamilton.Time[i], 'x' : hamilton.X[i], 'y' : hamilton.Y[i], 'z' : hamilton.Z[i]})

# Test print
#print(telemetryData)
with open('telData.json', 'w') as file:
    json.dump(str(telemetryData), file)
