import os
import jieba


class DocumentProcessor:
    def __init__(self, directory, stop_words_path):
        self.directory = directory
        self.stop_words = self.load_stop_words(stop_words_path)
        self.documents = []
        self.doc_names = {}

    def load_stop_words(self, stop_words_path):
        """
        加载停用词列表。
        :param stop_words_path: 停用词列表文件路径
        :return: 停用词列表
        """
        stop_words = []
        if stop_words_path:
            with open(stop_words_path, 'r', encoding='utf-8') as file:
                for line in file:
                    stop_words.extend(line.strip())
        return stop_words

    def load_documents(self):
        """
        加载目录中的所有TXT文档。
        """
        for doc_id, filename in enumerate(os.listdir(self.directory)):
            if filename.endswith('.txt'):
                filepath = os.path.join(self.directory, filename)
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.documents.append(content)
                    self.doc_names[doc_id] = filename  # 保存文档名

    def preprocess_documents(self):
        processed_documents = []
        for doc in self.documents:
            # 使用结巴分词进行中文分词
            words = jieba.cut(doc)
            # 去除停用词和非字母字符
            filtered_words = [word for word in words if word.isalpha() and word not in self.stop_words]
            processed_documents.append(' '.join(filtered_words))
        self.documents = processed_documents