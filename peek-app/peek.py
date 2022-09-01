#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import argparse
import csv
import pathlib
import console


def data_filter(data: list, values: list) -> list:
    """
    Filter data by choice of field and desired value

    Values:
        data (list):            dataset that will be filtered
        field (str):            field that will be used as basis for filtration
        filter_value (str):     value that will be used as the filter

    Return (list):              a list of dicts filtered by the desired value
    """

    return [
        dictionary for dictionary in data
        if dictionary[values[0]] == values[1].capitalize()]


def list_of_fields(data: list) -> list:
    """
    Provides a list of available fields within a csv

    Values:
        data (list):    dataset that will contain list of fields

    Return (list):      a list of fields from dataset
    """

    return [key for key in data[0].keys()]


def main():

    file_path = pathlib.Path("peek-app")

    file_to_open = file_path / "cups.csv"

    with open(file_to_open, "r") as file:
        reader = csv.DictReader(file)
        data_dict = [{key: value for key, value in row.items()}
                     for row in reader]

    # function map for flags
    FUNCTION_MAP = {
        "search": data_filter,
        "list": list_of_fields
    }

    # create parser object
    parser = argparse.ArgumentParser()

    # add arguments
    parser.add_argument(
        "-s", "--search",
        type=str,
        nargs=2,
        help="Search for matching results based on field and value")

    parser.add_argument(
        "-l", "--list",
        nargs=0,
        help="Returns list of fields available for filtration"
    )

    args = parser.parse_args()
    fields = list(vars(args).values())[0]
    flags = list(vars(args).keys())[0]

    func = FUNCTION_MAP[flags]
    # print(func(data_dict, fields))

    console.make_table(func(data_dict, fields))


if __name__ == "__main__":
    main()
