import matplotlib.pyplot as plt

def draw_barplot(results_first, results_second, title_first, title_second):
    plt.figure(figsize=(8, 5))
    plt.bar(results_first.keys(),
            [p*100 for p in results_first.values()],
            width=0.4, label=title_first, alpha=0.7)

    plt.bar([x + 0.4 for x in results_second.keys()],
            [p*100 for p in results_second.values()],
            width=0.4, label=title_second, alpha=0.7)

    plt.xticks(range(2, 13))
    plt.xlabel("Die sum")
    plt.ylabel("Probability (%)")
    plt.title(f"{title_first} vs {title_second}")
    plt.legend()
    plt.show()



def print_cli_table(results_first, results_second, title_first, title_second):
    print(f"Sum\t{title_first}\t{title_second}\tDifference")
    for s in range(2, 13):
        tb = results_first[s] * 100
        mc = results_second[s] * 100
        diff = mc - tb
        print(f"{s}\t{tb:.2f}%\t\t{mc:.2f}%\t\t{diff:.2f}%")
