from document_processor import DocumentProcessor
from search_engine import SearchEngine
import visualization as viz
import config

if __name__ == '__main__':
    # 初始化文档处理器和搜索引擎
    doc_processor = DocumentProcessor(config.DIRECTORY, config.STOP_WORDS_PATH)
    search_engine = SearchEngine(stop_words=doc_processor.stop_words)

    # 加载和预处理文档
    doc_processor.load_documents()
    doc_processor.preprocess_documents()

    # 构建TF-IDF矩阵和倒排索引
    search_engine.build_term_document_matrix(doc_processor.documents, list(doc_processor.doc_names.values()))
    search_engine.build_inverted_index(doc_processor.documents)

    # 交互式查询
    while True:
        print("\n菜单:")
        print("1. 生成词云            2. 可视化最常见的30个词项及其频率")
        print("3. 可视化倒排索引       4. 进行查询         5. 退出")
        choice = input("请选择一个操作: ")

        if choice == '1':
            viz.visualize_wordcloud(doc_processor.documents, config.FONT_PATH)  # 生成词云
        elif choice == '2':
            viz.visualize_top_words(search_engine.vectorizer, search_engine.term_document_matrix, 30, config.FONT_PATH)  # 可视化最常见的词项及其频率
        elif choice == '3':
            viz.visualize_inverted_index(search_engine.inverted_index)   # 可视化倒排索引
        elif choice == '4':
            use_boolean_search = input("是否使用布尔查询（AND 操作）? (y/n): ").strip().lower() == 'y'
            query = input("请输入查询词 : ")
            results = search_engine.search(query, use_boolean_search)
            if results:
                if use_boolean_search:
                    print(f"找到了 {len(results)} 个包含查询词 '{query}' 的文档：")
                    for i, doc_name in enumerate(results, 1):
                        print(f"{doc_name}", end='\t')
                        if i % 4 == 0:  # 每四个结果换行
                            print()
                    if len(results) % 4 != 0:  # 如果结果数量不是4的倍数，需要手动换行
                        print()
                else:
                    print(f"找到了 {len(results)} 个包含查询词 '{query}' 的文档：")
                    for i, (doc_name, score) in enumerate(results, 1):
                        print(f"{doc_name} (评分: {score:.4f})", end='\t')
                        if i % 4 == 0:  # 每四个结果换行
                            print()
                    if len(results) % 4 != 0:  # 如果结果数量不是4的倍数，需要手动换行
                        print()
            else:
                print(f"抱歉，没有找到包含查询词 '{query}' 的文档。")
            print()
        elif choice == '5':
            print("欢迎下次使用！！！")
            break
        else:
            print("无效的选择，请重新输入。")

