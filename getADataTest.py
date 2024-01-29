# import fastf1
import fastf1

# Create session to get telemetry data
session = fastf1.get_session(2023, 'Silverstone', 'Q')
session.load()

# Get data on driver
hamilton = session.laps.pick_driver('HAM').get_pos_data()

#Test print
print(hamilton)