#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import argparse
import csv
from rich import *
import pathlib


def data_filter(data: list, field: str, filter_value: str) -> list:
    """
    Filter data by choice of field and desired value

    Values:
        data (list):            dataset that will be filtered
        field (str):            field that will be used as basis for filtration
        filter_value (str):     value that will be used as the filter

    Return (list):              a list of dicts filtered by the desired value
    """

    return [dictionary for dictionary in data if dictionary[field] == filter_value]


def list_of_units(data: list) -> list:
    """
    Provides a list of available fields within a csv

    Values:
        data (list):    dataset that will contain list of fields

    Return (list):      a list of fields from dataset
    """

    return [key for key in data[0].keys()]


file_path = pathlib.Path("peek-app")

file_to_open = file_path / "cups.csv"

with open(file_to_open, "r") as file:
    reader = csv.DictReader(file)
    data_dict = [{key: value for key, value in row.items()} for row in reader]

print(list_of_units(data_dict))
