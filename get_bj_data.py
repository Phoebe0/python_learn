import requests
from bs4 import BeautifulSoup

# 定义要爬取的网址
url = "https://example.com/shanghai-attractions/mid-autumn-festival-tickets"

# 发送GET请求并获取网页内容
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 使用BeautifulSoup解析网页内容
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 根据网页结构和元素标签，找到包含中秋节售票信息的部分
    # 请根据实际网页结构进行调整
    ticket_info = soup.find("div", {"class": "mid-autumn-tickets"})
    
    # 提取售票信息
    if ticket_info:
        ticket_text = ticket_info.get_text()
        print(ticket_text)
    else:
        print("未找到中秋节售票信息。")

else:
    print("请求失败，状态码：", response.status_code)
