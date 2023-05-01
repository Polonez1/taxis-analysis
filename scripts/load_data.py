import seaborn as sns
import pandas as pd
import os


def load_dataset() -> pd.DataFrame:
    """loading test dataset

    Returns:
        _type_: pd.Dataframe
    """
    return sns.load_dataset("taxis")


def collect_data():
    df_list = []
    path = "..\\data\\yellow_trip_data_2022\\"
    files_list = os.listdir(path)
    df_list = [pd.read_parquet(f"{path}{i}", engine="pyarrow") for i in files_list]
    df = pd.concat(df_list)
    return df
