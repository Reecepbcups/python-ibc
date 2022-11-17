# python-ibc

A library used to condense down-chain queries in an easy-to-use way.

Includes:

```bash
- Coingecko token price query
- chain_apis (rest, rpc, denom, logo png, twitter, explorers, staking & gov pages, coingecko_id, & chain_registery )
```

## Used by

Used in / for:

- <https://github.com/Reecepbcups/cosmos-validator-income-tracker> (prices, queries, etc.)
- <https://github.com/Reecepbcups/cosmos-governance-bot>
- <https://github.com/Reecepbcups/cosmos-balance-bot>

## Example usage

```py
from pyibc_api import get_chain, ChainInfo
info: ChainInfo
info = get_chain("juno")
print(info) # gets chain data

# Returns:
# class ChainInfo:
#     '''Object to track important data about a chain'''
#     name: str
#     denom: str
#     coingecko_id: str
#     bech32_prefix: str
#     rest_root: str
#     rpc_root: str
#     twitter: str
#     logo: str
#     chain_registry: str
#     explorers: dict

from pyibc_chain.validators import get_latest_validator_set_sorted
for idx, op_addr in enumerate(get_latest_validator_set_sorted(info.rest_root, bondedOnly=True), 1):
    print(idx, op_addr, vals[op_addr])
    if idx > 10: break


from cosmpy_price import get_price
print(get_price(['juno-network', "cmdx"]))
# print(get_price('juno-network')) # also works
```
