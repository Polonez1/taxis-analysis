import seaborn as sns
import pandas as pd
import os
import logging
import json

import data_validation
import category_and_dtypes as cat
import config

config.log


def get_data_files_list() -> list:
    path = config.INPUT_DATA_PATH
    files_list = os.listdir(path)

    return files_list


def validate_Yellow_taxis_analysis(df):
    df = data_validation.transform_YellowTripData(df)
    return df


def load_data_frame(month: str, year: str = "2022") -> pd.DataFrame:
    """load data frame by year and month

    Args:
        year (str): format: yyyy. Defaut: 2022
        month (str): format: mm

    Returns:
        _type_: pd.DataFrame
    """
    file_name = f"yellow_tripdata_{year}-{month}.parquet"
    path = config.INPUT_DATA_PATH
    df = pd.read_parquet(f"{path}{file_name}", engine="pyarrow")
    df = cat.change_dtypes_YellowData(df)
    df = validate_Yellow_taxis_analysis(df)
    df = cat.category_data(df)
    logging.info(f"\nTransform dtype: Complete\n Validate: Complete\n")
    total_memory_usage = df.memory_usage(deep=True).sum() / (1024 * 1024)
    logging.info(f"DataFrame size: {total_memory_usage:.2f} MB")

    return df


def load_zonemap_data():
    path = config.MAP_TAXIS_ZONE_FILE
    df = pd.read_csv(path)
    return df


def load_payment_type_table():
    path = config.PAYMENT_TYPE_FILE
    df = pd.DataFrame(pd.read_json(path))
    return df


def load_weather_data():
    with open(".\\data\\map_data\\daily_weather.json", "r") as file:
        data = json.load(file)

        return pd.DataFrame(data)


def load_weather_name():
    with open(".\\data\\map_data\\wmo_code.csv", "r") as file:
        data = pd.read_csv(file)

        return data
