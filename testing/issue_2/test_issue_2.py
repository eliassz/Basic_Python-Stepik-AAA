import pytest
from issue_2 import decode


@pytest.mark.parametrize("input_data, expected", [
    (
        '..-. --- ---',
        'FOO',
    ),
    (
        '-... .- --..',
        'BAZ',
    ),
    (
        '-... .- .-.',
        'BAR'
    )
])
def test_decode(input_data, expected):
    assert decode(input_data) == expected


if __name__ == "__main__":
    test_decode()
    print("All tests passed!")
