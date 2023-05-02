import pandas as pd


def calculate_gasoline_consumption(
    df: pd.DataFrame, gasoline_consuption=5, gasoline_price=1.4
) -> pd.DataFrame:
    "calculate gasoline consuption cost"
    return df.assign(
        gas_expense=lambda x: gasoline_consuption * x["distance"] / 100 * gasoline_price
    )


def calculate_auto_utilization(df: pd.DataFrame) -> pd.DataFrame:
    "calculate auto utilization cost"
    auto_utilization_cost = 215
    df = df.assign(
        utilization_cost=lambda x: auto_utilization_cost * x["distance"] / 1000
    )
    return df


def calculate_work_hours(df: pd.DataFrame) -> pd.DataFrame:
    return df.assign(date_diff=lambda x: x["dropoff"] - x["pickup"]).assign(
        work_hours=lambda x: x["date_diff"].dt.total_seconds() / 60 / 60
    )


def calculate_profit_by_hour(df: pd.DataFrame) -> pd.DataFrame:
    df = df.assign(profit_per_hour=lambda x: x["total"] / x["hours_sum"])

    return df


def calculate_total_profit(df: pd.DataFrame) -> pd.DataFrame:
    "Get total profit"
    df = df.assign(
        total=lambda x: sum(
            [
                x["fare"],
                x["tips"]
                - sum([x["tolls"], x["gas_expense"], x["auto_utilization_cost"]]),
            ]
        )
    )
    return df


def calculate_passengers_fare_index(df: pd.DataFrame) -> pd.DataFrame:
    return df.assign(profit_by_passenger=lambda x: x["fare"] / x["passenger"])


def get_tips_sum(df: pd.DataFrame):
    return df.agg(
        tip_sum_by_cash=("tip", lambda x: x[df["payment"] == "cash"].sum()),
        tip_sum_by_card=("tip", lambda x: x[df["payment"] == "credit card"].sum()),
    )
