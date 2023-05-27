import data_compare
import pandas as pd
import numpy as np


def test_data_compare():
    df1 = pd.DataFrame(
        {
            "col0": [2, 3, 4, 8, 6, 1, 10, 11, 12],
            "col1": [None, np.nan, "gar", "car", "par", "vas", None, "p", "c"],
        }
    )

    df2 = pd.DataFrame(
        {"col0": [1, 2, 3, 4, 5], "col1": ["vas", None, None, "gar", "car"]}
    )

    expected_result = 4

    result = data_compare.compare_dataframe(df=df1, df1=df2)
    comp_result = expected_result == result
    print(comp_result)
