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


def get_args():
    """
    Parse console args and return three variables
    that contain commands, flags, and additional args

    Values:
        None:           Accepts inputs and returns values

    Return (list):      Three variables that
    """

    # create parser object
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s", "--search",
        nargs=2,
        dest="search",
        help="Search for matching results based on field and value")

    parser.add_argument(
        "-l", "--list",
        dest="list",
        action="store_true",
        help="Returns list of fields available for filtration"
    )

    # gather arguments and flags into variables
    args = parser.parse_args()
    commands = [tup for tup in list(
        vars(args).items()) if tup[1] is not None][0]
    flags = commands[0]
    fields = commands[1]

    return commands, flags, fields


def main():

    # function map for flags
    FUNCTION_MAP = {
        "search": data_filter,
        "list": list_of_fields
    }

    file_path = pathlib.Path("peek-app")

    file_to_open = file_path / "cups.csv"

    with open(file_to_open, "r") as file:
        reader = csv.DictReader(file)
        data_dict = [{key: value for key, value in row.items()}
                     for row in reader]

    # get arguments
    commands, flags, fields = get_args()

    # map function based on flags applied in console
    func = FUNCTION_MAP[flags]

    # pretty print out data that is returned
    if isinstance(commands[1], bool):
        console.make_table(func(data_dict))
    else:
        console.make_table(func(data_dict, fields))


if __name__ == "__main__":
    main()
