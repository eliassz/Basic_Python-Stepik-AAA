from issue_2 import decode


def test_decode():
    assert decode('..-. --- ---') == 'FOO'
    assert decode('-... .- --..') == 'BAZ'
    assert decode('-... .- .-.') == 'BAR'


if __name__ == "__main__":
    test_decode()
    print("All tests passed!")
