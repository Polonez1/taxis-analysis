import pandas as pd
import numpy as np


def change_dtypes_YellowData(df: pd.DataFrame):
    columns_to_int8 = ["VendorID", "payment_type"]
    columns_to_float16 = [
        "passenger_count",
        "RatecodeID",
        "fare_amount",
        "extra",
        "mta_tax",
        "tip_amount",
        "tolls_amount",
        "improvement_surcharge",
        "total_amount",
        "congestion_surcharge",
        "airport_fee",
    ]
    columns_to_int16 = ["PULocationID", "DOLocationID"]

    df[columns_to_int8] = df[columns_to_int8].astype(np.int8)

    df[columns_to_float16] = df[columns_to_float16].astype(np.float16)

    df[columns_to_int16] = df[columns_to_int16].astype(np.int16)

    return df
