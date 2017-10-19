import requests
from operator import itemgetter

# 执行API调用并存储响应
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(r.json())
