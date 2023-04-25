import seaborn as sns
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt


def load_dataset():
    return sns.load_dataset("taxis")

def distance_group_column(df: pd.DataFrame)-> pd.DataFrame:
    "returned new column with distance group names"
    
    df['distance_group'] = pd.cut(df['distance'], bins=[0, 5, 15, float("inf")], labels=['short', 'medium', 'long'])
    
    return df

def calculate_gasoline_consumption(df: pd.DataFrame, gasoline_consuption = 5, gasoline_price = 1.4)-> pd.DataFrame:
    "calculate gasoline consuption cost"
    return df.assign(gas_expense = lambda x: gasoline_consuption * x['distance']/100*gasoline_price)
  
    
def calculate_auto_utilization(df: pd.DataFrame)->pd.DataFrame:
    "calculate auto utilization cost"
    auto_utilization_cost = 215
    df = df.assign(utilization_cost = lambda x: auto_utilization_cost * x['distance']/1000)
    return df

def group_by_distance(df: pd.DataFrame) -> pd.DataFrame:
    """group by distance and calculate profit"""
    df = df.groupby(['distance_group'], as_index= False ).agg(
            count_summons = ('pickup','count'),
            dist_avg = ('distance','mean'),
            dist_total = ('distance','sum'),
            dist_min = ('distance', 'min'),
            dist_max = ('distance', 'max'),
           fare = ('fare','sum'),
           tips = ('tip', 'sum'),
           tolls = ('tolls', 'sum'),
           gas_expense = ('gas_expense', 'sum'),
           auto_utilization_cost = ('utilization_cost', 'sum'),
           hours_sum = ('work_hours','sum')
        )
    return df  

def calculate_work_hours(df: pd.DataFrame)-> pd.DataFrame:
    
    return (df.assign(date_diff = lambda x: x['dropoff'] - x['pickup'])
            .assign(work_hours = lambda x: x['date_diff'].dt.total_seconds() / 60 / 60))
    
   
def calculate_profit_by_hour(df: pd.DataFrame)-> pd.DataFrame:
    df = df.assign(profit_per_hour = lambda x: x['total']/x['hours_sum'])
    
    return df
    
def calculate_total_profit(df: pd.DataFrame)->pd.DataFrame:
    "Get total profit"
    df = df.assign(total = lambda x: sum([x['fare'],x['tips']-sum([x['tolls'],x['gas_expense'],x['auto_utilization_cost']])]))
    return df



def add_week_day(df:pd.DataFrame)->pd.DataFrame:
    df = df.assign(week_day = lambda x: x['pickup'].dt.day_name())
    return df


def get_time_groups(df:pd.DataFrame) -> pd.DataFrame:
    
    labels = []
    for i in range(0, 24, 3):
        time_label = '{:02d}-{:02d}'.format(i, i+3)
        labels.append(time_label)
    
    df['pickup_temp'] = pd.to_datetime(df['pickup'] + pd.Timedelta(hours=1))
    df['3h_interval'] = pd.cut(df['pickup_temp'].dt.hour, 
        bins=list(range(0, 25, 3)),
        labels=labels)
    df = df.drop(columns='pickup_temp')
    
    return df

def group_by_time_weekdays(df:pd.DataFrame) -> pd.DataFrame:
    df = df.groupby(['week_day','3h_interval'], as_index= False).sum()
    return df

def create_pivot_table(df:pd.DataFrame, values:str, index='week_day', columns='3h_interval') -> pd.DataFrame:
    weeks_labels = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    return pd.pivot_table(df, values=values, index=index, columns=columns).reindex(weeks_labels)
    
def visual_hot_map(df:pd.DataFrame, title:str, **kwargs) -> sns.heatmap:
    
    ax = sns.heatmap(df,cmap='coolwarm',linecolor='black',linewidth=1, **kwargs)
    ax.set_title(title, fontsize=18)
    
    return ax

def calculate_passengers_fare_index(df: pd.DataFrame) -> pd.DataFrame:
    return df.assign(profit_by_passenger = lambda x: x['fare']/x['passengers'])
    
    
def visualisation_main(df:pd.DataFrame, by:str, visual:bool = True)-> sns.heatmap or pd.DataFrame:
    """by: [passengers, fare, profit_by_passenger, tip]
    """
    pivot = create_pivot_table(df, values=by)
    if visual: 
        visualisation_1 = visual_hot_map(pivot, title=f'by_{by}')
        return visualisation_1
    else:
        return pivot
    

def get_tips_sum(df: pd.DataFrame):
    return df.agg(
    tip_sum_by_cash=('tip', lambda x: x[df['payment'] == 'cash'].sum()),
    tip_sum_by_card=('tip', lambda x: x[df['payment'] == 'credit card'].sum())
    )
    
def get_pick_up_zone_by_card(df: pd.DataFrame):
    return df.loc[df['payment']=='credit card']