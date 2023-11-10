import pytest
from issue_2 import decode


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (
            "..-. --- ---",
            "FOO",
        ),
        (
            "-... .- --..",
            "BAZ",
        ),
        ("-... .- .-.", "BAR"),
    ],
)
def test_decode(input_data, expected):
    assert decode(input_data) == expected
