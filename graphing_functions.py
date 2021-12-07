import matplotlib.pyplot as plt

def scatterplot():
    print()


def histogram(values, names, num_of_graphs, pos, title,):
    if num_of_graphs>2:
        plt.subplot(2, 3, pos)
    else:
        plt.subplot(1, num_of_graphs, pos)
    plt.bar(names, values, width=5)
    plt.xlabel('Percentage Ranges')
    plt.ylabel('Total Count')
    plt.title(f'Histogram of{title}')
    


def bar_graph(values, names, title):
    plt.bar(names, values, width=1)
    plt.xlabel('Percentage Ranges')
    plt.ylabel('Total Count')
    plt.title(f'{title}')

#def scatter(y_value,x_value):
#    plt.scatter(x_value,y_value)
