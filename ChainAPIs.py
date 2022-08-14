'''
Dict of chains in the following format:

{
    "ticker": [
        "LCD endpoints for validator stats",
        {
            "ping": "https://ping.pub/ticker/gov/",
            "mintscan": "https://mintscan.io/ticker/proposals/",
        },
        "@twitter"
    ]
}

Take from:
- https://github.com/Reecepbcups/cosmos-validator-income-tracker (prices, queries, etc.)

curl -X GET "https://api.cosmos.network/cosmos/staking/v1beta1/validators/cosmosvaloper16s96n9k9zztdgjy8q4qcxp4hn7ww98qkrka4zk" -H "accept: application/json"
'''

# /cosmos/staking/v1beta1/validators/<address>

PAGES = {
    "ping": {
        "gov_page": "/gov/{id}",
        "staking_page": "/staking/{valoper}",
    },
    "mintscan": {
        "gov_page": "/proposals/{id}",
        "staking_page": "/proposals/{valoper}",
    },
    "keplr": {
        "gov_page": "/proposals/{id}",
        "staking_page": "/validators/{valoper}", 
    },
}

REST_ENDPOINTS = {
    "validator_info": "/cosmos/staking/v1beta1/validators/",
    "proposals": "/cosmos/gov/v1beta1/proposals",
}

chainAPIs = {
    # alias pointing to the main dict, have a check instance == str type
    # "udig": "dig",
    # "dig-chain": "dig",
    "dig": {
        "denom": "udig",
        "name": "Dig Chain",
        "coingecko_id": "dig-chain",
        "explorers": {
            "ping": 'https://ping.pub/dig',
        },
        "rest_root": "https://api-1-dig.notional.ventures",
        "rpc_root": "https://rpc.cosmos.directory/dig",
        "twitter": "@dig_chain",
        "logo": "https://raw.githubusercontent.com/cosmos/chain-registry/master/dig/images/dig.png",
        "chain-registry": "https://raw.githubusercontent.com/cosmos/chain-registry/master/dig/chain.json",
    },

    "juno": {
        "denom": "ujuno",
        "name": "Juno",
        "coingecko_id": "juno",
        "explorers": {
            "ping": 'https://ping.pub/juno',
            "mintscan": 'https://www.mintscan.io/juno',
            "keplr": 'https://wallet.keplr.app/chains/juno',        
        },
        "rest_root": "https://lcd-juno.itastakers.com", # https://rest.cosmos.directory/juno
        "rpc_root": "https://rpc.cosmos.directory/juno",
        "endpoints": {
            "validators": "/cosmos/staking/v1beta1/validators/",
            "proposals": "/cosmos/gov/v1beta1/proposals",
        },
        "twitter": "@JunoNetwork",
        "logo": "https://raw.githubusercontent.com/cosmos/chain-registry/master/juno/images/juno.png",
        "chain-registry": "https://raw.githubusercontent.com/cosmos/chain-registry/master/juno/chain.json",
    },

    "chihuahua": "huahua",
    "huahua": {
        "denom": "uhuahua",
        "name": "Chihuahua",
        "coingecko_id": "",
        "explorers": {
            "ping": 'https://ping.pub/chihuahua',
            "mintscan": 'https://www.mintscan.io/chihuahua',
        },
        "rest_root": "https://api.chihuahua.wtf", 
        "rpc_root": "https://rpc.cosmos.directory/chihuahua",
        "endpoints": {
            "validators": "/cosmos/staking/v1beta1/validators/",
            "proposals": "/cosmos/gov/v1beta1/proposals",
        },
        "twitter": "@ChihuahuaChain",
        "logo": "https://raw.githubusercontent.com/cosmos/chain-registry/master/chihuahua/images/huahua.png",
        "chain-registry": "https://raw.githubusercontent.com/cosmos/chain-registry/master/chihuahua/chain.json",
    },

    "osmosis": "osmo",
    "osmo": {
        "denom": "uosmo",
        "name": "Osmosis",
        "coingecko_id": "osmosis",
        "explorers": {
            "ping": 'https://ping.pub/osmosis',
            "mintscan": 'https://www.mintscan.io/osmosis',
            "keplr": 'https://wallet.keplr.app/chains/osmosis',
        },
        "rest_root": "https://api.chihuahua.wtf", 
        "rpc_root": "https://rpc.cosmos.directory/chihuahua",
        "twitter": "@OsmosisZone",
        "logo": "https://info.osmosis.zone/static/media/logo.551f5780.png",
        "chain-registry": "https://raw.githubusercontent.com/cosmos/chain-registry/master/osmosis/chain.json",
    },

    "cosmos": "atom",
    "atom": {
        "denom": "uatom",
        "name": "Cosmos Hub",
        "coingecko_id": "cosoms",
        "explorers": {
            "ping": 'https://ping.pub/cosmos',
            "mintscan": 'https://www.mintscan.io/cosmos',
            "keplr": 'https://wallet.keplr.app/chains/cosmos-hub'
        },
        "rest_root": "https://lcd-cosmoshub.blockapsis.com", 
        "rpc_root": "https://rpc.cosmos.directory/cosmoshub",
        "twitter": "@Cosmos",
        "logo": "https://raw.githubusercontent.com/cosmos/chain-registry/master/cosmoshub/images/atom.png",
        "chain-registry": "https://raw.githubusercontent.com/cosmos/chain-registry/master/cosmoshub/chain.json",
    },

    "akash": "akt",
    "akt": {
        "denom": "uakt",
        "name": "Akash",
        "coingecko_id": "akash",
        "explorers": {
            "ping": 'https://ping.pub/akash-network',
            "mintscan": 'https://www.mintscan.io/akash',
            "keplr": 'https://wallet.keplr.app/chains/akash'
        },
        "rest_root": "https://akash.api.ping.pub", 
        "rpc_root": "https://rpc.cosmos.directory/akash",
        "twitter": "@Akashnet_",
        "logo": "https://raw.githubusercontent.com/cosmos/chain-registry/master/akash/images/akt.png",
        "chain-registry": "https://raw.githubusercontent.com/cosmos/chain-registry/master/akash/chain.json",
    },

    "stargaze": "stars",
    "stars": {
        "denom": "ustars",
        "name": "Stargaze",
        "coingecko_id": "stargaze",
        "explorers": {
            "ping": 'https://ping.pub/stargaze',
            "mintscan": 'https://www.mintscan.io/stargaze',
            "keplr": 'https://wallet.keplr.app/chains/stargaze'
        },
        "rest_root": "https://rest.stargaze-apis.com", 
        "rpc_root": "https://rpc.cosmos.directory/stargaze",
        "twitter": "@StargazeZone",
        "logo": "https://raw.githubusercontent.com/cosmos/chain-registry/master/stargaze/images/stars.png",
        "chain-registry": "https://raw.githubusercontent.com/cosmos/chain-registry/master/stargaze/chain.json",
    },

    "kava": {
        "denom": "",
        "name": "Kava",
        "coingecko_id": "kava",
        "explorers": {
            "ping": 'https://ping.pub/kava',
            "mintscan": 'https://www.mintscan.io/kava',
            "keplr": 'https://wallet.keplr.app/chains/kava'
        },
        "rest_root": "https://api.data.kava.io", 
        "rpc_root": "https://rpc.cosmos.directory/kava",
        "twitter": "@kava_platform",
        "logo": "https://raw.githubusercontent.com/cosmos/chain-registry/master/kava/images/kava.png",
        "chain-registry": "https://raw.githubusercontent.com/cosmos/chain-registry/master/kava/chain.json",
    },

    "like": {
        "denom": "ulike",
        "name": "Likecoin",
        "coingecko_id": "",
        "explorers": {
            "ping": 'https://ping.pub/likecoin',
        },
        "rest_root": "https://mainnet-node.like.co", 
        "rpc_root": "https://rpc.cosmos.directory/likecoin",
        "twitter": "@likecoin",
        "logo": "https://raw.githubusercontent.com/cosmos/chain-registry/master/likecoin/images/like.png",
        "chain-registry": "https://raw.githubusercontent.com/cosmos/chain-registry/master/likecoin/chain.json",
    },

    "xprt": {
        "denom": "",
        "name": "",
        "coingecko_id": "",
        "explorers": {
            "ping": 'https://ping.pub/persistence',
            "mintscan": 'https://www.mintscan.io/persistence',
            "keplr": 'https://wallet.keplr.app/chains/persistence',            
        },
        "rest_root": "https://rest.core.persistence.one", 
        "rpc_root": "",
        "twitter": "@PersistenceOne",
        "logo": "",
        "chain-registry": "",
    },
    "cmdx": {
        "denom": "uxmdx",
        "name": "Comdex",
        "coingecko_id": "",
        "explorers": {
            "ping": 'https://ping.pub/comdex',
            "mintscan": 'https://www.mintscan.io/comdex',            
        },
        "rest_root": "https://rest.comdex.one", 
        "rpc_root": "",
        "twitter": "@ComdexOfficial",
        "logo": "",
        "chain-registry": "",
    },

    
    'bcna': {
        "denom": "",
        "name": "",
        "coingecko_id": "",
        "explorers": {
            "ping": "https://ping.pub/bitcanna",
            "mintscan": "https://www.mintscan.io/bitcanna"
        },
        "rest_root": "https://lcd.bitcanna.io",
        "rpc_root": "",
        "twitter": "@BitCannaGlobal",
        "logo": "",
        "chain-registry": ""
    },
    'btsg': {
        "denom": "",
        "name": "",
        "coingecko_id": "",
        "explorers": {
            "ping": "https://ping.pub/bitsong",
            "mintscan": "https://www.mintscan.io/bitsong"
        },
        "rest_root": "https://lcd-bitsong.itastakers.com",
        "rpc_root": "",
        "twitter": "@BitSongOfficial",
        "logo": "",
        "chain-registry": ""
    },
    'band': {
        "denom": "",
        "name": "",
        "coingecko_id": "",
        "explorers": {
            "ping": "https://ping.pub/band-protocol",
            "mintscan": "https://www.mintscan.io/akash"
        },
        "rest_root": "https://laozi1.bandchain.org/api",
        "rpc_root": "",
        "twitter": "@BandProtocol",
        "logo": "",
        "chain-registry": ""
    },
    'boot': {
        "denom": "",
        "name": "",
        "coingecko_id": "",
        "explorers": {
            "ping": "https://ping.pub/bostrom",
            "keplr": "https://wallet.keplr.app/chains/bostrom"
        },
        "rest_root": "https://lcd.bostrom.cybernode.ai",
        "rpc_root": "",
        "twitter": "",
        "logo": "",
        "chain-registry": ""
    },
    'cheqd': {
        "denom": "",
        "name": "",
        "coingecko_id": "",
        "explorers": {
            "ping": "https://ping.pub/cheqd"
        },
        "rest_root": "https://api.cheqd.net",
        "rpc_root": "",
        "twitter": "@cheqd_io",
        "logo": "",
        "chain-registry": ""
    },
    'cro': {
        "denom": "",
        "name": "",
        "coingecko_id": "",
        "explorers": {
            "ping": "https://ping.pub/crypto-com-chain",
            "mintscan": "https://www.mintscan.io/crypto-org",
            "keplr": "https://wallet.keplr.app/chains/crypto-org"
        },
        "rest_root": "https://mainnet.crypto.org:1317",
        "rpc_root": "",
        "twitter": "@cryptocom",
        "logo": "",
        "chain-registry": ""
    },
    'evmos': {
        "denom": "",
        "name": "",
        "coingecko_id": "",
        "explorers": {
            "ping": "https://ping.pub/evmos",
            "mintscan": "https://www.mintscan.io/evmos",
            "keplr": "https://wallet.keplr.app/chains/evmos/proposals"
        },
        "rest_root": "https://rest.bd.evmos.org:1317",
        "rpc_root": "",
        "twitter": "@EvmosOrg",
        "logo": "",
        "chain-registry": ""
    },
    'fetch': {
        "denom": "",
        "name": "",
        "coingecko_id": "",
        "explorers": {
            "ping": "https://ping.pub/fetchhub",
            "mintscan": "https://www.mintscan.io/fetchai"
        },
        "rest_root": "https://rest-fetchhub.fetch.ai",
        "rpc_root": "",
        "twitter": "@Fetch_ai",
        "logo": "",
        "chain-registry": ""
    },
    'grav': {
        "denom": "",
        "name": "",
        "coingecko_id": "",
        "explorers": {
            "ping": "https://ping.pub/gravity-bridge",
            "mintscan": "https://www.mintscan.io/gravity-bridge",
            "keplr": "https://wallet.keplr.app/chains/gravity-bridge"
        },
        "rest_root": "https://gravitychain.io:1317",
        "rpc_root": "",
        "twitter": "@gravity_bridge",
        "logo": "",
        "chain-registry": ""
    },
    'inj': {
        "denom": "",
        "name": "",
        "coingecko_id": "",
        "explorers": {
            "ping": "https://ping.pub/injective",
            "mintscan": "https://www.mintscan.io/injective"
        },
        "rest_root": "https://public.lcd.injective.network",
        "rpc_root": "",
        "twitter": "@InjectiveLabs",
        "logo": "",
        "chain-registry": ""
    },
    'iris': {
        "denom": "",
        "name": "",
        "coingecko_id": "",
        "explorers": {
            "ping": "https://ping.pub/iris-network",
            "mintscan": "https://www.mintscan.io/iris",
            "keplr": "https://wallet.keplr.app/chains/irisnet"
        },
        "rest_root": "https://lcd-iris.keplr.app",
        "rpc_root": "",
        "twitter": "@irisnetwork",
        "logo": "",
        "chain-registry": ""
    },
    'iov': {
        "denom": "",
        "name": "",
        "coingecko_id": "",
        "explorers": {
            "ping": "https://ping.pub/starname",
            "mintscan": "https://www.mintscan.io/starname",
            "keplr": "https://wallet.keplr.app/chains/starname"
        },
        "rest_root": "https://lcd-iov.keplr.app",
        "rpc_root": "",
        "twitter": "@starname_me",
        "logo": "",
        "chain-registry": ""
    },
    'lum': {
        "denom": "",
        "name": "",
        "coingecko_id": "",
        "explorers": {
            "ping": "https://ping.pub/lum-network",
            "mintscan": "https://www.mintscan.io/lum"
        },
        "rest_root": "https://node0.mainnet.lum.network/rest",
        "rpc_root": "",
        "twitter": "@lum_network",
        "logo": "",
        "chain-registry": ""
    },
    'regen': {
        "denom": "",
        "name": "",
        "coingecko_id": "",
        "explorers": {
            "ping": "https://ping.pub/regen",
            "mintscan": "https://www.mintscan.io/regen",
            "keplr": "https://wallet.keplr.app/chains/regen"
        },
        "rest_root": "https://regen.stakesystems.io",
        "rpc_root": "",
        "twitter": "@regen_network",
        "logo": "",
        "chain-registry": ""
    },
    'hash': {
        "denom": "",
        "name": "",
        "coingecko_id": "",
        "explorers": {
            "ping": "https://ping.pub/provenance"
        },
        "rest_root": "https://api.provenance.io",
        "rpc_root": "",
        "twitter": "@provenancefdn",
        "logo": "",
        "chain-registry": ""
    },
    'secret': {
        "denom": "",
        "name": "",
        "coingecko_id": "",
        "explorers": {
            "ping": "https://ping.pub/secret",
            "mintscan": "https://www.mintscan.io/secret",
            "keplr": "https://wallet.keplr.app/chains/secret-network"
        },
        "rest_root": "https://api.scrt.network",
        "rpc_root": "",
        "twitter": "@SecretNetwork",
        "logo": "",
        "chain-registry": ""
    },
    'sent': {
        "denom": "",
        "name": "",
        "coingecko_id": "",
        "explorers": {
            "ping": "https://ping.pub/sentinel",
            "mintscan": "https://www.mintscan.io/sentinel",
            "keplr": "https://wallet.keplr.app/chains/sentinel"
        },
        "rest_root": "https://lcd-sentinel.keplr.app",
        "rpc_root": "",
        "twitter": "@Sentinel_co",
        "logo": "",
        "chain-registry": ""
    },
    'sif': {
        "denom": "",
        "name": "",
        "coingecko_id": "",
        "explorers": {
            "ping": "https://ping.pub/sifchain",
            "mintscan": "https://www.mintscan.io/sifchain",
            "keplr": "https://wallet.keplr.app/chains/sifchain"
        },
        "rest_root": "https://api.sifchain.finance:443",
        "rpc_root": "",
        "twitter": "@sifchain",
        "logo": "",
        "chain-registry": ""
    },
    'kuji': {
        "denom": "",
        "name": "",
        "coingecko_id": "",
        "explorers": {
            "ping": "https://explorer.chaintools.tech/kujira"
        },
        "rest_root": "https://kujira-api.polkachu.com",
        "rpc_root": "",
        "twitter": "@TeamKujira",
        "logo": "",
        "chain-registry": ""
    },
    'terraC': {
        "denom": "",
        "name": "",
        "coingecko_id": "",
        "explorers": {
            "ping": "https://ping.pub/terra-luna"
        },
        "rest_root": "https://blockdaemon-terra-lcd.api.bdnodes.net:1317",
        "rpc_root": "",
        "twitter": "@terraC_money",
        "logo": "",
        "chain-registry": ""
    },
    'terra': {
        "denom": "",
        "name": "",
        "coingecko_id": "",
        "explorers": {
            "ping": "https://ping.pub/terra2"
        },
        "rest_root": "https://phoenix-lcd.terra.dev",
        "rpc_root": "",
        "twitter": "@terra_money",
        "logo": "",
        "chain-registry": ""
    },
    'umee': {
        "denom": "",
        "name": "",
        "coingecko_id": "",
        "explorers": {
            "ping": "https://ping.pub/umee",
            "mintscan": "https://www.mintscan.io/umee",
            "keplr": "https://wallet.keplr.app/chains/umee"
        },
        "rest_root": "https://api.blue.main.network.umee.cc",
        "rpc_root": "",
        "twitter": "@Umee_CrossChain",
        "logo": "",
        "chain-registry": ""
    },

}