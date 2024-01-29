# import fastf1
import fastf1

# Create session to get telemetry data
session = fastf1.get_session(2023, 'Silverstone', 'Q')
session.load(telemetry = True, laps = False, weather = False)

# Get data on driver
hamilton = session.get_driver('HAM')
hamCarData = hamilton.get_pos_data()

#Test print
print(hamCarData)