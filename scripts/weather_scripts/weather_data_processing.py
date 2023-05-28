import pandas as pd
import json

import weather_data


def weather_daily_data():
    json_ob = weather_data.get_weather_data()

    with open(".\\data\\map_data\\daily_weather.json", "w") as file:
        json.dump(json_ob["daily"], file)


def weather_code_map():
    df_list = weather_data.get_wmo_code_table()

    index_list = []
    for i, table in enumerate(df_list):
        if "Code figure" in table.columns:
            index_list.append(i)

    frames_list = []
    for i in index_list:
        frames_list.append(df_list[i])

    df = pd.concat(frames_list)

    return df


def trasform_code_table():
    df = weather_code_map()
    df = df.rename(columns={"Unnamed: 1": "weather", "Unnamed: 2": "description"})

    df.to_csv(".\\data\\map_data\\wmo_code.csv", index=False)


weather_daily_data()
