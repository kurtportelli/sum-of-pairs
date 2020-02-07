def sum_pairs(ints, s):
    cache = set()
    for num in ints:
        other = s - num
        if other in cache:
            return [other, num]
        cache.add(num)
