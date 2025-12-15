# main.py
# Nexus 2RedBeans Scraper Entry Point

import requests
from bs4 import BeautifulSoup
import config
import parser
import utils

def fetch_page(page_num):
    """请求单页数据"""
    # 2RedBeans 翻页通常是 ?page=X
    url = f"{config.BASE_URL}?page={page_num}"
    utils.log(f"Fetching page {page_num}...")
    
    try:
        response = requests.get(url, headers=config.HEADERS, timeout=15)
        if response.status_code == 200:
            return response.text
        else:
            utils.log(f"Error: Status code {response.status_code}")
            return None
    except Exception as e:
        utils.log(f"Request failed: {e}")
        return None

def run():
    utils.log("Starting Nexus Scraper Task...")
    
    # 检查是否配置了 Cookie
    if "YOUR_COOKIE_HERE" in config.HEADERS['Cookie']:
        utils.log("WARNING: Please set your Cookie in config.py first!")
        return

    for page in range(config.START_PAGE, config.MAX_PAGE + 1):
        html = fetch_page(page)
        
        if html:
            soup = BeautifulSoup(html, 'html.parser')
            
            # 定位所有用户卡片
            # 根据提供的HTML，class 是 "SearchResult__user"
            cards = soup.find_all('div', class_='SearchResult__user')
            
            if not cards:
                utils.log("No user cards found. Maybe cookie expired or end of list.")
                break
                
            page_data = []
            for card in cards:
                try:
                    user_info = parser.parse_user_card(card)
                    page_data.append(user_info)
                except Exception as e:
                    utils.log(f"Parse error: {e}")
            
            # 保存数据
            if page_data:
                utils.save_to_csv(page_data, config.OUTPUT_FILE)
                utils.log(f"Page {page} done. Got {len(page_data)} users.")
            
        # 翻页随机延迟
        utils.random_sleep()

    utils.log("Task Completed.")
    utils.log("Remember to verify data quality with Xunfang Standards.")

if __name__ == "__main__":
    run()