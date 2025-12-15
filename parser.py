# parser.py
# Nexus HTML Parser Module

from bs4 import BeautifulSoup
import re

def clean_text(text):
    """去除空白字符和换行"""
    if text:
        return text.replace('\n', ' ').strip()
    return ""

def extract_style_url(style_str):
    """从 background-image: url(...) 中提取链接"""
    if not style_str:
        return ""
    match = re.search(r'url\("?(.+?)"?\)', style_str)
    return match.group(1) if match else ""

def parse_user_card(html_card):
    """
    解析单个用户卡片 HTML
    """
    data = {}
    
    # 1. 提取主链接 (Profile URL)
    link_tag = html_card.find('a', class_='SearchResult__user__container')
    if link_tag:
        data['profile_url'] = link_tag.get('href')
    
    # 2. 提取头像 (Image)
    img_div = html_card.find('div', class_='SearchResult__smallPhoto')
    if img_div:
        style = img_div.get('style')
        data['avatar_url'] = extract_style_url(style)
    
    # 3. 提取姓名与年龄 (Name & Age)
    # 结构: vivian, 31
    # 这里的 HTML 结构比较深，通常在 svg 图标后的 div 里
    # 技巧：直接找包含 "SearchResult__nameRowContainer" 下的文本
    name_row = html_card.find('div', class_='SearchResult__nameRowContainer')
    if name_row:
        # 获取纯文本，通常格式为 "Name, Age"
        full_text = name_row.get_text(separator=',').strip()
        # 清洗掉多余的 svg 文本，只取最后一部分
        # 这里用更通用的方式：查找那个 style="margin-left: 5px;" 的 div
        name_div = name_row.find('div', style="margin-left: 5px;")
        if name_div:
            data['name_age_raw'] = name_div.get_text(strip=True)
    
    # 4. 提取地理位置 (Location)
    loc_div = html_card.find('div', class_='SearchResult__user-info__location')
    data['location'] = clean_text(loc_div.get_text()) if loc_div else "N/A"
    
    # 5. 提取自我介绍 (Bio)
    bio_div = html_card.find('div', class_='SearchResult__user-info__introduce')
    data['bio'] = clean_text(bio_div.get_text()) if bio_div else ""
    
    return data