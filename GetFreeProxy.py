import requests
import json
import socks
import socket

socks.set_default_proxy(socks.SOCKS4, "101.39.205.10", 1080)
socket.socket = socks.socksocket

url = "https://www.uu-proxy.com/api/free"
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7,en-GB;q=0.6",
    "Connection": "keep-alive",
    "Host": "www.uu-proxy.com",
    "Referer": "https://www.uu-proxy.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
response = requests.get(url, headers=headers)

data = json.loads(response.text)
for proxy in data['free']['proxies']:
    proxy_str = f"{proxy['ip']}:{proxy['port']}:{proxy['scheme']}"
    print(proxy_str)
