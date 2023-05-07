import seaborn as sns
import pandas as pd
import data_procedures as Data
import matplotlib.pyplot as plt


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


def show_profit_table(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(20, 6))
    # fig.patch.set_visible(False)
    ax.axis("off")
    ax.axis("tight")
    table = ax.table(
        cellText=df.values,
        colLabels=df.columns,
        loc="center",
        cellLoc="center",
    )
    table.auto_set_font_size(False)
    table.set_fontsize(6)
    ax.set_title("Profit table by hour")
    plt.tight_layout()

    plt.show()
