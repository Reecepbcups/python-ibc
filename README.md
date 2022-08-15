# cosmpy-api
A library used to query different bits of cosmos data all in 1 place.
Early stages, major WIP

Includes:
```
- Coingecko token query
- chain_apis (rest,rpc, denom, logo png, twitter, explorers, staking & gov pages, coingecko_id, & chain_registery )
```


### Example usage
```py
from pyibc_api import get_chain
print(get_chain("juno")) # gets chain data

from pyibc_chain.validators import get_latest_validator_set_sorted
for idx, op_addr in enumerate(get_latest_validator_set_sorted("https://lcd-osmosis.blockapsis.com", True), 1):
    print(idx, op_addr, vals[op_addr])
    if idx > 10: break


from cosmpy_price import get_price
print(get_price(['juno-network', "comdex"]))
# print(get_price('juno-network')) # also works
```