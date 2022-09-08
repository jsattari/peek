#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import csv
import console as con
import functions as funcs
from args import create_parser, get_args


def main():

    # function map for flags
    FUNCTION_MAP = {
        "search": funcs.search,
        "list": funcs.list_of_fields,
        "head": funcs.head,
        "tail": funcs.tail
    }

    # create parser
    # get arguments
    parser = create_parser()
    data, flags, fields = get_args(parser)

    # open file
    with open(data, "r") as file:
        reader = csv.DictReader(file)
        data_dict = [{key: value for key, value in row.items()}
                     for row in reader]

    # map function based on flags applied in console
    func = FUNCTION_MAP[flags]

    # pretty print out data that is returned
    if isinstance(fields, bool):
        results = func(data_dict)
        con.make_table(results)
    else:
        results = func(data_dict, fields)
        con.make_table(results)


if __name__ == "__main__":
    main()
