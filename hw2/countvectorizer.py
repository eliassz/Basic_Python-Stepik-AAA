from typing import Dict, List

import warnings


class CountVectorizer:
    """
    Convert a collection of text documents to a matrix of token counts.
    """
    def __init__(self):
        self.tokenized_corpus = []
        self.tokenized_text = []
        self.feature_names = []

    def _tokenize(self, corpus: List[str]) -> None:
        """
        Tokenize the given corpus.

        Args:
            corpus: A list of text documents.
        """
        for text in corpus:
            tokens = text.lower().split()
            self.tokenized_text.append(tokens)
            self.tokenized_corpus.extend(tokens)

    def _set_feature_names(self) -> None:
        """
        Create a dictionary counter and set the feature names for the corpus.
        """
        self.dict_counter: Dict[str, int] = {}
        for el in self.tokenized_corpus:
            self.dict_counter[el] = self.dict_counter.get(el, 0) + 1
        self.feature_names = list(self.dict_counter.keys())

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        """
        Learn the vocabulary dictionary and return document-term matrix.

        Args:
            corpus: A list of text documents.

        Returns:
            The document-term matrix.
        """
        self._tokenize(corpus)
        self._set_feature_names()
        output = []
        for i in range(len(corpus)):
            tmp = []
            tokenized_text = self.tokenized_text[i]
            for token in self.feature_names:
                tmp.append(tokenized_text.count(token))
            output.append(tmp)
        return output

    def get_feature_names(self) -> List[str]:
        """
        Get feature names (i.e. tokens) for the vectorizer.

        Returns:
            A list of feature names.
        """
        if self.feature_names:
            return self.feature_names
        warnings.warn("Return None if fit_transform method isn't used.")
        return None


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus=corpus)
    names = vectorizer.get_feature_names()

    check_feature_names = [
        'crock', 'pot', 'pasta', 'never',
        'boil', 'again', 'pomodoro', 'fresh',
        'ingredients', 'parmesan', 'to', 'taste'
    ]
    check_count_matrix = [
        [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    ]

    assert names == check_feature_names
    assert count_matrix == check_count_matrix

    print(f'count matrix : {count_matrix}')
    print(f'feature names: {names}')
