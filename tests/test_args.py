from cli.args import create_parser, get_args


def test_no_flags():
    parser = create_parser(["-f", "/Users/johnsattari/peek/cups.csv"])
    [data, flags, fields] = get_args(parser)
    assert [data, flags, fields] == [
        "/Users/johnsattari/peek/cups.csv", "head", True]


def test_no_flags_txt():
    parser = create_parser(["-f", "/Users/johnsattari/peek/cups.txt"])
    [data, flags, fields] = get_args(parser)
    assert [data, flags, fields] == [
        "/Users/johnsattari/peek/cups.txt", "head", True]


def test_search():
    parser = create_parser(
        ["-f", "/Users/johnsattari/peek/cups.csv", "-s", "host", "france"])
    [data, flags, fields] = get_args(parser)
    assert [data, flags, fields] == [
        "/Users/johnsattari/peek/cups.csv", "search", ["host", "france"]]


def test_list():
    parser = create_parser(["-f", "/Users/johnsattari/peek/cups.csv", "-l"])
    [data, flags, fields] = get_args(parser)
    assert [data, flags, fields] == [
        "/Users/johnsattari/peek/cups.csv", "list", True]


def test_head():
    parser = create_parser(["-f", "/Users/johnsattari/peek/cups.csv", "-hd"])
    [data, flags, fields] = get_args(parser)
    assert [data, flags, fields] == [
        "/Users/johnsattari/peek/cups.csv", "head", True]


def test_tail():
    parser = create_parser(["-f", "/Users/johnsattari/peek/cups.csv", "-t"])
    [data, flags, fields] = get_args(parser)
    assert [data, flags, fields] == [
        "/Users/johnsattari/peek/cups.csv", "tail", True]
