def add(*nums):
    total = 0
    for n in nums:
        total += n
    return total


def mul(*nums):
    if len(nums) == 0:
        return 0
    total = 1
    for n in nums:
        total *= n
    return total


def sub(a, b):
    return a - b