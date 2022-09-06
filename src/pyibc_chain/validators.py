import requests, time

from pyibc_utils.convert import simplify_balance, simplify_balance_str # . when live, remove . for testing here
from pyibc_api.chain_apis import REST_ENDPOINTS

headers = {'accept': 'application/json'}
# PAGE_LIMIT = "?pagination.limit=1000"

def get_validator_stats(chain, rest_url, operator_address, include_number_of_unique_delegations=False) -> dict:
    '''
    Returns a dict of information about a given validator
    https://api.cosmos.network/cosmos/staking/v1beta1/validators/cosmosvaloper16s96n9k9zztdgjy8q4qcxp4hn7ww98qkrka4zk
    '''

    ROOT_URL = rest_url


    # get a validators details
    queryEndpoint = f"{ROOT_URL}/{REST_ENDPOINTS['validator_info']}/{operator_address}".replace("{EPOCH}", f'{int(time.time())}')
    r = requests.get(queryEndpoint, headers=headers)
    if r.status_code != 200:
        print(f"\n(Error): {r.status_code} on {queryEndpoint}")
        return {}
    validatorData = r.json()['validator']

    # get chain params
    params_url = f"{ROOT_URL}/{REST_ENDPOINTS['params']}"
    r = requests.get(params_url, headers=headers)
    if r.status_code != 200:
        print(f"\n(Error): {r.status_code} on {params_url}")
        return {}
    paramsData = r.json()['params']

    # ! IMPORTANT, this may take a while
    # get total # of unique delegators
    #  https://lcd-osmosis.blockapsis.com/cosmos/staking/v1beta1/validators/osmovaloper16s96n9k9zztdgjy8q4qcxp4hn7ww98qk5wjn0s/delegations?pagination.limit=10000
    uniqueDelegators = "-1"
    try:
        if(include_number_of_unique_delegations):
            # raise Exception("test")
            delegators_url = f"{queryEndpoint}/delegations?pagination.limit=10000"
            r = requests.get(delegators_url, headers=headers)
            if r.status_code != 200:
                print(f"\n(Error): {r.status_code} on delegators_url: {delegators_url}")       
            uniqueDelegators = f"{len(r.json()['delegation_responses'])}"
    except:
        pass

    validator_ranking = get_latest_validator_set_sorted(rest_url, bondedOnly=False)
    # find index of operator_address in validator_ranking
    index = 1
    for k in validator_ranking.keys():
        if k == operator_address:
            break
        index += 1

    return {
        "chain": chain,
        "operator_address": validatorData['operator_address'],
        "jailed": validatorData['jailed'], 
        "status": validatorData['status'], # BOND_STATUS_BONDED
        "bonded_utokens": f"{int(validatorData['tokens'])}", # then based on bond_denom, convert
        "bonded_tokens": simplify_balance_str(paramsData['bond_denom'], int(validatorData['tokens'])),
        "moniker": validatorData['description']['moniker'],
        "identity": validatorData['description']['identity'],
        "website": validatorData['description']['website'],
        "security_contact": validatorData['description']['security_contact'],
        "commission": validatorData['commission']['commission_rates']['rate'],
        "validator_ranking": index,
        "max_validators": paramsData['max_validators'],
        "bond_denom": paramsData['bond_denom'],        
        "unique_delegators": uniqueDelegators,        
    }

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

def get_latest_validator_set_sorted(rest_url, bondedOnly: bool = True):    
    link = f'{rest_url}/cosmos/staking/v1beta1/validators?pagination.limit=1000'
    if bondedOnly: link += '&status=BOND_STATUS_BONDED'
    validators = {}
    
    response = requests.get(link, headers=headers).json()
    for val in response['validators']:
        # print(val) # sort them?
        # exit()
        opp_addr = val['operator_address']
        moniker = val['description']['moniker']
        identity = val['description']['identity']
        status = val['status']
        tokens = val['tokens']        
        validators[opp_addr] = {'moniker': moniker, 'identity': identity, "status": status, "token_share": int(tokens)}

    return {k: v for k, v in sorted(validators.items(), key=lambda x: x[1]['token_share'], reverse=True)}

def get_validator_slashes(rest_url, valop: str) -> list:
    response = requests.get(f'{rest_url}/cosmos/distribution/v1beta1/validators/{valop}/slashes').json()
    return response['slashes']

if __name__ == "__main__":
    # vals = get_latest_validator_set_sorted("https://lcd-osmosis.blockapsis.com", True)
    # for idx, op_addr in enumerate(vals, 1):
    #     print(idx, op_addr, vals[op_addr])
    #     if idx > 13: break

    stats = get_validator_stats(
        chain="osmosis", 
        rest_url="https://api.osmosis.interbloc.org", 
        operator_address="osmovaloper16s96n9k9zztdgjy8q4qcxp4hn7ww98qk5wjn0s", 
        include_number_of_unique_delegations=True
    )

    print(stats)