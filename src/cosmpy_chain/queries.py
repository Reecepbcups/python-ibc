import requests

headers = {'accept': 'application/json'}
PAGE_LIMIT = "&pagination.limit=1000"

# import simplify_balance from convert
from convert import simplify_balance

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
    # print(l)
    response = requests.get(l, headers=headers).json()
    return response['block']['data']['txs']


if __name__ == "__main__":
    from cosmpy_api import get_chain
    chain_endpoint = get_chain("osmosis")['rest_root']
    # print(get_latest_block_height(chain_endpoint))

    # print(get_outstanding_commission_rewards("osmovaloper16s96n9k9zztdgjy8q4qcxp4hn7ww98qk5wjn0s", chain_endpoint))
    # print(get_outstanding_commission_rewards_str("osmovaloper16s96n9k9zztdgjy8q4qcxp4hn7ww98qk5wjn0s", chain_endpoint))