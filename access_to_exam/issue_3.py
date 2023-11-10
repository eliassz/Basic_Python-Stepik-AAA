import math

from typing import List


def idf_transform(count_matrix: List[List[int]]) -> List[float]:
    """
    Calculate the inverse document frequency (IDF) for each term.

    IDF is computed as the logarithm of the number of documents divided
    by the number of documents that contain each term, adjusted
    and rounded to one decimal place.

    :param count_matrix: A matrix where each row represents a document
    and each column a term frequency.
    :return: A list of IDF values for each term.
    """
    n_docs = len(count_matrix)
    docs_with_words = [0] * len(count_matrix[0])
    idf_transformation = []

    for doc in count_matrix:
        for index, count in enumerate(doc):
            if doc[index] != 0:
                docs_with_words[index] += 1

    for el in docs_with_words:
        res = round(math.log((n_docs + 1) / (el + 1)) + 1, 1)
        idf_transformation.append(res)

    return idf_transformation


if __name__ == '__main__':
    count_matrix = [
        [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    ]
    idf_matrix = idf_transform(count_matrix)

    check_idf_matrix = [
        1.4, 1.4, 1.0, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4
    ]

    assert idf_matrix == check_idf_matrix

    print(idf_matrix)
