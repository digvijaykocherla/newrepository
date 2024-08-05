def min_energy_cost(energy):
    n = len(energy)
    if n == 0:
        return 0
    if n == 1:
        return energy[0]

    dp = [0] * n
    dp[0] = energy[0]
    dp[1] = energy[1]

    for i in range(2, n):
        dp[i] = min(dp[i - 1], dp[i - 2]) + energy[i]

    return min(dp[n - 1], dp[n - 2])

print(min_energy_cost([10, 15, 20]))
print(min_energy_cost([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
