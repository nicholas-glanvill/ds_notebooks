import pandas as pd

# Sample data
data = [
    {
        'departure': {
            'airport': {
                'icao': 'KMCO',
                'iata': 'MCO',
                'name': 'Orlando',
                'timeZone': 'America/New_York'
            },
            'scheduledTime': {
                'utc': '2024-11-05 17:20Z',
                'local': '2024-11-05 12:20-05:00'
            },
            'terminal': 'B',
            'quality': ['Basic']
        },
        'arrival': {
            'scheduledTime': {
                'utc': '2024-11-05 20:12Z',
                'local': '2024-11-05 15:12-05:00'
            },
            'revisedTime': {
                'utc': '2024-11-05 20:12Z',
                'local': '2024-11-05 15:12-05:00'
            },
            'terminal': '1',
            'gate': 'F36',
            'baggageBelt': '9',
            'quality': ['Basic', 'Live']
        },
        'number': 'AC 1675',
        'status': 'Expected',
        'codeshareStatus': 'IsOperator',
        'isCargo': False,
        'aircraft': {'model': 'Airbus A321'},
        'airline': {'name': 'Air Canada', 'iata': 'AC', 'icao': 'ACA'}
    },
    {
        'departure': {
            'airport': {
                'icao': 'KMCO',
                'iata': 'MCO',
                'name': 'Orlando',
                'timeZone': 'America/New_York'
            },
            'scheduledTime': {
                'utc': '2024-11-05 17:20Z',
                'local': '2024-11-05 12:20-05:00'
            },
            'terminal': 'B',
            'quality': ['Basic']
        },
        'arrival': {
            'scheduledTime': {
                'utc': '2024-11-05 20:12Z',
                'local': '2024-11-05 15:12-05:00'
            },
            'revisedTime': {
                'utc': '2024-11-05 20:12Z',
                'local': '2024-11-05 15:12-05:00'
            },
            'terminal': '1',
            'gate': 'F36',
            'baggageBelt': '9',
            'quality': ['Basic', 'Live']
        },
        'number': 'AC 1675',
        'status': 'Expected',
        'codeshareStatus': 'IsOperator',
        'isCargo': False,
        'aircraft': {'model': 'Airbus A330-300'},
        'airline': {'name': 'Air Canada', 'iata': 'AC', 'icao': 'ACA'}
    }
]

# Flattening the data
flattened_data = []
for flight in data:
    try:
        flattened_flight = {
            'flight_number': flight['number'],
            'status': flight['status'],
            'codeshare_status': flight['codeshareStatus'],
            'is_cargo': flight['isCargo'],
            'aircraft_model': flight['aircraft']['model'],
            'airline_name': flight['airline']['name'],
            'airline_iata': flight['airline']['iata'],
            'airline_icao': flight['airline']['icao'],
            'departure_airport_icao': flight['departure']['airport']['icao'],
            'departure_airport_iata': flight['departure']['airport']['iata'],
            'departure_airport_name': flight['departure']['airport']['name'],
            'departure_airport_timezone': flight['departure']['airport']['timeZone'],
            'departure_scheduled_time_utc': flight['departure']['scheduledTime']['utc'],
            'departure_scheduled_time_local': flight['departure']['scheduledTime']['local'],
            'departure_terminal': flight['departure']['terminal'],
            'departure_quality': ', '.join(flight['departure']['quality']),
            'arrival_scheduled_time_utc': flight['arrival']['scheduledTime']['utc'],
            'arrival_scheduled_time_local': flight['arrival']['scheduledTime']['local'],
            'arrival_revised_time_utc': flight['arrival']['revisedTime']['utc'],
            'arrival_revised_time_local': flight['arrival']['revisedTime']['local'],
            'arrival_terminal': flight['arrival']['terminal'],
            'arrival_gate': flight['arrival']['gate'],
            'arrival_baggage_belt': flight['arrival']['baggageBelt'],
            'arrival_quality': ', '.join(flight['arrival']['quality']),
        }
        flattened_data.append(flattened_flight)
    except TypeError as e:
        print(f"Error processing flight data: {e}")

# Creating DataFrame
df = pd.DataFrame(flattened_data)

# Display the DataFrame
print(df)
