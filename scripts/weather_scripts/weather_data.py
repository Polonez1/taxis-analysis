import requests
import json
import pandas as pd

import weather_config as Wconfig


def get_weather_data() -> json:
    params = Wconfig.params
    _url = Wconfig.OPEN_METEO_URL

    url = _url.format(**params)

    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()

    else:
        print(f"Response Error: {response.status_code} - {response.text}")

    return weather_data


def get_wmo_code_table():
    url = Wconfig.WMO_CODE_TABLE

    response = requests.get(url)
    if response.status_code == 200:
        df_list = pd.read_html(response.content)
    else:
        print(f"Response Error: {response.status_code} - {response.text}")

    return df_list
