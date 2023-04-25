import pandas as pd
import sys
sys.path.insert(0, "..\\scripts\\")
import scripts.taxis_analysis_function as taxis_analysis_function
#import os

#print(os.getcwd())


def test_time_interval_groups():
    df = pd.DataFrame({"pickup": [pd.Timestamp('2019-03-23 00:30:09'), pd.Timestamp('2019-03-23 03:21:09'),
                                  pd.Timestamp('2019-03-23 06:57:09'), pd.Timestamp('2019-03-23 09:45:09'),
                                  pd.Timestamp('2019-03-23 12:30:09'), pd.Timestamp('2019-03-23 15:21:09'),
                                  pd.Timestamp('2019-03-23 18:30:09'), pd.Timestamp('2019-03-23 21:21:09')
                                  ]
                       })
    df_expected = pd.DataFrame(
        {
            "pickup": [pd.Timestamp('2019-03-23 00:30:09'), pd.Timestamp('2019-03-23 03:21:09'),
                    pd.Timestamp('2019-03-23 06:57:09'), pd.Timestamp('2019-03-23 09:45:09'),
                    pd.Timestamp('2019-03-23 12:30:09'), pd.Timestamp('2019-03-23 15:21:09'),
                    pd.Timestamp('2019-03-23 18:30:09'), pd.Timestamp('2019-03-23 21:21:09')
                                  ],
            "3h_interval": ['00-03', '03-06', '06-09', '09-12', '12-15', '15-18', '18-21', '21-24']
            
        }
    )
    categories = ['00-03', '03-06', '06-09', '09-12', '12-15', '15-18', '18-21', '21-24']
    df_expected['3h_interval'] = df_expected['3h_interval'].astype(pd.CategoricalDtype(categories=categories, ordered=True))
    df_expected.Name = '3h_interval'
    
    df_expected.Name = '3h_interval'
    result = taxis_analysis_function.get_time_groups(df)
    pd.testing.assert_frame_equal(result, df_expected)
    