import requests

from .convert import simplify_balance_str

from cosmpy_api.chain_apis import REST_ENDPOINTS

headers = {'accept': 'application/json'}

def get_validator_stats(chain, rest_url, operator_address, include_number_of_unique_delegations=False) -> dict:
    '''
    Returns a dict of information about a given validator
    https://api.cosmos.network/cosmos/staking/v1beta1/validators/cosmosvaloper16s96n9k9zztdgjy8q4qcxp4hn7ww98qkrka4zk
    '''

    ROOT_URL = rest_url


    # get a validators details
    queryEndpoint = f"{ROOT_URL}/{REST_ENDPOINTS['validator_info']}/{operator_address}"
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
        "max_validators": paramsData['max_validators'],
        "bond_denom": paramsData['bond_denom'],        
        "unique_delegators": uniqueDelegators,        
    }