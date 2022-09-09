from cli.args import create_parser, get_args


def test_no_flags():
    parser = create_parser(["-f", "/Users/johnsattari/peek/cups.csv", "-hd"])
    [data, flags, fields] = get_args(parser)
    assert [data, flags, fields] == [
        "/Users/johnsattari/peek/cups.csv", "head", True]
