import seaborn as sns
import pandas as pd
import data_procedures as Data


def visual_hot_map(df: pd.DataFrame, title: str, **kwargs) -> sns.heatmap:
    ax = sns.heatmap(df, cmap="coolwarm", linecolor="black", linewidth=1, **kwargs)
    ax.set_title(title, fontsize=18)

    return ax


def show_heatmap(df: pd.DataFrame, by: str, **kwargs) -> sns.heatmap:
    """get table or heatmap by passengers, fare, profit_by_passenger, tip
    Args:
        df (pd.DataFrame): df
        by (str):  passengers, fare, profit_by_passenger, tip
        kwargs: sns.heatmap parameters
    Returns:
        sns.heatmap or pd.DataFrame: _description_
    """
    pivot = Data.create_pivot_table(df, values=by)
    visualisation_1 = visual_hot_map(pivot, title=f"by_{by}", **kwargs)
    return visualisation_1
