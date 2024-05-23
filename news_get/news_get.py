import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time
import random

# 基本配置
base_url = "http://mrxwlb.com/"
output_dir = "../News_Database"
days_to_fetch = 30
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"

# 创建存储文件的目录
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 获取指定日期的新闻内容
def fetch_news_for_date(date):
    year = date.year
    month = date.month
    day = date.day
    chinese_date = date.strftime("%Y年%m月%d日")
    url = f"{base_url}{year}/{month}/{day}/{chinese_date}新闻联播文字版/"
    headers = {"User-Agent": user_agent}
    print(f"Fetching news from URL: {url}")  # Debug: print the URL
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        content_div = soup.find('div', class_='entry-content')
        if content_div:
            return content_div.get_text(strip=True)
    else:
        print(f"Error: Received status code {response.status_code} for URL: {url}")  # Debug: print the status code
        print(f"Response content: {response.content.decode('utf-8')}")  # Debug: print the response content
    return None

# 保存新闻内容到文件
def save_news(date, content):
    file_name = date.strftime("%Y-%m-%d") + ".txt"
    file_path = os.path.join(output_dir, file_name)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# 爬取最近30天的新闻
current_date = datetime.now()
for i in range(days_to_fetch):
    target_date = current_date - timedelta(days=i)
    news_content = fetch_news_for_date(target_date)
    if news_content:
        save_news(target_date, news_content)
        print(f"Saved news for {target_date.strftime('%Y-%m-%d')}")
    else:
        print(f"No news found for {target_date.strftime('%Y-%m-%d')}")
    # 增加随机间隔以避免被检测为爬虫
    time.sleep(random.uniform(1, 3))

print("News fetching completed.")
