import argparse


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
    parser = argparse.ArgumentParser(
        description="A Python CLI that helps you preview your datasets"
    )

    # subparser object
    subparser = parser.add_subparsers(
        title="commands",
        dest="command"
    )

    # subparser and arg for filepath
    file_parser = subparser.add_parser(
        name="filepath",
        description="filepath of dataset",
        help="filepath of dataset"
    )
    file_parser.add_argument(
        "-f", "--filepath",
        required=True,
        dest="filepath",
        help="filepath of dataset")

    # subparser and arg for search
    search_parser = subparser.add_parser(
        name="search",
        description="Search for matching results based on field and value",
        help="Search for matching results based on field and value"
    )
    search_parser.add_argument(
        "-s", "--search",
        nargs=2,
        dest="search",
        default=False,
        help="Search for matching results based on field and value")

    # subparser and arg for listing fields
    field_parser = subparser.add_parser(
        name="list",
        description="Returns list of fields available for filtration",
        help="Returns list of fields available for filtration"
    )
    field_parser.add_argument(
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
