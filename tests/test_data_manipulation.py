from problems.data_manipulation import normalize_scores, merge_records, top_student

def test_normalize_scores_basic():
    scores = {"A": 50, "B": 100}
    assert normalize_scores(scores) == {"A": 0.5, "B": 1.0}

def test_normalize_scores_empty():
    assert normalize_scores({}) == {}

def test_merge_records_basic():
    a = [{"id": 1, "name": "A"}, {"id": 2, "name": "B"}]
    b = [{"id": 2, "score": 80}, {"id": 3, "score": 90}]
    assert merge_records(a, b) == [
        {"id": 1, "name": "A"},
        {"id": 2, "name": "B", "score": 80},
        {"id": 3, "score": 90}
    ]

def test_merge_records_empty():
    assert merge_records([], []) == []

def test_top_student_basic():
    records = [
        {"name": "A", "score": 70},
        {"name": "B", "score": 90},
        {"name": "C", "score": 80}
    ]
    assert top_student(records) == {"name": "B", "score": 90}

def test_top_student_empty():
    assert top_student([]) is None
