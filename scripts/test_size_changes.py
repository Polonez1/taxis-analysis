import pandas as pd
import logging
import psutil

import category_and_dtypes as cat


import config

config.log


def load_data_frame(month: str = "01", year: str = "2022") -> pd.DataFrame:
    file_name = f"yellow_tripdata_{year}-{month}.parquet"
    path = ".\\data\\yellow_trip_data_2022\\"
    df = pd.read_parquet(f"{path}{file_name}", engine="pyarrow")

    return df


def data_after_dtypes_changes(df):
    df = cat.change_dtypes_YellowData(df)

    return df


def test_calculations(df: pd.DataFrame):
    df = df[
        [
            "trip_distance",
            "fare_amount",
            "extra",
            "mta_tax",
            "tip_amount",
            "tolls_amount",
        ]
    ]
    # I intentionally use the apply function to increase computational load
    df = df.apply(
        lambda x: x[["extra", "mta_tax", "tip_amount", "tolls_amount", "fare_amount"]]
        / x["trip_distance"],
        axis=1,
    )
    return df


def get_dataframes():
    clear_data = load_data_frame()
    new_data = data_after_dtypes_changes(clear_data)

    return clear_data, new_data


def memory_usage_test(df: pd.DataFrame):
    before_memory = psutil.Process().memory_info().rss
    df = test_calculations(df.head(10000))
    after_memory = psutil.Process().memory_info().rss
    memory_usage = (after_memory - before_memory) / (1024 * 1024)
    return memory_usage


def compramison_memory_usage(memory1, memory2):
    info = f"""
    clear_data table memory usage: {memory1:.2f} MB\n
    after dtypes changes table memory usage: {memory2:.2f} MB\n
    """
    logging.info(info)


def test_memory_usage():
    clear_data = load_data_frame()
    new_data = data_after_dtypes_changes(clear_data)

    memory1 = memory_usage_test(clear_data)
    memory2 = memory_usage_test(new_data)
    compramison_memory_usage(memory1=memory1, memory2=memory2)
