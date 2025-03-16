import requests

if __name__ == '__main__':
    url = "https://api.upbit.com/v1/market/all?is_details=true"
    #url = "https://api.bithumb.com/v1/market/all?isDetails=false"

    headers = {"accept": "application/json"}

    res = requests.get(url, headers=headers)

    data = res.json()

    for oneData in data:
        print(f"market:{oneData['market']}")

    #print(res.json())