# import fastf1 and json
import fastf1
import json

# Create session to get telemetry data
session = fastf1.get_session(2023, 'Silverstone', 'Q')
session.load()

# Get data on driver
hamilton = session.laps.pick_driver('HAM').pick_fastest().get_pos_data()

# Test print
print(hamilton)
with open('telData.json', 'w', encoding='utf-8') as f:
    json.dump(str(hamilton), f, ensure_ascii=False, indent=4)
