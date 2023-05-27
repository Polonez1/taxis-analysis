import sys

sys.path.append(".\\scripts\\test_scripts\\")

import data_compare as comp


def find_diffs():
    df = comp.test_main().reset_index(drop=True)
    sns_df = comp.load_seaborn_trip_data().reset_index(drop=True)
    sns_df["passengers"] = sns_df["passengers"].astype("float64")

    test = df.loc[
        (df["pickup"] == "2019-03-23 20:21:09")
        & (df["dropoff"] == "2019-03-23 20:27:24")
    ]
    test2 = sns_df.loc[
        (sns_df["pickup"] == "2019-03-23 20:21:09")
        & (sns_df["dropoff"] == "2019-03-23 20:27:24")
    ]

    test = test.reset_index(drop=True)
    test2 = test2.reset_index(drop=True)

    res = test.compare(test2)

    print(res)
