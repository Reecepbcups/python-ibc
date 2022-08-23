# convert token types to their parent forms
def simplify_balance(denom: str, amount) -> dict:    
    # removes the u denom & div by 1mil. So ucraft 1000000 = craft 1
    if denom.startswith('u'):        
        fmtNum = "{:,}".format(round(float(amount) / 1_000_000, 2))
        # return f"{fmtNum} {denom[1::]}"
        return {denom[1::]: fmtNum}

    elif denom.startswith('n'): # ncheq
        fmtNum = "{:,}".format(round(float(amount) / 1_000_000_000, 2))
        # return f"{fmtNum} {denom[1::]}"
        return {denom[1::]: fmtNum}
    
    elif denom.startswith('a'): # aevmos
        fmtNum = "{:,}".format(round(float(amount) / 1_000_000_000_000_000_000, 2))
        # return f"{fmtNum} {denom[1::]}"
        return {denom[1::]: fmtNum}

    else:        
        # return f"{int(amount)} {denom}"
        return {denom: float(amount)}

def simplify_balances_dict(balances: dict, show_ibc_hash=False, show_gamm=False) -> dict:
    '''
    Reduces [{"denom": "ucraft","amount": "69908452"},{"denom": "uexp","amount": "1000100"}]
    To: {'ucraft':69908452, 'uexp':1000100}
    '''
    output = {}
    for balance in balances:
        denom = balance['denom']
        amount = balance['amount']

        if show_ibc_hash and denom.startswith('ibc/'):
            continue # skip non native assets
        elif show_gamm and denom.startswith('gamm'):
            continue # skip osmo pools
        
        for k, v in simplify_balance(denom, amount).items():
            output[k] = v
    
    return dict(output)    


def simplify_balance_str(denom: str, amount) -> str:
    output = ""
    for d, amt in simplify_balance(denom, amount).items():
        output += f"{amt} {d}"
    return output


if __name__ == "__main__":
    print(simplify_balance_str('ucraft', 1_000_000)) # 10^6
    print(simplify_balance_str('aevmos', 100000000000000000)) # 10^18 (or 10^17)
