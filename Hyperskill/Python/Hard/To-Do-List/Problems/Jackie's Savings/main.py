def final_deposit_amount(*interest, amount=1000):
    value = amount
    for rate in interest:
        value *= (1 + (rate / 100))

    return round(value, 2)
