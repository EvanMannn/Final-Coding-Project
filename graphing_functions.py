import matplotlib.pyplot as plt

def scatterplot():
    print()


def histogram(values, names, num_of_graphs, pos, title):
    plt.subplot(1, num_of_graphs, pos)
    plt.bar(names, values, width=1)
    plt.xlabel('Percentage Ranges')
    plt.ylabel('Total Count')
    plt.title(f'Histogram of {title}')
    


def bar_graph(values, names, num_of_graphs, pos, title):
    plt.subplot(1, num_of_graphs, pos)
    plt.bar(names, values, width=1)
    plt.xlabel('Percentage Ranges')
    plt.ylabel('Total Count')
    plt.title(f'Histogram of {title}')