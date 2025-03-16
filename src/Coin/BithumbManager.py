import requests

if __name__ == '__main__':
    url = "https://api.bithumb.com/v1/ticker?markets=KRW-BTC"

    headers = {"accept": "application/json"}

    res = requests.get(url, headers=headers)

    data = res.json()

    #for oneData in data:
    #    print(f"market:{oneData['market']}")

    print(data[0]["trade_price"])