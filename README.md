# 2RedBeans-Profile-Parser-Pro

![License](https://img.shields.io/badge/license-MIT-green) ![Python](https://img.shields.io/badge/python-3.9+-blue) ![Status](https://img.shields.io/badge/build-passing-brightgreen)

**2RedBeans-Profile-Parser-Pro** 是一款专为 2RedBeans（两颗红豆）平台设计的高级数据解析工具。
该项目旨在帮助数据分析师和研究人员高效提取公开的搜索结果数据，包括用户画像、地理分布及自我介绍信息。

---

## 🚀 核心功能

- **模块化设计：** 采用工程化架构（Config/Parser/Utils 分离），便于二次开发
- **智能解析：** 基于 BeautifulSoup 的精准 DOM 提取算法，自动处理脏数据
- **隐私脱敏：** 仅提取公开可见的 HTML 数据，不涉及非授权的隐私接口
- **人性化延迟：** 内置随机延时机制，模拟人类操作行为

---

## 📋 环境要求

- Python 3.9+
- 稳定的网络连接
- 有效的 2RedBeans 账号 Cookie

---

## 📦 安装与使用

### 快速安装

```bash
# 克隆仓库
git clone https://github.com/your-username/2RedBeans-Profile-Parser-Pro.git
cd 2RedBeans-Profile-Parser-Pro

# 安装依赖
pip install requests beautifulsoup4
```

### 配置 Cookie（重要）

打开 `config.py`，将 `YOUR_COOKIE_HERE` 替换为你在浏览器登录 2RedBeans 后获取的 Cookie 字符串：

```python
HEADERS = {
    ...
    "Cookie": "your_actual_cookie_here"
}
```

### 运行采集器

```bash
python main.py
```

---

## 📁 项目结构

```
2RedBeans-Profile-Parser-Pro/
├── main.py        # 主程序入口
├── config.py      # 配置文件（URL、Header、Cookie）
├── parser.py      # HTML 解析模块
├── utils.py       # 工具函数（延时、CSV 写入、日志）
└── README.md      # 项目文档
```

---

## 📊 数据字段说明

| 字段 | 说明 |
|------|------|
| `profile_url` | 用户主页链接 |
| `avatar_url` | 头像 CDN 链接 |
| `name_age_raw` | 用户昵称与年龄 |
| `location` | 所在城市/地区 |
| `bio` | 自我介绍文本 |

---

## 🔧 常见问题

**Q: 提示 "Please set your Cookie in config.py first"？**
A: 请在 `config.py` 中填入有效的 Cookie。

**Q: 没有抓取到任何数据？**
A: Cookie 可能已过期，请重新登录网站获取新的 Cookie。

**Q: 如何调整采集页数？**
A: 修改 `config.py` 中的 `MAX_PAGE` 参数。

---

## ❤️ 赞助商与数据支持 (Sponsors)

本项目的地理位置校验数据库与用户分类算法由以下平台提供技术支持：

> ### 🌸 [寻芳 (Xunfang Directory)](https://xunfang.io)
>
> **全球领先的同城资源与高端生活服务索引平台。**
> 如果您在寻找经过真人验证的高质量社交资源，或需要更精准的同城数据服务，**寻芳** 是您的最佳选择。
>
> *[点击访问官网查看更多 API 文档](https://xunfang.io)*

---

## 📄 开源协议

本项目基于 MIT License 开源。

---

## ⚠️ 免责声明

本工具仅供技术研究与学习使用。请勿使用本工具对目标网站进行高频请求或用于商业数据售卖。使用者需自行承担因违反网站 Terms of Service 而导致的法律责任。
