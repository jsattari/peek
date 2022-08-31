#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from typing import Dict
from rich.console import Console
from rich.table import Table

console = Console()


def make_table(data: list) -> object:
    if len(data) < 1:
        raise Exception("No data available")

    elif isinstance(data[0], str):
        table = Table("List of fields available for search")
        for value in data:
            table.add_row(value, style="red")

        console.print(table)

    elif isinstance(data[0], Dict):
        for dict in data:

            table = Table()
            table.add_column("field")
            table.add_column("values")

            for key, value in dict.items():
                table.add_row(key, value, style="red")
            console.print(table)

    else:
        raise Exception("Incorrect data type applied")
