import requests

def get_price(coins: list = []) -> float:
    if len(coins) == 0:
        raise ValueError("No coins provided")

    coins = ",".join(coins)
    url=f'''https://api.coingecko.com/api/v3/simple/price?ids={coins}&vs_currencies=usd'''
    coinData = requests.get(url).json()

    prices = {}
    for cName in coinData:
        prices[cName] = float(coinData[cName]['usd'])
              
    return prices

if __name__ == '__main__':
    print((['juno-network']))