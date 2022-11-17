'''
Dict of chains following the same schema so all my applications can use.
'''

import requests
from dataclasses import dataclass

# NOTE: no /'s after any URL

# TODO: ping is now = ping-pub

PAGES = {
    "ping.pub": {
        "gov_page": "gov/{id}",
        "staking_page": "staking/{valoper}",
    },
    "ping-pub": {
        "gov_page": "gov/{id}",
        "staking_page": "staking/{valoper}",
    },
    "mintscan": {
        "gov_page": "proposals/{id}",
        "staking_page": "proposals/{valoper}",
    },
    "keplr": {
        "gov_page": "proposals/{id}",
        "staking_page": "validators/{valoper}", 
    },
    "dig": {
        "gov_page": "proposals/{id}",
        "staking_page": "https://app.digchain.org/staking", # no valoper view
    },
    "EZStaking Tools": {
        "gov_page": "proposals/{id}",
        "staking_page": "validators/{valoper}",
    },
    "explorers.guru": {
        "gov_page": "proposal/{id}",
        "staking_page": "validator/{valoper}",
    },
    "atomscan": {
        "gov_page": "votes/{id}",
        "staking_page": "validators/{valoper}",
    },
}

CUSTOM_EXPLORER_LINKS = {
    "dig": "https://app.digchain.org",    
}

REST_ENDPOINTS = {
    # DO NOT START WITH A /, this way we have to do in our f string
    "validator_info": "cosmos/staking/v1beta1/validators",
    "proposals": "cosmos/gov/v1beta1/proposals",
    "params": "cosmos/staking/v1beta1/params",
    "balances": "cosmos/bank/v1beta1/balances",
}




COSMOS_DIR_URL = "https://chains.cosmos.directory/"
@dataclass
class ChainInfo:
    '''Object to track important data about a chain'''
    name: str
    denom: str
    coingecko_id: str
    bech32_prefix: str
    rest_root: str
    rpc_root: str
    twitter: str
    logo: str
    chain_registry: str
    explorers: dict
    def __init__(self) -> None:
        pass

@dataclass
class DAOInfo:
    ''''''
    name: str
    proposals: str
    vote: str
    twitter: str

    def __init__(self, name, proposals, vote, twitter) -> None:
        self.name = name
        self.proposals = proposals
        self.vote = vote
        self.twitter = twitter


JUNO_REST_API = "https://rest-juno.ecostake.com/cosmwasm/wasm/v1/contract/"
DAOs = {
    "raw": DAOInfo(
        name = "RAW DAO",
        proposals = f"{JUNO_REST_API}/juno1eqfqxc2ff6ywf8t278ls3h3rdk7urmawyrthagl6dyac29r7c5vqtu0zlf/smart/eyJsaXN0X3Byb3Bvc2FscyI6e319?encoding=base64",
        vote = "https://www.rawdao.zone/vote",
        twitter = "@raw_dao"
    ),
    "rac": DAOInfo(
        name = "Racøøn DAO",
        proposals = f"{JUNO_REST_API}/juno16l0ymhpwfm63gdcjv8q32z7hqzv8g22spw6ul75l76s5lxtw4anscc5eek/smart/eyJsaXN0X3Byb3Bvc2FscyI6e319?encoding=base64",
        vote = "https://daodao.zone/dao/juno1svduqrvcmzpl5g74q8rkm6rhcjnhch2yaagzu4ljuv2u9tf86ltqx9a54s/proposals/A",
        twitter = "@RacoonSupply"
    ),
}

CHAIN_APIS = {} # symbols/tickes -> chain info
CHAIN_APIS_WALLETS = {} # wallet prefix -> symbol (-> chain information from there)

info = requests.get(COSMOS_DIR_URL).json().get("chains", [])
chain: dict # annotation
for chain in info:
    symbol = str(chain.get("symbol", ""))
    if len(symbol) == 0: continue

    bech32 = chain.get("bech32_prefix", "")    

    explorers = {}
    for expl in chain.get("explorers", []):   
        name = expl.get("name", expl.get('kind', ""))
        url = expl.get("url", '') 
        if len(name) == 0 or len(url) == 0: continue
        explorers[name] = url
    
    apis = {}
    for api_type in chain.get("best_apis", []): # rest, rpc
        v = chain.get("best_apis", {}).get(api_type, [{}])
        apis[api_type] = v[0].get("address", "") if len(v) > 0 else ""        

    # TODO: Do this or just save the data as it is in cosmos dir?
    cinfo = ChainInfo()
    cinfo.name = chain.get("pretty_name", "")
    cinfo.denom = chain.get("denom", "")
    cinfo.coingecko_id = chain.get("coingecko_id", "")
    cinfo.bech32_prefix = bech32
    cinfo.explorers = explorers
    cinfo.rest_root = apis['rest']
    cinfo.rpc_root = apis['rpc']
    cinfo.twitter = chain.get("twitter", "")
    cinfo.logo = chain.get("image", "")
    cinfo.chain_registry = f"https://raw.githubusercontent.com/cosmos/chain-registry/master/{chain.get('path')}/chain.json"

    CHAIN_APIS[symbol.lower()] = cinfo
    CHAIN_APIS_WALLETS[bech32] = symbol.lower()
    continue

# Normal names / aliases here
aliases = {
    # alias: name in CHAIN_APIS symbol
    "terra-classic": "lunc",
    "dvpn": "sent",
    "provenance": "hash",
    "bostrom": "boot",
    "bandchain": "band",
    "bitsong": "btsg",
    "comdex":"cmdx",
    "persistence":"xprt",
    "stargaze": "stars",
    "akash": "akt",
    "cosmos": "atom",
    "osmosis": "osmo",
    "chihuahua": "huahua",
    "dig-chain": "dig",
    "passage": "pasg",
}

def get_chain(name):
    if name not in CHAIN_APIS.keys() and name not in aliases.keys():
        raise ValueError("Unknown chain: {}".format(name))
    
    if name in aliases.keys():
        # name was an alias, so we get the real name by calling this function on itself again
        return CHAIN_APIS[aliases[name]]

    if name in CHAIN_APIS_WALLETS.keys():
        return CHAIN_APIS[CHAIN_APIS_WALLETS[name]]
        
    value = CHAIN_APIS[name]
    return value

def get_all_chains():
    # get all CHAIN_APIS keys & aliases keys
    keys = list(CHAIN_APIS.keys())
    for alias in aliases.keys():
        keys.append(alias)
    return keys

def get_all_chains_by_wallet_prefix():
    return list(CHAIN_APIS_WALLETS.keys())
    
def get_endpoint(key) -> str:
    if key not in REST_ENDPOINTS.keys():
        print("Unknown endpoint: {}. Available: \n{}".format(key, REST_ENDPOINTS))        

    return REST_ENDPOINTS.get(key, "")

if __name__ == "__main__":
    print(get_chain('dig'))
