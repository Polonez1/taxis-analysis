import seaborn as sns
import pandas as pd
import os

import data_validation


def get_data_files_list() -> list:
    path = ".\\data\\yellow_trip_data_2022\\"
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
    path = ".\\data\\yellow_trip_data_2022\\"
    df = pd.read_parquet(f"{path}{file_name}", engine="pyarrow")
    df = validate_Yellow_taxis_analysis(df)

    return df


def load_zonemap_data():
    path = ".\\data\\map_data\\taxi_zone.csv"
    df = pd.read_csv(path)
    return df


def load_payment_type_table():
    path = ".\\data\\map_data\\payment_type.json"
    df = pd.DataFrame(pd.read_json(path))
    return df
