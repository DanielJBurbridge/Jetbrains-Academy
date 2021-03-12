def get_percentage(number, round_digits=None):
    if round_digits is None:
        return f'{int(number * 100)}%'
    else:
        return f'{round(number * 100, round_digits)}%'
