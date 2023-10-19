class CountVectorizer:

    def _tokenize(self, corpus):
        self.tokenized_corpus = []
        self.tokenized_text = []
        for text in corpus:
            tokens = text.lower().split()
            self.tokenized_text.append(tokens)
            self.tokenized_corpus.extend(tokens)

    def _set_feature_names(self):
        self.dict_counter = {}
        for el in self.tokenized_corpus:
            self.dict_counter[el] = self.dict_counter.get(el, 0) + 1
        self.feature_names = list(self.dict_counter.keys())

    def fit_transform(self, corpus):
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

    def get_feature_names(self):
        return self.feature_names


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
