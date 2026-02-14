from problems.algorithms import recursive_max, is_balanced, two_sum

def test_recursive_max_basic():
    assert recursive_max([1, 9, 3, 7]) == 9

def test_recursive_max_empty():
    assert recursive_max([]) is None

def test_is_balanced_true():
    assert is_balanced("(())()") is True

def test_is_balanced_false():
    assert is_balanced("(()") is False

def test_two_sum_basic():
    assert two_sum([2,7,11,15], 9) == (0,1)

def test_two_sum_not_found():
    assert two_sum([1,2,3], 7) is None
