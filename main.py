import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

# import os

import sys

sys.path.append(".\\scripts\\")
import taxis_analysis as MyFn
import seaborn as sns

sns.set(style="ticks", color_codes=True)
plt.ion()

df = MyFn.load_dataset()
df = MyFn.filtered_by_date(df, date_range=("2019-02-28", "2019-03-31"))
general_dataframe = (
    df.pipe(MyFn.add_week_day)
    .pipe(MyFn.get_time_groups)
    .pipe(MyFn.group_by_time_weekdays)
    .pipe(MyFn.calculate_passengers_fare_index)
)

MyFn.show_heatmap(general_dataframe, by="tip")

plt.show(block=True)
