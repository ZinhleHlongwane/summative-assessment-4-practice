from problems.loops import staircase, count_vowels, reverse_every_k

def test_staircase_basic():
    assert staircase(4) == "#\n##\n###\n####"

def test_staircase_one():
    assert staircase(1) == "#"

def test_staircase_zero():
    assert staircase(0) == ""

def test_count_vowels_basic():
    assert count_vowels("hello") == 2

def test_count_vowels_caps():
    assert count_vowels("HELLO") == 2

def test_count_vowels_empty():
    assert count_vowels("") == 0

def test_reverse_every_k_basic():
    assert reverse_every_k("abcdef", 2) == "badcfe"

def test_reverse_every_k_three():
    assert reverse_every_k("abcdefgh", 3) == "cbafedhg"

def test_reverse_every_k_edge():
    assert reverse_every_k("abc", 10) == "cba"
