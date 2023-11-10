import math
from typing import List

from issue_1 import CountVectorizer


class TfidfVectorizer(CountVectorizer):
    """
    A class to perform TF-IDF transformation on a term count matrix.

    This class takes a matrix where each row represents a document
    and each column a term frequency count
    It provides methods to transform this matrix into a term frequency (TF)
    matrix and then inverse document frequency (IDF) transformation
    to compute the TF-IDF matrix.
    """

    def __init__(self):
        """
        Initialize the TfidfTransformer with empty TF and IDF matrices.
        """
        super().__init__()
        self.tf_matrix = None
        self.idf_matrix = None

    def _tf_transform(self, count_matrix: List[List[int]]) -> None:
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
        self.tf_matrix = count_matrix

    def _idf_transform(self, count_matrix: List[List[int]]) -> None:
        """
        Calculate the inverse document frequency (IDF) for each term.

        IDF is computed as the logarithm of the number
        of documents divided by the number of documents that contain each term,
        adjusted and rounded to one decimal place.

        :param count_matrix: A matrix where each row represents a document
        and each column a term frequency.
        :return: A list of IDF values for each term.
        """
        n_docs = len(count_matrix)
        docs_with_words = [0] * len(count_matrix[0])
        idf_transformation = []

        for doc in count_matrix:
            for index, _ in enumerate(doc):
                if doc[index] != 0:
                    docs_with_words[index] += 1

        for el in docs_with_words:
            res = round(math.log((n_docs + 1) / (el + 1)) + 1, 1)
            idf_transformation.append(res)

        self.idf_matrix = idf_transformation

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        """
        Perform TF-IDF transformation on the given count matrix.

        This method applies term frequency transformation followed by
        inverse document frequency transformation
        to compute the TF-IDF matrix.

        :param count_matrix: Matrix of term counts for each document.
        :return: TF-IDF matrix.
        """
        count_matrix = super().fit_transform(corpus)
        self._tf_transform(count_matrix)
        self._idf_transform(count_matrix)
        return [
            [
                round(tf_value * idf_value, 3)
                for tf_value, idf_value in zip(tf_row, self.idf_matrix)
            ]
            for tf_row in self.tf_matrix
        ]


if __name__ == "__main__":
    corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste",
    ]

    transformer = TfidfVectorizer()
    tfidf_matrix = transformer.fit_transform(corpus)

    check_tfidf_matrix = [
        [0.2, 0.2, 0.286, 0.2, 0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.143, 0.0, 0.0, 0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
    ]

    assert tfidf_matrix == check_tfidf_matrix

    print(f"tf-idf matrix : {tfidf_matrix}")
