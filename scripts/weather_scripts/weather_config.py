SOURCE = "https://open-meteo.com/"


# API

params = {
    "start_date": "2022-01-01",
    "end_date": "2022-12-31",
    "latitude": 40.71,
    "longitude": -74.01,
    "daily": "weathercode",
    "timezone": "America%2FNew_York",
}

OPEN_METEO_URL = "https://archive-api.open-meteo.com/v1/archive?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&daily={daily}&timezone={timezone}"


# ISO WEATHER CODE
WMO_CODE_TABLE = "https://www.nodc.noaa.gov/archive/arc0021/0002199/1.1/data/0-data/HTML/WMO-CODE/WMO4677.HTM"
