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
from cosmpy_api import get_chain
print(get_chain("juno")) # get data

from cosmpy_price import get_price
print(get_price(['juno-network']))
```