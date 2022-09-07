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

    # gather arguments and flags into variables
    args = parser.parse_args()
    data = args.filepath
    commands = [tup for tup in list(
        vars(args).items())[1:] if tup[1] is not False][0]
    flags = commands[0]
    fields = commands[1]
    print(data, commands, flags, fields, sep="\n")

    return data, commands, flags, fields
