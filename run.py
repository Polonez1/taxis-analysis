import argparse

import main

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="get data visualisation")
    parser.add_argument("--run_visualisation", type=str, help="main")

    args = parser.parse_args()

    if args.function_name == "--run_visualisation":
        main.main()
    else:
        print("Invalid function name")
