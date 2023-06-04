import argparse
import main
import logging
import pandas as pd

import visualisations
import load_and_save_data
import config

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="get data visualisation")
    parser.add_argument(
        "--run_visualisation",
        action="store_true",
        help="run data visualisation",
    )  # done

    parser.add_argument("--run_table", action="store_true", help="run profit table")

    parser.add_argument(
        "--run_weather_bar", action="store_true", help="run bar visualisation"
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

    args = parser.parse_args()

    if args.run_visualisation:
        month = args.month
        by = args.by
        date_range = ()  # fix
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
        print("input month(Format: mm)")
        month = input()
        print(
            "Filtered by date range (if pass, press Enter), Date range format: (yyyy-mm-dd, yyyy-mm-dd)"
        )
        date_range = input()
        logging.info(f"Data load...please wait")
        main.show_weather_visualisation(month=month, date_range=())
    elif args.run_data_compare:
        logging.info("....>")
        main.data_compare_run()

    else:
        logging.warning("Wrong command")
