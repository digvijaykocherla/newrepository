def numJewelsInStones(jewels, stones):
    jewel_set = set(jewels)
    count = 0

    for stone in stones:
        if stone in jewel_set:
            count += 1

    return count


print(numJewelsInStones("aA", "aAAbbbb"))  # Output: 3
print(numJewelsInStones("z", "ZZ"))  # Output: 0
