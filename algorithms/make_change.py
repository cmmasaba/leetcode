def change(amount, charge):
    """
    Calculate how much change to give back to user in fewst denominations possible
    @param amount: the amount of money paid by user
    @param charge: the amount of money to charge the user

    :return: the change in as few denominations as possible
    """
    if charge > amount:
        raise Exception("Insufficient amount paid. Please add money.")
    
    denominations = [
        ("Thousand", 1000),
        ("Five hundred", 500),
        ("Two hundred", 200),
        ("One hundred", 100),
        ("Fifty", 50),
        ("Twenty", 20),
        ("Ten", 10),
        ("Five", 5)
    ]
    
    whole_change = amount - charge
    change_denominations = []
    
    for denomination_name, denomination_value in denominations:
        if whole_change >= denomination_value:
            quotient, remainder = divmod(whole_change, denomination_value)
            change_denominations.append({denomination_name: quotient * denomination_value})
            whole_change = remainder
    
    if whole_change > 0:
        change_denominations.append({"Shilling": whole_change})
    
    return change_denominations

print(change(2000, 1437))