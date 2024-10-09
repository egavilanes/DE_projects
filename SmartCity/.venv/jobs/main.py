import os
from confluent_kafka import SerializingProducer
import simplejson as json

LONDON_COORDINATES = {"lattitude": 51.5074, "longitude": -0.1278}
BIRMINGHAM_COORDINATES = {"lattitude": 52.4862, "longitude": -1.8904}

# calculate movement increments
LATTITUDE_INCREMEMNT = (BIRMINGHAM_COORDINATES['lattitude'] - LONDON_COORDINATES['lattitude'])
LONGITUDE_INCREMENT = (BIRMINGHAM_COORDINATES['longitude'] - LONDON_COORDINATES['longitude'])

# environment variables for configuration
KAFKA_BOOTSTARP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
VEHICLE_TOPIC = os.getenv('VEHICLE_TOPIC', 'vehicle_data')
GPS_TOPIC = os.getenv('GPS_TOPIC', 'gps_data')
TRAFFIC_TOPIC = os.getenv('')