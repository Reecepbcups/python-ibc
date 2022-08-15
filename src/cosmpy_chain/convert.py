# convert token types to their parent forms
def simplify_balance(denom: str, amount) -> dict:    
    # removes the u denom & div by 1mil. So ucraft 1000000 = craft 1
    if denom.startswith('u'):        
        fmtNum = "{:,}".format(round(float(amount) / 1_000_000, 2))
        # return f"{fmtNum} {denom[1::]}"
        return {denom[1::]: fmtNum}

    elif denom.startswith('a'): # aevmos
        fmtNum = "{:,}".format(round(float(amount) / 1_000_000_000_000_000_000, 2))
        # return f"{fmtNum} {denom[1::]}"
        return {denom[1::]: fmtNum}

    else:        
        # return f"{int(amount)} {denom}"
        return {denom: float(amount)}

def simplify_balance_str(denom: str, amount) -> str:
    output = ""
    for d, amt in simplify_balance(denom, amount).items():
        output += f"{amt} {d}"
    return output


if __name__ == "__main__":
    print(simplify_balance_str('ucraft', 1_000_000)) # 10^6
    print(simplify_balance_str('aevmos', 100000000000000000)) # 10^18 (or 10^17)
