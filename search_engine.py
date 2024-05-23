from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from collections import defaultdict


class SearchEngine:
    def __init__(self, stop_words):
        self.vectorizer = TfidfVectorizer(stop_words=stop_words)
        self.term_document_matrix = None
        self.inverted_index = defaultdict(set)
        self.doc_names = []

    def build_term_document_matrix(self, documents, doc_names):
        """
        构建词项——文档矩阵
        """
        self.term_document_matrix = self.vectorizer.fit_transform(documents)
        self.doc_names = doc_names

    def build_inverted_index(self, documents):
        """
        构建倒排索引
        """
        for doc_id, doc in enumerate(documents):
            for word in doc.split():
                self.inverted_index[word].add(doc_id)

    def search(self, query, use_boolean_search=False):
        if use_boolean_search:
            # 解析布尔查询
            query_parts = query.split()
            result_docs = None
            current_operator = None

            for part in query_parts:
                if part in ['AND', 'OR', 'NOT']:
                    current_operator = part
                else:
                    term_docs = set(self.inverted_index.get(part, []))
                    if result_docs is None:
                        result_docs = term_docs
                    else:
                        if current_operator == 'OR':
                            result_docs |= term_docs
                        elif current_operator == 'NOT':
                            result_docs -= term_docs
                        else:  # Default is AND
                            result_docs &= term_docs

            return [self.doc_names[doc_id] for doc_id in result_docs] if result_docs else []
        else:
            # 处理普通查询
            query_vector = self.vectorizer.transform([query])
            scores = (self.term_document_matrix * query_vector.T).toarray().flatten()
            results = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
            return [(self.doc_names[i], score) for i, score in results if score > 0]