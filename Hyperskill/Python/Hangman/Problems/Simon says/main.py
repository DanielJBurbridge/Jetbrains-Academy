def what_to_do(instructions):
    valid_end = (instructions.endswith("Simon says"))
    valid_start = (instructions.startswith("Simon says"))

    if valid_end:
        return f"I {instructions[:len('Simon says') +1]}"
    elif valid_start:
        return f"I {instructions[len('Simon says '):]}"
    else:
        return "I won't do it!"
