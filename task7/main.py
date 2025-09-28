from probabilities import calculate_throws, probabilities_table, probabilities_monte_carlo
from visualize import draw_barplot, print_cli_table

# sims
N = 1000000  

sum_counter = {i: 0 for i in range(2, 13)}
sum_counter = calculate_throws(N, sum_counter)



probabilities_mc = probabilities_monte_carlo(N, sum_counter)


print_cli_table(probabilities_table, probabilities_mc, "Table", "Monte-Carlo")
draw_barplot(probabilities_table, probabilities_mc, "Table", "Monte-Carlo")