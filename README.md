# 新闻联播信息检索系统

## 概览

本项目实现了一个新闻联播信息检索系统，该系统能够爬取指定日期内的新闻联播文字稿，构建词项-文档矩阵，建立倒排索引。系统支持交互式查询，允许用户使用布尔查询（AND OR NOT）和向量空间模型搜索特定词汇并获取包含这些词汇的文档名称。

## 功能

- **信息获取**：爬取新闻联播文字稿并保存本地
- **文档处理**：加载和预处理文本文档，包括分词和去除停用词。
- **词项-文档矩阵**：使用TF-IDF向量化方法构建词项-文档矩阵。
- **倒排索引**：建立倒排索引，将词汇映射到文档。
- **交互式查询**：提供交互式命令行界面进行文档集合的查询。
- **可视化**：生成词云、可视化高频词汇、打印倒排索引表。

## 项目结构
```commandline
 ---Information-Retrieval-System\
    |----__init__.py
    |----news_get\       
    |    |----news_get.py       // 信息获取
    |    |----__init__.py
    |----main.py                // 主函数
    |----document_processor.py  // 文档处理
    |----search_engine.py       // 索引和检索
    |----visualization.py       // 可视化
    |----config.py              // 路径配置文件
    |----News_Database\         // 数据库
    |    |----2024-04-22.txt
    |    |----2024-04-23.txt
    |    |----......
    |    |----2024-05-20.txt
    |    |----2024-05-21.txt
    |    |----2024-05-22.txt
    |----requirements.txt       // 项目配置
    |----stop_words.txt         // 停用词
    |----README.md              // README文件
```
## 安装

1. 克隆仓库：
   ```bash
   git clone https://github.com/xuanls/Information-Retrieval-System.git
   ```

2. 进入项目目录：
   ```bash
   cd Information-Retrieval-System
   ```

3. 安装所需包：
   ```bash
   pip install -r requirements.txt
   ```

## 使用方法

1. 运行`news_get.py`以获取数据集。
2. 运行`main.py`以加载文档，构建词项-文档矩阵和倒排索引：
   ```bash
   python main.py
   ```

3. 使用交互式查询界面搜索词汇：
   ```bash
   # 示例查询
   菜单:
   1. 生成词云            2. 可视化最常见的30个词项及其频率
   3. 可视化倒排索引       4. 进行查询         5. 退出
   请选择一个操作: 4
   是否使用布尔查询（AND 操作）? (y/n): y
   请输入查询词 : 发展 NOT 美国 AND 假期 OR 塞尔维亚
   找到了 15 个包含查询词 '发展 NOT 美国 AND 假期 OR 塞尔维亚' 的文档：
   2024-04-25.txt	2024-04-29.txt	2024-04-30.txt	2024-05-01.txt	
   2024-05-02.txt	2024-05-03.txt	2024-05-04.txt	2024-05-05.txt	
   2024-05-06.txt	2024-05-07.txt	2024-05-08.txt	2024-05-09.txt	
   2024-05-11.txt	2024-05-19.txt	2024-05-22.txt	
      ```


## 许可证

本项目基于MIT许可证 - 详情请见[LICENSE](LICENSE)文件。

## 联系

如有问题或反馈，请联系[2693652020@qq.com](mailto:你的邮箱@example.com)。

