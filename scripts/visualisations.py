import seaborn as sns
import pandas as pd


def visual_hot_map(df: pd.DataFrame, title: str, **kwargs) -> sns.heatmap:
    ax = sns.heatmap(df, cmap="coolwarm", linecolor="black", linewidth=1, **kwargs)
    ax.set_title(title, fontsize=18)

    return ax
