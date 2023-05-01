import sys

sys.path.append(".\\scripts\\")

import load_and_save_data as Data
import data_procedures as DPro
import calculate as calc

from tabulate import tabulate

df = Data.load_data_frame(month="03")

df = (
    df.pipe(DPro.rename_columns)
    .pipe(DPro.join_zones)
    .pipe(DPro.join_payment_type)
    .pipe(DPro.drop_unnecessary_columns)
)

# df = DPro.filtered_by_date(df, date_range=("2022-01-01","2022-01-02"))
df = DPro.distance_group_column(df)

distance_profit_analysis = (
    df.pipe(DPro.distance_group_column)
    .pipe(calc.calculate_work_hours)
    .pipe(calc.calculate_gasoline_consumption)
    .pipe(calc.calculate_auto_utilization)
    .pipe(DPro.group_by_distance)
    .pipe(calc.calculate_total_profit)
    .pipe(calc.calculate_profit_by_hour)
)

print(tabulate(distance_profit_analysis, headers="keys", tablefmt="pretty"))
