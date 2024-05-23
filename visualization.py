import matplotlib.pyplot as plt
from wordcloud import WordCloud
import matplotlib.font_manager as fm


def visualize_wordcloud(documents, font_path):
    """
    生成文档集的词云。
    """
    text = ' '.join(documents)
    wordcloud = WordCloud(font_path=font_path, background_color='white').generate(text)
    plt.figure(figsize=(10, 7))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()


def visualize_top_words(vectorizer, term_document_matrix, top_n, font_path):
    """
    可视化最常见的top_n个词项及其频率。
    """
    sum_words = term_document_matrix.sum(axis=0)
    words_freq = [(word, sum_words[0, idx]) for word, idx in vectorizer.vocabulary_.items()]
    words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)[:top_n]
    words, freqs = zip(*words_freq)

    # 加载中文字体
    prop = fm.FontProperties(fname=font_path)

    plt.figure(figsize=(10, 8))
    plt.bar(words, freqs)
    plt.xticks(rotation=45, fontproperties=prop)
    plt.xlabel('Words', fontproperties=prop)
    plt.ylabel('Frequency', fontproperties=prop)
    plt.title('Top Words Frequency', fontproperties=prop)
    plt.show()


def visualize_inverted_index(inverted_index):
    """
    可视化倒排索引表。
    """
    print("倒排索引：")
    for term, doc_ids in sorted(inverted_index.items()):
        print(f"词项 '{term}': 文档列表 {doc_ids}")

