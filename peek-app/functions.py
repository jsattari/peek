#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import argparse


def search(*args) -> list:
    """
    Filter data by choice of field and desired value

    Values:
        data (list):            dataset that will be filtered
        field (str):            field that will be used as basis for filtration
        filter_value (str):     value that will be used as the filter

    Return (list):              a list of dicts filtered by the desired value
    """

    try:
        output = []
        for struct in args[0]:
            if struct[args[1][0]].lower() == args[1][1].lower():
                output.append(struct)

        if len(output) == 0:
            return [-1]

        else:
            return output
    except Exception:
        return "Error: Unable to complete action"


def list_of_fields(*args) -> list:
    """
    Provides a list of available fields within a csv

    Values:
        data (list):    dataset that will contain list of fields

    Return (list):      a list of fields from dataset
    """

    return [key for key in args[0][0].keys()]


def head(*args) -> list:
    """
    Returns the first 5 or last 5 rows of data as a preview

    Values:
        data (list):        dataset for preview

    Return (list):          list of first 5 rows of dataset
    """

    return args[0][:5]


def tail(*args) -> list:
    """
    Returns the first 5 or last 5 rows of data as a preview

    Values:
        data (list):        dataset for preview

    Return (list):          list of first 5 rows of dataset
    """

    return args[0][-5:]


def get_args():
    """
    Parse console args and return three variables
    that contain commands, flags, and additional args

    Values:
        None:           Accepts inputs and returns values

    Return (list):      Three variables that contains the path to dataset,
                        flags, fields (if any)
    """

    # create parser object
    parser = argparse.ArgumentParser()

    # func for search
    parser.add_argument(
        "-f", "--filepath",
        required=True,
        dest="filepath",
        help="filepath of dataset")

    parser.add_argument(
        "-s", "--search",
        nargs=2,
        dest="search",
        default=False,
        help="Search for matching results based on field and value")

    # func for listing fields
    parser.add_argument(
        "-l", "--list",
        dest="list",
        action="store_true",
        default=False,
        help="Returns list of fields available for filtration"
    )

    # func for head of data
    parser.add_argument(
        "-hd", "--head",
        dest="head",
        action="store_true",
        default=False,
        help="Shows preview of first 5 rows of dataset"
    )

    # func for tail of data
    parser.add_argument(
        "-t", "--tail",
        dest="tail",
        action="store_true",
        default=False,
        help="Shows preview of last 5 rows of dataset"
    )

    # gather arguments and flags into variables
    args = parser.parse_args()
    data = args.filepath
    commands = [tup for tup in list(
        vars(args).items())[1:] if tup[1] is not False][0]
    flags = commands[0]
    fields = commands[1]

    return data, commands, flags, fields
