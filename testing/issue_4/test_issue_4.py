import pytest
from issue_4 import fit_transform

expected = [
    ("apple", [0, 0, 1]),
    ("banana", [0, 1, 0]),
    ("apple", [0, 0, 1]),
    ("cherry", [1, 0, 0]),
]


def test_list_input():
    result = fit_transform(["apple", "banana", "apple", "cherry"])
    assert result == expected


def test_strs_input():
    result = fit_transform("apple", "banana", "apple", "cherry")
    assert result == expected


def test_no_arguments_raises():
    with pytest.raises(TypeError):
        fit_transform()


def test_repeated_categories():
    result = fit_transform("apple", "banana", "apple", "cherry")
    assert ("banana", [0, 1, 0]) in result
    assert len(result) == 4
