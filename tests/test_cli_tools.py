from problems.cli_tools import parse_flags, format_help

def test_parse_flags_basic():
    args = ["--name=Zinhle", "--age=22", "--debug"]
    assert parse_flags(args) == {
        "name": "Zinhle",
        "age": "22",
        "debug": True
    }

def test_format_help_basic():
    flags = {"name": "Your name", "age": "Your age"}
    result = format_help("register", flags)
    assert result == "Usage: register --name=<Your name> --age=<Your age>"
