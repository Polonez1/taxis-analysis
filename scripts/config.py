import sys
import logging

log = logging.basicConfig(stream=sys.stdout, level=logging.INFO)

import sys
import logging

log = logging.basicConfig(stream=sys.stdout, level=logging.INFO)


# path
INPUT_DATA_PATH = ".\\data\\yellow_trip_data_2022\\"
MAP_TAXIS_ZONE_FILE = ".\\data\\map_data\\taxi_zone.csv"
PAYMENT_TYPE_FILE = ".\\data\\map_data\\payment_type.json"


# path to test
GREEN_FILE = ".\\data\\trip_data_201903_to_test\\green_tripdata_2019-03.parquet"
YELLOW_FILE = ".\\data\\trip_data_201903_to_test\\yellow_tripdata_2019-03.parquet"
