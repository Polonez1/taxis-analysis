import pandas as pd
import pandera as pa
from pandera.typing import Index, DataFrame, Series
from datetime import datetime
from pandera import dtypes
import logging as log

import config

config.log


class InputSchema:
    class YellowTripData(pa.SchemaModel):
        VendorID: Series[int] = pa.Field(coerce=True, nullable=True)
        tpep_pickup_datetime: Series[pa.DateTime] = pa.Field(coerce=True)
        tpep_dropoff_datetime: Series[pa.DateTime] = pa.Field(coerce=True)
        passenger_count: Series[float] = pa.Field(coerce=True, nullable=True)
        trip_distance: Series[float] = pa.Field(coerce=True, nullable=True)
        RatecodeID: Series[float] = pa.Field(coerce=True, nullable=True)
        store_and_fwd_flag: Series[str] = pa.Field(coerce=True, nullable=True)
        PULocationID: Series[int] = pa.Field(coerce=True, nullable=True)
        DOLocationID: Series[int] = pa.Field(coerce=True, nullable=True)
        payment_type: Series[int] = pa.Field(coerce=True, nullable=True)
        fare_amount: Series[float] = pa.Field(coerce=True, nullable=True)
        extra: Series[float] = pa.Field(coerce=True, nullable=True)
        mta_tax: Series[float] = pa.Field(coerce=True, nullable=True)
        tip_amount: Series[float] = pa.Field(coerce=True, nullable=True)
        tolls_amount: Series[float] = pa.Field(coerce=True, nullable=True)
        improvement_surcharge: Series[float] = pa.Field(coerce=True, nullable=True)
        total_amount: Series[float] = pa.Field(coerce=True, nullable=True)
        congestion_surcharge: Series[float] = pa.Field(coerce=True, nullable=True)
        airport_fee: Series[float] = pa.Field(coerce=True, nullable=True)


class OutputSchema:
    class YellowTripData(InputSchema.YellowTripData):
        pass


@pa.check_types
def transform_YellowTripData(
    df: DataFrame[InputSchema.YellowTripData],
) -> DataFrame[OutputSchema.YellowTripData]:
    log.info(f"Table YellowTripData validation complete. DataFrame shape: {df.shape}")
    return df
