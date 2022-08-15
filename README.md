# python-ibc
A library used to condense down chain queries in an easy to use way.

Includes:
```
- Coingecko token price query
- chain_apis (rest, rpc, denom, logo png, twitter, explorers, staking & gov pages, coingecko_id, & chain_registery )
```


### Example usage
```py
from pyibc_api import get_chain
print(get_chain("juno")) # gets chain data
# {
#     "denom": "ujuno",
#     "name": "Juno",
#     "coingecko_id": "juno-network",
#     "explorers": {
#         "ping": 'https://ping.pub/juno',
#         "mintscan": 'https://www.mintscan.io/juno',
#         "keplr": 'https://wallet.keplr.app/chains/juno',        
#     },
#     "rest_root": "https://lcd-juno.itastakers.com", # https://rest.cosmos.directory/juno
#     "rpc_root": "https://rpc.cosmos.directory/juno",
#     "twitter": "@JunoNetwork",
#     "logo": "https://raw.githubusercontent.com/cosmos/chain-registry/master/juno/images/juno.png",
#     "chain-registry": "https://raw.githubusercontent.com/cosmos/chain-registry/master/juno/chain.json",
# }


from pyibc_chain.validators import get_latest_validator_set_sorted
for idx, op_addr in enumerate(get_latest_validator_set_sorted(get_chain("juno")['rest_root'], bondedOnly=True), 1):
    print(idx, op_addr, vals[op_addr])
    if idx > 10: break


from cosmpy_price import get_price
print(get_price(['juno-network', "cmdx"]))
# print(get_price('juno-network')) # also works
```