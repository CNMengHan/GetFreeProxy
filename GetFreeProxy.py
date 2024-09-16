import requests
import json
import socks
import socket


def set_proxy(proxy_info):
    proxy_type = socks.SOCKS4 if proxy_info["type"] == "socks4" else socks.SOCKS5
    socks.set_default_proxy(proxy_type, proxy_info["ip"], proxy_info["port"])
    socket.socket = socks.socksocket


def get_response(url, headers):
    while True:
        for proxy in proxy_list:
            try:
                set_proxy(proxy)
                response = requests.get(url, headers=headers, timeout=5)
                if response.status_code == 200:
                    return response
            except requests.RequestException:
                print(f"Connection Error: {proxy['ip']}:{proxy['port']}")


proxy_list = [
    {"ip": "39.107.70.7", "port": 22, "type": "socks5"},
    {"ip": "116.255.147.37", "port": 3306, "type": "socks5"},
    {"ip": "180.106.150.247", "port": 2222, "type": "socks4"},
    {"ip": "120.25.222.150", "port": 1080, "type": "socks4"},
    {"ip": "101.39.205.10", "port": 1080, "type": "socks4"},
    {"ip": "182.92.185.192", "port": 443, "type": "socks5"},
    {"ip": "8.140.255.223", "port": 443, "type": "socks4"},
    {"ip": "112.126.73.130", "port": 1080, "type": "socks5"},
    {"ip": "117.80.63.66", "port": 1080, "type": "socks5"},
    {"ip": "150.158.2.130", "port": 80, "type": "http"},
    {"ip": "111.230.53.150", "port": 3129, "type": "http"},
    {"ip": "47.106.228.234", "port": 8088, "type": "socks5"},
    {"ip": "58.57.130.134", "port": 1080, "type": "socks5"},
    {"ip": "101.200.122.251", "port": 443, "type": "socks5"},
    {"ip": "49.232.207.118", "port": 80, "type": "http"},
    {"ip": "111.6.43.154", "port": 3128, "type": "http"},
    {"ip": "123.249.77.88", "port": 80, "type": "socks4"},
    {"ip": "121.37.221.98", "port": 443, "type": "socks5"},
    {"ip": "120.25.222.150", "port": 1080, "type": "socks5"},
    {"ip": "116.204.83.23", "port": 80, "type": "http"},
    {"ip": "124.221.31.66", "port": 80, "type": "http"},
    {"ip": "106.52.220.140", "port": 80, "type": "http"},
    {"ip": "47.109.143.104", "port": 8010, "type": "socks5"},
    {"ip": "159.75.179.68", "port": 8888, "type": "http"},
    {"ip": "39.104.173.190", "port": 10057, "type": "socks4"},
    {"ip": "49.232.61.105", "port": 1080, "type": "socks5"},
    {"ip": "101.201.181.233", "port": 8000, "type": "socks5"}
]
url = "https://www.uu-proxy.com/api/free"
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7,en-GB;q=0.6"
}

response = get_response(url, headers)
data = json.loads(response.text)

for proxy in data['free']['proxies']:
    proxy_str = f"{proxy['ip']}:{proxy['port']}:{proxy['scheme']}"
    print(proxy_str)
