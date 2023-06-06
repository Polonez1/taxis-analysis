import argparse
import main
import logging
import pandas as pd

import visualisations
import load_and_save_data
import config

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="get data visualisation by weeks name and time periods"
    )
    parser.add_argument(
        "--run_visualisation",
        action="store_true",
        help="run data visualisation",
    )

    parser.add_argument(
        "--run_table",
        action="store_true",
        help="get profit by hour table and other stats",
    )

    parser.add_argument(
        "--run_weather_bar",
        action="store_true",
        help="get bar visualisation by weather",
    )
    parser.add_argument(
        "--run_data_compare",
        action="store_true",
        help="run bar visualisation",
    )

    # ------Args and actions----------#
    parser.add_argument(
        "--action", choices=["show", "save"], help="choose action: show or save"
    )

    parser.add_argument("--month", type=str, help="month (Format: mm)")
    parser.add_argument(
        "--by", type=str, help="show by: tip, passenger, fare, profit_by_passenger"
    )
    parser.add_argument(
        "-sd",
        type=str,
        default="",
        help="start_date: enter start date to filter. Format yyyy-mm-dd",
    )
    parser.add_argument(
        "-ed",
        type=str,
        default="",
        help="end_date: enter end date to filter. Format yyyy-mm-dd",
    )
    # start_date and end_date.
    args = parser.parse_args()

    if args.run_visualisation:
        month = args.month
        by = args.by
        start_date = args.start_date
        end_date = args.end_date
        logging.info(f"Data load...please wait")
        visual_object = main.call_heatmap_object(month=month, by=by, date_range=())
        if args.action == "show":
            visualisations.show_visualization(visual_object)
        elif args.action == "save":
            visualisations.save_visualisation_as_png(visual_object, month=month, by=by)

    elif args.run_table:
        month = args.month
        date_range = ()  # fix
        logging.info(f"Data load...please wait")
        profit_table = main.create_profit_table(month=month, date_range=())
        if args.action == "show":
            visualisations.show_profit_table(profit_table)
        elif args.action == "save":
            profit_table.to_excel(
                f"{config.EXCEL_OUTPUT_PATH}profit_exp_month_{month}.xlsx"
            )

    elif args.run_weather_bar:
        month = args.month
        date_range = ()
        logging.info(f"Data load...please wait")
        weather_df = main.create_weather_table(month=month, date_range=())
        if args.action == "show":
            visualisations.show_weather_bar(weather_df)
        elif args.action == "save":
            weather_df.to_excel(
                f"{config.EXCEL_OUTPUT_PATH}weather_table_month_{month}.xlsx"
            )
    elif args.run_data_compare:
        logging.info("....>")
        main.data_compare_run()

    else:
        logging.warning("Wrong command")
