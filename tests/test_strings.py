from problems.strings import hollow_box, format_report, snake_to_camel

def test_hollow_box_basic():
    assert hollow_box(4, 3) == "****\n*  *\n****"

def test_hollow_box_edge():
    assert hollow_box(1, 1) == "*"

def test_format_report_basic():
    assert format_report("Zinhle", 45, 50) == "Zinhle: 45/50 (90%)"

def test_format_report_zero():
    assert format_report("A", 0, 10) == "A: 0/10 (0%)"

def test_snake_to_camel_basic():
    assert snake_to_camel("hello_world_test") == "helloWorldTest"

def test_snake_to_camel_single():
    assert snake_to_camel("hello") == "hello"
