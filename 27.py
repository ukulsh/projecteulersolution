def sequence(num):
    if (num == 1):
        return 1
    else:
        return sequence(num - 1) + 2 * (num - 1)