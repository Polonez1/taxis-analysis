import argparse
import main
import logging

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="get data visualisation")
    parser.add_argument(
        "--run_visualisation", action="store_true", help="run data visualisation"
    )
    parser.add_argument("--run_table", action="store_true", help="run profit table")

    args = parser.parse_args()

    if args.run_visualisation:
        print("input month(Format: mm)")
        month = input()
        print("Show by: tip, passenger, fare, profit_by_passenger ")
        by = input()
        print(
            "Filtered by date range (if pass, press Enter), Date range format: (yyyy-mm-dd, yyyy-mm-dd)"
        )
        date_range = input()

        main.show_heatmap(month=month, by=by, date_range=())
    elif args.run_table:
        print("input month(Format: mm)")
        month = input()
        print(
            "Filtered by date range (if pass, press Enter), Date range format: (yyyy-mm-dd, yyyy-mm-dd)"
        )
        date_range = input()

        main.show_profit_table(month=month, date_range=())
    else:
        print("Invalid function name")
