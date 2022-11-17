import requests

headers = {'accept': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
PAGE_LIMIT = "&pagination.limit=1000"

# import simplify_balance from convert
from pyibc_utils.convert import simplify_balance
from pyibc_api.chain_apis import REST_ENDPOINTS
from pyibc_api import get_chain

def get_latest_block_height(rest_endpoint: str = "") -> int:
    response = requests.get(f'{rest_endpoint}/blocks/latest', headers=headers).json()
    return int(response['block']['header']['height'])


def get_outstanding_commission_rewards(valop: str, rest_endpoint: str = "", humanReadable = True) -> dict:
    # This function should really be async / multithreaded in some way
    # I assume /outstanding_rewards is their commission AND their self bonded rewards? Look into API
    response = requests.get(f'{rest_endpoint}/cosmos/distribution/v1beta1/validators/{valop}/commission', headers=headers)
    print(f'{rest_endpoint}/cosmos/distribution/v1beta1/validators/{valop}/commission')

    data = {}
    rewards = response.json()['commission']['commission'] # /outstanding_rewards is 'rewards' 'rewards'
    for r in rewards:
        denom = r['denom']
        amt = r['amount']
        if humanReadable:
            for k, v in simplify_balance(denom, amt).items():
                data[k] = v
        else:
            data[denom] = amt    
    return data # {'osmo': '0.04'}

def get_outstanding_commission_rewards_str(valop: str, rest_endpoint: str = ""):
    data = get_outstanding_commission_rewards(valop, rest_endpoint, humanReadable=True)
    return ", ".join([f"{k}: {v}" for k, v in data.items()])

def get_latest_block_transactions(rest_endpoint: str = "", block: str = "latest") -> list:
    l = f'{rest_endpoint}/blocks/{block}'    
    response = requests.get(l, headers=headers).json()
    return response['block']['data']['txs']

def get_balances(chain_name: str, walletAddr) -> dict:
    '''
    Gets the balances JSON from chain & returns those values
    [{"denom": "ucraft","amount": "69908452"},{"denom": "uexp","amount": "1000100"}]
    '''
    rest_endpoint = get_chain(chain_name).rest_root
    if rest_endpoint.endswith("/"):
        rest_endpoint = rest_endpoint[:-1]
    queryEndpoint = rest_endpoint + "/" + REST_ENDPOINTS['balances'] + f"/{walletAddr}"
    r = requests.get(queryEndpoint, headers=headers) 
    if r.status_code != 200:
        print(f"\n(Error): {r.status_code} on {queryEndpoint}")
        return {}
    
    # http://API:1317/cosmos/bank/v1beta1/balances/craft10r39fueph9fq7a6lgswu4zdsg8t3gxlqd6lnf0    
    return r.json()['balances']


if __name__ == "__main__":    
    from pyibc_api import ChainInfo
    info: ChainInfo
    info = get_chain("pasg")
    chain_endpoint = info.rest_root
    print(chain_endpoint)
    # print(get_latest_block_height(chain_endpoint))

    # print(get_outstanding_commission_rewards("osmovaloper16s96n9k9zztdgjy8q4qcxp4hn7ww98qk5wjn0s", chain_endpoint))
    # print(get_outstanding_commission_rewards_str("osmovaloper16s96n9k9zztdgjy8q4qcxp4hn7ww98qk5wjn0s", chain_endpoint))

    # print(get_balances("osmosis", "osmo10r39fueph9fq7a6lgswu4zdsg8t3gxlqyhl56p"))