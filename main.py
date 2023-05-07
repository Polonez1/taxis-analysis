import matplotlib
import seaborn as sns

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

import sys

sys.path.append(".\\scripts\\")
import load_and_save_data as Data
import data_procedures as DPro
import calculate as calc
import visualisations as vs


def show_heatmap(month: str, by: str, date_range: tuple = (), **kwargs):
    """This function creating sns.heatmap by tip, passenger, fare and profit_by_passenger

    Args:
        month (str): format mm
        by (str): tip, passenger, fare, profit_by_passenger
    """
    df = Data.load_data_frame(month=month)
    df = (
        df.pipe(DPro.rename_columns)
        .pipe(DPro.join_zones)
        .pipe(DPro.join_payment_type)
        .pipe(DPro.drop_unnecessary_columns)
    )

    if date_range != ():
        df = DPro.filtered_by_date(df, date_range=date_range)

    general_dataframe = (
        df.pipe(DPro.add_week_day)
        .pipe(DPro.get_time_groups)
        .pipe(DPro.group_by_time_weekdays)
        .pipe(calc.calculate_passengers_fare_index)
    )

    vs.show_heatmap(general_dataframe, by=f"{by}", **kwargs)
    plt.show(block=True)


def show_profit_table(month: str, date_range: tuple = ()):
    df = Data.load_data_frame(month=month)

    df = (
        df.pipe(DPro.rename_columns)
        .pipe(DPro.join_zones)
        .pipe(DPro.join_payment_type)
        .pipe(DPro.drop_unnecessary_columns)
    )

    if date_range != ():
        df = DPro.filtered_by_date(df, date_range=date_range)

    distance_profit_analysis = (
        df.pipe(DPro.distance_group_column)
        .pipe(calc.calculate_work_hours)
        .pipe(calc.calculate_gasoline_consumption)
        .pipe(calc.calculate_auto_utilization)
        .pipe(DPro.group_by_distance)
        .pipe(calc.calculate_total_profit)
        .pipe(calc.calculate_profit_by_hour)
    )

    fig, ax = plt.subplots(figsize=(20, 6))
    ax.axis("off")
    ax.axis("tight")
    table = ax.table(
        cellText=distance_profit_analysis.values,
        colLabels=distance_profit_analysis.columns,
        loc="center",
        cellLoc="center",
    )
    table.auto_set_font_size(False)
    table.set_fontsize(6)
    plt.tight_layout()

    plt.show()
