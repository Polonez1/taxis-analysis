import sys

sys.path.append(".\\scripts\\")

import load_and_save_data as Data
import data_procedures as DPro

import pandas as pd
import numpy as np
import seaborn as sns
import logging

import config

config.log


def add_data_type(df: pd.DataFrame, data_source):
    df["color"] = f"{data_source}"
    return df


def load_2019_03_TripData(
    data_path,
    data_source: str,
) -> pd.DataFrame:
    df1 = pd.read_parquet(data_path, engine="pyarrow")
    df = add_data_type(df1, f"{data_source}")

    return df


def get_full_original_data():
    green_df = load_2019_03_TripData(data_path=config.GREEN_FILE, data_source="green")
    yellow_df = load_2019_03_TripData(
        data_path=config.YELLOW_FILE, data_source="yellow"
    )
    green_data = rename_columns(green_df, data_source="green")
    yellow_data = rename_columns(yellow_df, data_source="yellow")

    return pd.concat([green_data, yellow_data])


def load_seaborn_trip_data() -> pd.DataFrame:
    return sns.load_dataset("taxis")


def rename_columns(df: pd.DataFrame, data_source: str):
    if data_source == "yellow":
        df = df.rename(
            columns={
                "tpep_pickup_datetime": "pickup",
                "tpep_dropoff_datetime": "dropoff",
                "passenger_count": "passengers",
                "trip_distance": "distance",
                "fare_amount": "fare",
                "tip_amount": "tip",
                "tolls_amount": "tolls",
                "total_amount": "total",
            }
        )
    if data_source == "green":
        df = df.rename(
            columns={
                "lpep_pickup_datetime": "pickup",
                "lpep_dropoff_datetime": "dropoff",
                "passenger_count": "passengers",
                "trip_distance": "distance",
                "fare_amount": "fare",
                "tip_amount": "tip",
                "tolls_amount": "tolls",
                "total_amount": "total",
            }
        )

    return df


def select_data_range(df: pd.DataFrame):
    sns_df = load_seaborn_trip_data()

    min_date = sns_df["pickup"].min()
    max_date = sns_df["pickup"].max()

    df = df.loc[(df["pickup"] >= min_date) & (df["pickup"] <= max_date)]

    return df


def compare_dataframe(df: pd.DataFrame, df1: pd.DataFrame) -> int:
    common_rows = df.merge(df1)
    num_equal_rows = len(common_rows)
    return num_equal_rows


def compare_tables():
    original_data = get_full_original_data()

    sns_data = load_seaborn_trip_data()
    sns_data["passengers"] = sns_data["passengers"].astype("float64")
    sns_data["payment"] = sns_data["payment"].str.lower()

    new_df = (
        original_data.pipe(DPro.join_payment_type)
        .pipe(DPro.join_zones)
        .pipe(select_data_range)
    )
    new_df["payment"] = new_df["payment"].str.lower()

    df = new_df[sns_data.columns]

    types = (df.dtypes == sns_data.dtypes).all()
    headers = (df.columns == sns_data.columns).all()
    congruent_data = compare_dataframe(df, sns_data)
    miss_data = len(sns_data) - congruent_data

    logging.info(f"dtypes: {types}")
    logging.info(f"columns: {headers}")
    logging.info(f"congruent data: {congruent_data}")
    logging.info(f"missed data: {miss_data}")
