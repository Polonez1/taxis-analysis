import matplotlib
import seaborn as sns
import plotly.figure_factory as ff
import logging
import pandas as pd


# matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

import sys

# sys.path.append(".\\scripts\\")
# sys.path.append(".\\scripts\\data_compare_scripts\\")


from scripts import data_procedures
from scripts import calculate

from scripts import visualisations
from scripts.data_compare_scripts import data_compare

import config


def call_heatmap_object(
    month: str, by: str, start_date="", end_date="", **kwargs
) -> plt.subplot:
    """This function creating sns.heatmap by tip, passenger, fare and profit_by_passenger

    Args:
        month (str): format mm
        by (str): tip, passenger, fare, profit_by_passenger
    """
    config.log

    df = data_procedures.get_clear_dataframe(month=month)

    if start_date != "" and end_date != "":
        df = data_procedures.filtered_by_date(
            df, start_date=start_date, end_date=end_date
        )
        logging.info(f"Filtered date range: {start_date}, {end_date}")

    general_dataframe = (
        df.pipe(data_procedures.add_week_day)
        .pipe(data_procedures.get_time_groups)
        .pipe(data_procedures.group_by_time_weekdays)
        .pipe(calculate.calculate_passengers_fare_index)
    )

    heat_map = visualisations.create_heatmap_object(
        general_dataframe, by=f"{by}", **kwargs
    )
    logging.info(f"Data shape: {df.shape}")
    logging.info(f"Data lenght: {len(general_dataframe)}")

    # plt.show(block=True)

    return heat_map


def create_profit_table(month: str, start_date="", end_date="") -> pd.DataFrame:
    config.log

    df = data_procedures.get_clear_dataframe(month=month)

    if start_date != "" and end_date != "":
        df = data_procedures.filtered_by_date(
            df, start_date=start_date, end_date=end_date
        )
        logging.info(f"Filtered date range: {start_date}, {end_date}")

    distance_profit_analysis = (
        df.pipe(data_procedures.distance_group_column)
        .pipe(calculate.calculate_work_hours)
        .pipe(calculate.calculate_gasoline_consumption)
        .pipe(calculate.calculate_auto_utilization)
        .pipe(data_procedures.group_by_distance)
        .pipe(calculate.calculate_total_profit)
        .pipe(calculate.calculate_profit_by_hour)
    )
    logging.info(f"Data lenght: {len(df)}")

    return distance_profit_analysis

    # vs.show_profit_table(distance_profit_analysis)


def create_weather_table(month: str, start_date="", end_date="") -> plt.bar:
    config.log

    df = data_procedures.get_clear_dataframe(month=month)

    if start_date != "" and end_date != "":
        df = data_procedures.filtered_by_date(
            df, start_date=start_date, end_date=end_date
        )
        logging.info(f"Filtered date range: {start_date}, {end_date}")

    df = data_procedures.group_by_weather(df)

    return df
    # vs.show_weather_bar(df)


def data_compare_run():
    data_compare.compare_tables()
