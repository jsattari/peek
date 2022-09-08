import argparse


def create_parser():
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

    # arg and arg for filepath
    parser.add_argument(
        "-f", "--filepath",
        required=True,
        dest="filepath",
        help="filepath of dataset")

    # arg and arg for search
    parser.add_argument(
        "-s", "--search",
        nargs=2,
        dest="search",
        default=False,
        help="Search for matching results based on field and value")

    # arg for listing fields
    parser.add_argument(
        "-l", "--list",
        dest="list",
        action="store_true",
        default=False,
        help="Returns list of fields available for filtration"
    )

    # arg for head of data
    parser.add_argument(
        "-hd", "--head",
        dest="head",
        action="store_true",
        default=False,
        help="Shows preview of first 5 rows of dataset"
    )

    # arg for tail of data
    parser.add_argument(
        "-t", "--tail",
        dest="tail",
        action="store_true",
        default=False,
        help="Shows preview of last 5 rows of dataset"
    )

    return parser.parse_args()


def get_args(cli_args):

    # data should be the filepath to dataset
    data = cli_args.filepath

    # find which flags are active
    commands = [tup for tup in list(
        vars(cli_args).items())[1:] if tup[1] is not False]

    # separate flag and fields
    flags = commands[0][0]
    fields = commands[0][1]

    return data, flags, fields
