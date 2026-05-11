import argparse
from src.display import display_most_important
from src.display import show_rows
from src.data_loader import df
from src.utils import row_generator
from src.menu import SleepAnalyticsMenu


def main():
    parser = argparse.ArgumentParser(
        description="CLI для анализа сна"
    )

    parser.add_argument(
        "command",
        help="analysis, stream_rows, menu"
    )

    args = parser.parse_args()

    if args.command == "analysis":
        display_most_important()
    elif args.command == "stream_rows":
        show_rows(row_generator, df)
    elif args.command == "menu":
        GUI = SleepAnalyticsMenu()
        GUI.main_menu()
    else:
        print(f"Неизвестная команда: {args.command}")


if __name__ == "__main__":
    main()