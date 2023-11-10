from typing import List


def tf_transform(count_matrix: List[List[int]]) -> List[List[float]]:
    """
    Convert a matrix of term counts to term frequencies.

    Each term count is divided by the sum of terms in the sentence,
    ignoring zeros, and rounded to three decimals.

    :param count_matrix: Matrix of term counts for each sentence.
    :return: Matrix with term frequencies for each sentence.
    """
    for sentence in count_matrix:
        amount_words = sum([el for el in sentence if el != 0])
        for i in range(len(sentence)):
            sentence[i] = round(sentence[i] / amount_words, 3)
    return count_matrix


if __name__ == '__main__':
    count_matrix = [
        [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    ]
    tf_matrix = tf_transform(count_matrix)

    check_tf_matrix = [
        [
            0.143, 0.143, 0.286, 0.143, 0.143,
            0.143, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
        ],
        [
            0.0, 0.0, 0.143, 0.0, 0.0, 0.0, 0.143,
            0.143, 0.143, 0.143, 0.143, 0.143
        ],
    ]

    assert tf_matrix == check_tf_matrix

    print(tf_matrix)
