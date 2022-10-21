
from datetime import datetime
import requests

# date = datetime.datetime(2013, 7, 6,12,12,12,12)
pickup_lon = -73.950655
pickup_lat = 40.783282
dropoff_lon = -73.984365
dropoff_lat = 40.769802


passenger_count = 1


url = 'https://taxifare-john-uiovyej6ca-ew.a.run.app//predict'

PARAMS = {'pickup_datetime':'2013-07-06 17:18:00',
        'pickup_longitude': pickup_lon,
        'pickup_latitude': pickup_lat,
        'dropoff_longitude': dropoff_lon,
        'dropoff_latitude': dropoff_lat,
        'passenger_count': passenger_count}

r = requests.get(url = url, params = PARAMS)
data = r.json()

print(data)
