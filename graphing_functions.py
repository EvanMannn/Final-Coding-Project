import matplotlib.pyplot as plt

def scatterplot():
    print()


def histogram(values, names, fig_num, title):
    plt.figure(fig_num)
    plt.bar(names, values, width=1)
    plt.xlabel('Percentage Ranges')
    plt.ylabel('Total Count')
    plt.title(f'Histogram of {title}')


def bar_graph(values, names, fig_num, title):
    plt.figure(fig_num)
    plt.bar(names, values, width=1)
    plt.xlabel('Percentage Ranges')
    plt.ylabel('Total Count')
    plt.title(f'Bar graph of {title}')