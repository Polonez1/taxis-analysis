import pandas as pd
import logging
import psutil

import load_and_save_data as data
import category_and_dtypes as cat
import data_procedures as DPro
import calculate as calc

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


def main_process(df: pd.DataFrame):
    df = (
        df.pipe(DPro.rename_columns)
        .pipe(DPro.join_zones)
        .pipe(DPro.join_payment_type)
        .pipe(DPro.drop_unnecessary_columns)
    )

    general_dataframe = (
        df.pipe(DPro.add_week_day)
        .pipe(DPro.get_time_groups)
        .pipe(DPro.group_by_time_weekdays)
        .pipe(calc.calculate_passengers_fare_index)
    )

    return general_dataframe


def get_dataframes():
    clear_data = load_data_frame()
    new_data = data_after_dtypes_changes(clear_data)

    return clear_data, new_data


def memory_usage_test(df: pd.DataFrame):
    before_memory = psutil.Process().memory_info().rss
    df = main_process(df)
    after_memory = psutil.Process().memory_info().rss
    memory_usage = (after_memory - before_memory) / (1024 * 1024)
    return memory_usage


def compramison_memory_usage():
    df1, df2 = get_dataframes()
    memory1 = memory_usage_test(df1)
    memory2 = memory_usage_test(df2)

    info = f"""
    1 table memory usage: {memory1:.2f} MB\n
    2 table memory usage: {memory2:.2f} MB\n
    """
    logging.info(info)
