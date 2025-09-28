def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(),
        key=lambda x: x[1]["calories"] / x[1]["cost"],
        reverse=True)
    total_cost, total_calories = 0, 0
    chosen = []

    for name, data in sorted_items:
        if total_cost + data["cost"] <= budget:
            chosen.append(name)
            total_cost += data["cost"]
            total_calories += data["calories"]

    return {"chosen": chosen, "calories": total_calories, "cost": total_cost}