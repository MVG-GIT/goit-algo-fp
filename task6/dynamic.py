def dynamic_programming(items, budget):
    names = list(items.keys())
    costs = [items[n]["cost"] for n in names]
    calories = [items[n]["calories"] for n in names]
    n = len(names)

    dp = [[0] * (budget + 1) for a in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w],
                               dp[i - 1][w - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    w = budget
    chosen = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen.append(names[i - 1])
            w -= costs[i - 1]

    return {"chosen": chosen[::-1],
            "calories": dp[n][budget],
            "cost": budget - w}
