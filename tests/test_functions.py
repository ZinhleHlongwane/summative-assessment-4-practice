from problems.functions import apply_twice, safe_divide, unpack_stats

def test_apply_twice_basic():
    assert apply_twice(lambda x: x + 1, 3) == 5

def test_apply_twice_string():
    assert apply_twice(lambda x: x * 2, "a") == "aaaa"

def test_safe_divide_basic():
    assert safe_divide(10, 2) == 5

def test_safe_divide_zero():
    assert safe_divide(5, 0) is None

def test_unpack_stats_basic():
    assert unpack_stats([1, 2, 3, 4]) == (1, 4, 10)

def test_unpack_stats_single():
    assert unpack_stats([5]) == (5, 5, 5)

def test_unpack_stats_empty():
    assert unpack_stats([]) is None
