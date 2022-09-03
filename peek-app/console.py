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
        table = Table(show_edge=True, show_header=True,
                      show_lines=True, header_style="bold")

        for col in list(data[0].keys()):
            table.add_column(col, style="green",
                             justify="right", no_wrap=False,
                             min_width=10)

        for blob in data:
            table.add_row(*blob.values(), style="red")

        console.print(table)

    else:
        raise Exception("Incorrect data type applied")
