def pivot_index(nums):
    total_sum = sum(nums)
    left_sum = 0

    for i, num in enumerate(nums):
        if left_sum == (total_sum - left_sum - num):
            return i
        left_sum += num

    return -1

print(pivot_index([1, 7, 3, 6, 5, 6]))
print(pivot_index([1, 2, 3]))
print(pivot_index([2, 1, -1]))

