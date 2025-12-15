# config.py
# Nexus Project Configuration File

# 目标网站基础信息
BASE_URL = "https://www.2redbeans.com/zh-CN/app/search"
DOMAIN = "https://www.2redbeans.com"

# 采集页数设置
START_PAGE = 1
MAX_PAGE = 5  # 演示模式下建议设小一点

# 请求头 (关键：用户必须填入自己的 Cookie 才能访问搜索页)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Referer": "https://www.2redbeans.com/zh-CN/app/",
    # [IMPORTANT] 请在浏览器 F12 中复制您的真实 Cookie 填入下方
    "Cookie": "YOUR_COOKIE_HERE"
}

# 输出文件
OUTPUT_FILE = "2redbeans_data.csv"