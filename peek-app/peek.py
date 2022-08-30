import argparse
import csv
from rich import *
import pathlib


def data_filter(data: list, field: str, filter_value: str) -> list:
    """Filter data by choice of field and desired value

    :param data: list - dataset that will be filtered
    :param field: str - field that will be used as basis for filtration
    :param filter_value: str - value that will be used as the filter
    :return: list - a list of dicts filtered by the desired value
    """

    return [dictionary for dictionary in data if dictionary[field] == filter_value]


file_path = pathlib.Path("peek-app")

file_to_open = file_path / "cups.csv"

with open(file_to_open, "r") as file:
    reader = csv.DictReader(file)
    data_dict = [{key: value for key, value in row.items()} for row in reader]

print(data_filter(data_dict, "winner", "Italy"))
