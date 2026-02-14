from problems.data_structures import invert_social_graph, flatten_once, group_by_length

def test_invert_social_graph_basic():
    data = {
        "alice": ["bob", "claire"],
        "bob": ["claire"]
    }

    assert invert_social_graph(data) == {
        "bob": ["alice"],
        "claire": ["alice", "bob"]
    }

def test_flatten_once():
    assert flatten_once([1, [2,3], [4], 5]) == [1,2,3,4,5]

def test_group_by_length():
    assert group_by_length(["hi", "cat", "dog", "a"]) == {
        2: ["hi"],
        3: ["cat", "dog"],
        1: ["a"]
    }
