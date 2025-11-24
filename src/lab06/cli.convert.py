import argparse
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from lib.text import json_to_csv, csv_to_json, csv_to_xlsx


def main():
    parser = argparse.ArgumentParser(description="Конвертер данных между форматами")
    subparsers = parser.add_subparsers(dest="command")

    json_to_csv_parser = subparsers.add_parser(
        "json2csv", help="Конвертировать JSON в CSV"
    )
    json_to_csv_parser.add_argument(
        "--in", dest="input_file", required=True, help="Входной JSON файл"
    )
    json_to_csv_parser.add_argument(
        "--out", dest="output_file", required=True, help="Выходной CSV файл"
    )

    csv_to_json_parser = subparsers.add_parser(
        "csv2json", help="Конвертировать CSV в JSON"
    )
    csv_to_json_parser.add_argument(
        "--in", dest="input_file", required=True, help="Входной CSV файл"
    )
    csv_to_json_parser.add_argument(
        "--out", dest="output_file", required=True, help="Выходной JSON файл"
    )

    csv_to_xlsx_parser = subparsers.add_parser(
        "csv2xlsx", help="Конвертировать CSV в XLSX"
    )
    csv_to_xlsx_parser.add_argument(
        "--in", dest="input_file", required=True, help="Входной CSV файл"
    )
    csv_to_xlsx_parser.add_argument(
        "--out", dest="output_file", required=True, help="Выходной XLSX файл"
    )

    args = parser.parse_args()

    if args.command == "json2csv":
        json_to_csv(args.input_file, args.output_file)
    elif args.command == "csv2json":
        csv_to_json(args.input_file, args.output_file)
    elif args.command == "csv2xlsx":
        csv_to_xlsx(args.input_file, args.output_file)


if __name__ == "__main__":
    main()
