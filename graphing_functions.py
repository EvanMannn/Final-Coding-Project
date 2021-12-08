import matplotlib.pyplot as plt
import numpy as np

def histogram(values, names, num_of_graphs, pos, title):
    '''
    Summary:
        A function to produce a histogram of a chosen data set

    Parameters:
        values (list of values), names (list of names), num_of_graphs (int, number of graphs within the figure),
    pos (int, the position of the graph within the figure), title (str, title of the graph)

    returns:
        None
    '''
    if num_of_graphs > 2:                   #Determines if the figure should be formatted with 1 row or 2
        plt.subplot(2, 3, pos)              #If there are more than 2 graphs a second row is insetered for cleaner formatting
    else:
        plt.subplot(1, num_of_graphs, pos)  #Else only one row of graphs is needed. This row is made with a length equal to the number of graphs
    
    rainbow = plt.get_cmap('rainbow', 8)    #Creating a colormap
    plt.bar(names, values, width=3, color=rainbow(np.linspace(1,0,15))) #Plots the values with their corosponding names. This function also makes each bar a width of 3 and gives each a unique color from the colormap
    plt.tight_layout(pad=1.5)               #Spaces the graph within the figure 
    plt.xlabel('Percentage Ranges')         #Labels the x axis
    plt.ylabel('Total Count')               #Labels the y axis
    plt.title(f'Histogram of{title}')       #Titles the graph


def bar_graph(values, names, title):
    '''
    Summary:
        A function to produce a bar graph of a chosen data set

    Parameters:
        values (list of values), names (list of names), title (str, title of the graph)

    returns:
        None
    '''
    accent = plt.get_cmap('Accent', 8)  #Creates a colormap
    plt.bar(names, values, width=0.3, color=accent(range(8)))   #Plots the values for the graph with the corosponding names and assigns each bar a unique color
    plt.ylabel('Total Count')           #Labels the y axis
    plt.xticks(rotation=22)             #Rotates the labels of each bar so that they don't overlap
    plt.title(f'{title}')               #Titles the graph
