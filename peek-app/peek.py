#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import csv
import console
import functions as f


def main():

    # function map for flags
    FUNCTION_MAP = {
        "search": f.search,
        "list": f.list_of_fields,
        "head": f.head,
        "tail": f.tail
    }

    # get arguments
    data, commands, flags, fields = f.get_args()

    # open file
    with open(data, "r") as file:
        reader = csv.DictReader(file)
        data_dict = [{key: value for key, value in row.items()}
                     for row in reader]

    # map function based on flags applied in console
    func = FUNCTION_MAP[flags]

    # pretty print out data that is returned
    if isinstance(commands[1], bool):
        console.make_table(func(data_dict))
    else:
        console.make_table(func(data_dict, fields))


if __name__ == "__main__":
    main()
