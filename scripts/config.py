import sys
import logging

log = logging.basicConfig(stream=sys.stdout, level=logging.INFO)

import sys
import logging

log = logging.basicConfig(stream=sys.stdout, level=logging.INFO)


# path
INPUT_DATA_PATH = "./data/yellow_trip_data_2022/"
MAP_TAXIS_ZONE_FILE = "./data/map_data/taxi_zone.csv"
PAYMENT_TYPE_FILE = "./data/map_data/payment_type.json"


# path to test
GREEN_FILE = "./data/trip_data_2019_03/green_tripdata_2019-03.parquet"
YELLOW_FILE = "./data/trip_data_2019_03/yellow_tripdata_2019-03.parquet"

GREEN_FILE1 = "./data/trip_data_2019_03/green_tripdata_2019-02.parquet"
YELLOW_FILE1 = "./data/trip_data_2019_03/yellow_tripdata_2019-02.parquet"

# output path
VISUALISATIONS_OUTPUT_PATH = "./output/visualisations/"
EXCEL_OUTPUT_PATH = "./output/excel_files/"
