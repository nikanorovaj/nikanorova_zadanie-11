from collections import Counter
import math

class TextProcessor:
    STOPWORDS = set([
        'a', 'an', 'and', 'are', 'as', 'at', 'be', 'but', 'by',
        'for', 'if', 'in', 'into', 'is', 'it', 'no', 'not', 'of',
        'on', 'or', 'such', 'that', 'the', 'their', 'then', 'there',
        'these', 'they', 'this', 'to', 'was', 'will', 'with'
    ])

    def __init__(self, docs):
        self.docs = [doc.lower().split() for doc in docs]
        self.doc_count = len(self.docs)
        self.word_in_docs = Counter()
        for doc in self.docs:
            unique_words = set(doc)
            self.word_in_docs.update(unique_words)

    def get_tf(self, word, doc_index):
        words = self.docs[doc_index]
        return words.count(word.lower()) / len(words) if len(words) > 0 else 0

    def get_idf(self, word, doc_index=None):
        word = word.lower()
        count = self.word_in_docs.get(word, 0)
        return math.log(self.doc_count / (count + 1)) if count else 0

    def get_tf_idf(self, word, doc_index, ignore_stopwords=True):
        word = word.lower()
        if ignore_stopwords and word in self.STOPWORDS:
            return 0
        tf = self.get_tf(word, doc_index)
        idf = self.get_idf(word, doc_index)
        return tf * idf