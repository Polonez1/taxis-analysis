import pandas as pd
from datetime import datetime

import load_and_save_data as Data


def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    df.rename(
        columns={
            "tpep_pickup_datetime": "pickup",
            "tpep_dropoff_datetime": "dropoff",
            "passenger_count": "passenger",
            "trip_distance": "distance",
            "fare_amount": "fare",
            "tip_amount": "tip",
            "tolls_amount": "tolls",
            "total_amount": "total",
        },
        inplace=True,
    )
    return df


def join_zones(df: pd.DataFrame) -> pd.DataFrame:
    """joining Borough and zone by pickon and dropoff values.

    Args:
        df (pd.DataFrame): general taxis table

    Returns:
        pd.DataFrame: new taxis table with zones
    """
    zones_df = Data.load_zonemap_data()

    id_to_location = zones_df.set_index("LocationID")[["Borough", "Zone"]]

    df = df.join(id_to_location, on="PULocationID").rename(
        columns={"Borough": "pickup_borough", "Zone": "pickup_zone"}
    )
    df = df.join(id_to_location, on="DOLocationID").rename(
        columns={"Borough": "dropoff_borough", "Zone": "dropoff_zone"}
    )

    return df


def join_payment_type(df: pd.DataFrame) -> pd.DataFrame:
    payment_type = Data.load_payment_type_table()

    id_to_type = payment_type.set_index("type_id")["type"]
    df["payment"] = df["payment_type"].map(id_to_type)

    return df


def drop_unnecessary_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop(
        columns=[
            "RatecodeID",
            "store_and_fwd_flag",
            "PULocationID",
            "DOLocationID",
            "payment_type",
        ]
    )
    return df


def filtered_by_date(df: pd.DataFrame, start_date="", end_date="") -> pd.DataFrame:
    """filtered df by date
    min date: 2019-02-28
    max date: 2019-03-31
    Args:
        df (pd.DataFrame): df
        date_range (tuple): ('start_date': yyyy-mm-dd, 'end_date': yyyy-mm-dd). Default date_range = ()
    Returns:
        pd.DataFrame: new dataframe
    """
    if start_date != "" and end_date != "":
        return df
    else:
        start_date = start_date
        end_date = end_date
        dt_range = (df["pickup"] >= start_date) & (df["pickup"] <= end_date)
        filtered_df = df.loc[dt_range]
        return filtered_df


def distance_group_column(df: pd.DataFrame) -> pd.DataFrame:
    "returned new column with distance group names"

    df["distance_group"] = pd.cut(
        df["distance"],
        bins=[0, 5, 15, float("inf")],
        labels=["short", "medium", "long"],
    )

    return df


def group_by_distance(df: pd.DataFrame) -> pd.DataFrame:
    """group by distance and calculate profit"""
    df = df.groupby(["distance_group"], as_index=False).agg(
        count_summons=("pickup", "count"),
        dist_avg=("distance", "mean"),
        dist_total=("distance", "sum"),
        dist_min=("distance", "min"),
        dist_max=("distance", "max"),
        fare=("fare", "sum"),
        tips=("tip", "sum"),
        tolls=("tolls", "sum"),
        gas_expense=("gas_expense", "sum"),
        auto_utilization_cost=("utilization_cost", "sum"),
        hours_sum=("work_hours", "sum"),
    )
    return df


def add_week_day(df: pd.DataFrame) -> pd.DataFrame:
    df = df.assign(week_day=lambda x: x["pickup"].dt.day_name())
    return df


def get_time_groups(df: pd.DataFrame) -> pd.DataFrame:
    labels = []
    for i in range(0, 24, 3):
        time_label = "{:02d}-{:02d}".format(i, i + 3)
        labels.append(time_label)

    df["pickup_temp"] = pd.to_datetime(df["pickup"] + pd.Timedelta(hours=1))
    df["3h_interval"] = pd.cut(
        df["pickup_temp"].dt.hour, bins=list(range(0, 25, 3)), labels=labels
    )
    df = df.drop(columns="pickup_temp")

    return df


def group_by_time_weekdays(df: pd.DataFrame) -> pd.DataFrame:
    columns_to_sum = ["tip", "fare", "passenger"]
    df = df.groupby(["week_day", "3h_interval"], as_index=False)[columns_to_sum].sum(
        numeric_only=False
    )
    return df


def group_by_weather(df: pd.DataFrame):
    df = df.groupby(["weather"], as_index=False)["passenger"].sum()
    return df


def create_pivot_table(
    df: pd.DataFrame, values: str, index="week_day", columns="3h_interval"
) -> pd.DataFrame:
    weeks_labels = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    return pd.pivot_table(df, values=values, index=index, columns=columns).reindex(
        weeks_labels
    )


def add_date_column(df: pd.DataFrame):
    df = df.assign(date=lambda x: pd.to_datetime(x["pickup"]).dt.date.astype("str"))

    return df


def join_weathercode(df: pd.DataFrame):
    weather_df = Data.load_weather_data()
    id_to_type = weather_df.set_index("time")["weathercode"]
    df["weatercode"] = df["date"].map(id_to_type)

    return df


def join_weather_name(df: pd.DataFrame):
    weather = Data.load_weather_name()

    id_to_weathercode = weather.set_index("Code figure")["weather"]
    df["weather"] = df["weatercode"].map(id_to_weathercode)

    return df


def get_clear_dataframe(month: str, **kwargs) -> pd.DataFrame:
    """get dataframe to work after all data procedures

    Args:
        month (str): format: mm
    Kwargs:
        yeart (str): format: yyyy. Default: 2022

    Returns:
        pd.DataFrame: returned clear dataframe
    """
    df = Data.load_data_frame(month=month, **kwargs)

    df = (
        df.pipe(rename_columns)
        .pipe(join_zones)
        .pipe(join_payment_type)
        .pipe(drop_unnecessary_columns)
        .pipe(add_date_column)
        .pipe(join_weathercode)
        .pipe(join_weather_name)
    )

    return df
