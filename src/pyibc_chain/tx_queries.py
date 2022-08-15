import requests

# ! IMPORTANT
# This is a WIP and not apart of the library yet

# https://github.com/Reecepbcups/cosmos-validator-income-tracker/blob/main/src/CosmosEndpoints.py

headers = {'accept': 'application/json'}
PAGE_LIMIT = "&pagination.limit=1000"

# More specific
def getTxsAtHeight(height: int, msgType: str = ""):
    params = {
        'events': f'tx.height={height}',
        'order_by': 'ORDER_BY_UNSPECIFIED',
    }
    response = requests.get('https://api.cosmos.network/cosmos/tx/v1beta1/txs', params=params, headers=headers).json()
    if len(msgType) == 0:
        return response['txs']
    
    TxsWeWant = [] # from poc.py getTxsByHeight(
    for msg in response['txs']['body']['messages']:
        if msg['@type'] == msgType:
            TxsWeWant.append(msg)


def getTxEvents(rest_url, height: int, key = "txs"): # or tx_responses
    params = {
    'events': [
        f'tx.height={height}',
        'message.module=\'distribution\'',
    ],
    'order_by': 'ORDER_BY_UNSPECIFIED',
    }
    # curl -X GET "https://api.cosmos.network/cosmos/tx/v1beta1/txs?events=tx.height%3D10449274&events=message.module%3D'distribution'&order_by=ORDER_BY_UNSPECIFIED" -H "accept: application/json"
    return requests.get(f'{rest_url}/cosmos/tx/v1beta1/txs', params=params, headers=headers).json()[key]


def getMsgWithdrawValidatorCommission(height: int) -> list:
    # curl -X GET "https://api.cosmos.network/cosmos/tx/v1beta1/txs?events=tx.height%3D10449274&events=message.action%3D'%2Fcosmos.distribution.v1beta1.MsgWithdrawValidatorCommission'&order_by=ORDER_BY_UNSPECIFIED" -H "accept: application/json"
    eb = EventBuilder(height)
    eb.newAction('/cosmos.distribution.v1beta1.MsgWithdrawValidatorCommission')
    print(eb.build())
    response = requests.get('https://api.cosmos.network/cosmos/tx/v1beta1/txs', params=eb.build(), headers=headers).json()
    return response['txs']



class EventBuilder:
    # Build events easily at a height
    def __init__(self, height: int):
        self.height = height
        self.actions = []

    # https://github.com/cosmos/cosmos-sdk/pull/9139
    # Docs are out of date on how to do this
    def newAction(self, absolute_path):
        # "message.action='/cosmos.distribution.v1beta1.MsgWithdrawValidatorCommission'"
        # /cosmos.distribution.v1beta1.MsgWithdrawValidatorCommission
        if absolute_path.startswith('/'): absolute_path = absolute_path[1:]
        self.actions.append(f"message.action='/{absolute_path}'")

    def build(self):
        allEvents = self.actions + [f"tx.height={self.height}"]
        return {
            'events': allEvents,
            'order_by': 'ORDER_BY_UNSPECIFIED',
        }