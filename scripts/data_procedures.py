import pandas as pd
import load_and_save_data as Data


def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    df.rename(
        columns={
            "tpep_pickup_datetime": "pickup",
            "tpep_dropoff_datetime": "dropoff",
            "passenger_count": "passenger",
            "trip_distance": "distance",
            "fare_amount	": "fare",
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
