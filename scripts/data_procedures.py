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
    zones_df = Data.load_zonemap_data()

    id_to_location = zones_df.set_index("LocationID")[["Borough", "Zone"]]

    df = df.join(id_to_location, on="PULocationID").rename(
        columns={"Borough": "pickup_borough", "Zone": "pickup_zone"}
    )
    df = df.join(id_to_location, on="DOLocationID").rename(
        columns={"Borough": "dropoff_borough", "Zone": "dropoff_zone"}
    )

    return df
