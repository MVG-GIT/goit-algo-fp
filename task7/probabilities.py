import random

def calculate_throws(simulations, sums):
    for a in range(simulations):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        s = dice1 + dice2
        sums[s] += 1
    return sums
         
def probabilities_monte_carlo(simulations, sums):
    return {sum: sums[sum] / simulations for sum in sums}

probabilities_table = {
    2: 1/36,
    3: 2/36,
    4: 3/36,
    5: 4/36,
    6: 5/36,
    7: 6/36,
    8: 5/36,
    9: 4/36,
    10: 3/36,
    11: 2/36,
    12: 1/36
}
