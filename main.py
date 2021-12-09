import numpy as np
import matplotlib.pyplot as plt
from graphing_functions import histogram
from graphing_functions import bar_graph
#from graphing_functions import scatter



class Menu:

    '''
    Summary:
        A class used to store the inputs of a user to be called later by the program.
    
    Arguments:
        None
    '''

    def __init__(self):
        self.test_choice = ''
        self.focus_group = ''
        self.data_analysis = ''
        self.graph_choice = ''

    def print_menu_input(self):
        '''
        Summary: 
            A function to ask the user if they are content with their selections of data and data 
        analysis type. If the user inputs no, the function will return False which is read by the program telling it to 
        re-request inputs. 
        
        Parameters: 
            Self
        
        Returns: 
            True or False
        '''
        print(f'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
CHOSEN MENU OPTIONS:
    Test score:     {self.test_choice}
    Focus group:    {self.focus_group}
    Analysis type:  {self.data_analysis}
    Graph Type:     {self.graph_choice}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
        print()
        valid_input = False
        while valid_input == False:
            yes_or_no = input('Are you satisfed with this input? (yes/no) -> ').title().strip() #Asks if the user is ok with their choice
            print()
            if yes_or_no == 'No': return False      #If not return False
            elif yes_or_no == 'Yes': return True    #If yes return True
            else:
                print('Invalid entry, please try again')
                continue


    def request_inputs(self, focus_group_choices):
        '''
        Summary: 
            Function to request the inputs from the user.
        
        Parameters: 
            Self
            focus_group_choices (list): list of valid user inputs for choosing a focus group

        Returns: 
            None
        '''
        valid_input = False
        while valid_input == False:
            self.test_choice = input('Please input the test you wish to analyze [Math, Writing, Reading] -> ').title().strip() #Asks for an test input
            print()
            if self.test_choice not in ['Math', 'Writing', 'Reading']:  #If the input is not in this list the program asks for a new one
                print('Invalid entry, please try again')
                print()
                continue
            break
            
        while valid_input == False:
            valid_choices = [element for element in focus_group_choices]
            self.focus_group = input(f'Now please input the focus group you wish to analyze {valid_choices} -> ').title().strip() #Asks for focus group input
            print()
            if self.focus_group not in focus_group_choices:   #If the input is not in this list the program asks for a new one
                print('Invalid entry, please try again')
                print()
                continue
            break

        while valid_input == False:
            self.data_analysis = input('Please input the way you would like to analyze the data you\'ve chosen [Highest Mark, Lowest Mark, Test Average] -> ').title().strip() #Asks for how the user wishes to analyze the data
            print()
            if self.data_analysis not in ['Highest Mark', 'Lowest Mark', 'Test Average']:   #If the input is not in this list the program asks for a new one
                print('Invalid entry, please try again')
                print()
                continue
            break

        while valid_input == False:
            self.graph_choice = input('Finally, please input the type of graph you would like to see for this data [Histogram or Bar Graph] -> ').title().strip()   #Asks for the type of graph
            print()
            if self.graph_choice not in ['Histogram', 'Bar Graph']: #If the input is not in this list the program asks for a new one
                print('Invalid entry, please try again')
                print()
                continue
            break



def data_list_generator(focus_group, grade_array, array_dict):
    '''
    Summary: 
        A function to go through a requested array (though the string 'grade_array') to match a value to a list of possible 'keywords' within a given list,
    when found, a list is created with he first value being the found 'keyword' (something like 'male' or 'female') and the second value is the 7th column (being the grade)
    this list is then appended to another list to be returned.
    It basically grabs only the necessary data for the program

    Args:
        focus_group (list): A list of all requested bytes the function needs to locate (Example: 'must extract all necessary data for Gender' then focus_group=[d'male, d'female])
    grade_array (str): A string that must be one of the folowing: 'Writing', 'Math', or 'Reading'. This pertains to the grade array the user would like to pull information from
    array_dict (dict): A dictionary containing the three CSV files as numpy arrays

    Returns:
        output_list (list): A list of lists, each of the larger lists relate to each student, and each smaller list has two values, first is the found 'keyword' and the second is the grade found in the requested array
    '''
    

    output_list=[]
    for pos_1 in range(len(array_dict[grade_array][:,0])):      #these two for loops goes through each value of a 299x7 array, first loop is for the 300 rows
        for pos_2 in range(len(array_dict[grade_array][0,:])):    #and the second is for the 7 columns
            if array_dict[grade_array][pos_1][pos_2] in focus_group:                            #checks to see if the requested array (called using the array_dict) matches any of the bytes in the focus_group list
                #if true a list is made then appended to a larger list
                x=str(array_dict[grade_array][pos_1][pos_2]) #first value of the smaller list is the found byte converted to a string and manually striped of it's byte notation ("b'")
                output_list.append([x,array_dict[grade_array][pos_1][6]])                       #second value is the grade in that row (found in column 6) then the list is appended into the larger list to be returned
    return output_list



def analysis(input_list,analysis_type):
    '''Summary: 
        A function that preformes one of the possible calculations on an array: min, max, or mean

    Args:
        input_array (array): An array that will have numpy calculations preformed on it
    analysis_type (str): A string that must be one of the folowing: 'Min', 'Max', or 'Mean'. This is the calculation that the user would like to preform on the input_array

    Returns:
        int: the returned number from the requested operation done on the input_array
    '''
    int_array_list = [int(i) for i in input_list]
    computing_array = np.array(int_array_list)

    if analysis_type=='Lowest Mark':        #looks for which operation is requested
        return np.min(computing_array)      #then preforms that operation and returns the value
    elif analysis_type=='Highest Mark':
        return np.max(computing_array)
    else:
        return np.mean(computing_array)



def sort_list(input_list,keyword):
    '''
    Summary: 
        A function that goes through a list of lists (input_list) looking for the first value of each smaller list to equal the given keyword, if it is, the second value is appended to an output_list

    Args:
        input_list (list): A list where the values are lists whose values are a string and an int (example: =[['male', 80.0], ['female', 64.0]])
    keyword (byte): A byte that will be converted to a string then used by the program to find matching values within input_list

    Returns:
        output_list (list): a list of int values (grades) for each of the extracted students that meet the keyword
    '''
    output_list=[]
    for each_student in input_list:                                             #grabs each list within the input_list in a for loop
        if each_student[0]==keyword:     #then checks if the first value of that list matches the keyword in string form and is manually striped of it's byte notation ("b'")
            output_list.append(each_student[1])                                 #if true the second value in the list is then appended to the output_list to be returned
    return output_list



def histogram_values(input_list):
    '''
    Summary: 
        A function that counts each time any of the values within the input_list is between 0-100 and returns a list of 20 values, where each value is the number of times the value was found in the input_list that are within 5 unit intervals

    Args:
        input_list (list): A list where the values are floats that are between 0-100

    Returns:
        list: a list of 20 values that corespond to the number of grades within each 5% interval. For example: if the input_list had the values [12,5,13] then the output would have a '1' and a '2' in the first and second
    position with zeros in the other 18 postions
    '''
    percent_group_list=[5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,101]
    output_list=[]
    count=0
    for percent in range(percent_group_list[0]):
            for element in input_list:
                if int(element) == percent:
                    count+=1
    output_list.append(count)
    for group_pos in range(1,20):
        count=0
        for percent in range(percent_group_list[group_pos-1],percent_group_list[group_pos]):
            for element in input_list:
                if int(element) == percent:
                    count+=1
        output_list.append(count)
    return (output_list)    #returns the output_list as an array

def main():
    #Importing Data
    writing_score_array=np.genfromtxt('Writing Scores.csv',skip_header = True, delimiter=',', encoding='utf-8', dtype=str)
    math_score_array=np.genfromtxt('Reading Scores.csv',skip_header = True, delimiter=',', encoding='utf-8', dtype=str)
    reading_score_array=np.genfromtxt('Math Scores.csv',skip_header = True, delimiter=',', encoding='utf-8', dtype=str)

    array_dict={                        #Dictionary to call the correct array for a given string as the key
        'Writing':writing_score_array,
        'Math':math_score_array,
        'Reading':reading_score_array}

    #exit clause for the menu loop
    exit_clause = False

    #Creating a dictionary of focus groups and their corosponding subsections
    #This is used in the program to both check users entries and make sure they are a correct focus group as well as pass the lists of values to functions for analysis and graphing
    writing_score_array_with_header=np.genfromtxt('Writing Scores.csv', delimiter=',', encoding='utf-8', dtype=str)

    focus_group_choices={}                                          #Creats an empty dictionary
    for i in range(1,6):                                            #For loop to iterate over each coloumn
        focus_group = writing_score_array_with_header[0,i].title()  #Stores the focus group
        sub_sections = []                                           #Creates an empty list for the sub sections
        for item in writing_score_array_with_header[1:, i]:         #Iterates through the coloum of a focus group
            if item not in sub_sections:                            #Every time it finds a new type of item it adds it to list 
                sub_sections.append(item)
        focus_group_choices[focus_group]=sub_sections               #Finally creates a new dictionary entry with the key being the focus group and the value being the list of sub sections


    print('''
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    This is a school grade statistics analysis program.
    You will be prompted with various choices including what data set you wish to analyze and how you want to analyze it.
    Students wrote three different tests, one on math, one on reading and one on writing. 
    Students have also had different asspects about them recorded such as: gender, ethnicity, their parent's education,
    what kind of lunch they consistantly eat, and whether or not they completed a test prep.

    Using this program you can analyze any one of the chosen tests based on one of the focus groups recorded about the 
    students and print the corosponding data you would like to see such as highest/lowest marks and the average.
    You can also print out either bar graphs or histograms of the selected data groups as well.
    A bar graph will show the number of passing grades for each focus group and the histogram will show the totat
    students within a percentile range.
    You may also compare more than one data set at one time. 
    (Please note: no entries are case sensitive)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ''')
    while exit_clause == False:
        num_of_graphs = input('How many graphs would you like to compare? [1 or 2] -> ')    #Asks the user for the number of graphs they would like to analyze
        if num_of_graphs not in ['1','2']:
            print('Invalid entry, please try again')    #If the input is not in this list the program asks for a new one
            continue
        num_of_graphs = int(num_of_graphs)
        print()
        break

    user_inputs_1 = Menu()                              #Creates a new menu class instance to hold the users first inputs
    while exit_clause == False:                         
        user_inputs_1.request_inputs(focus_group_choices.keys())                  #Calls the request_inputs function from the menu class to collect the user inputs
        exit_clause = user_inputs_1.print_menu_input()  #Checks that the user is satisfied with their inputs, if no is inputted the request_inputs function is called again, if yes is inputted the program continues

    exit_clause = False
    if num_of_graphs == 2:  #If the user selected that they wanted to analyze two graphs a second menu instance is created to collect their second inputs
        print('\nNow select your second input options')
        print()
        user_inputs_2 = Menu()  
        while exit_clause == False:     
            user_inputs_2.request_inputs(focus_group_choices.keys())
            exit_clause = user_inputs_2.print_menu_input()

    #OUTPUTS FOR FIRST USER INPUTS

    computeing_array_1 = data_list_generator(focus_group_choices[user_inputs_1.focus_group],user_inputs_1.test_choice, array_dict) #a list of only the useful values are created using the data_list_generator
    list_of_calculated_values = []
    #Formatted Print statements for chosen analyzed data
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'Results for {user_inputs_1.data_analysis}s of the focus groups in the {user_inputs_1.test_choice} test')
    print('---------------------------------------------------------------------------')
    for group in focus_group_choices[user_inputs_1.focus_group]:                                        #This for loop goes through each sub-section of a chosen focus group printing the chosen data
        calculated_data = analysis(sort_list(computeing_array_1, group), user_inputs_1.data_analysis)   #Obtains the data
        list_of_calculated_values.append(calculated_data)                                               #Adds the data to a list so it can be indexed as part of the for loop
        print(f'{user_inputs_1.data_analysis} for {group}: {list_of_calculated_values[focus_group_choices[user_inputs_1.focus_group].index(group)]:.2f}') #Formatted print statement for the data that was just obtained
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    if user_inputs_1.graph_choice == 'Bar Graph': #creates a Bar graph if the user requests it for the first data
        plt.figure(1)
        values_to_graph = []
        for group in focus_group_choices[user_inputs_1.focus_group]:    #this grabs each of the groups (example: male and female)
            sorted_list = sort_list(computeing_array_1, group)          #creates a list of the grades for that group in the requested data set
            count = 0
            for i in sorted_list:   #counts each of the passing grades (above 59%)
                if int(i) >= 60:
                    count += 1
            values_to_graph.append(count)   #adds the count to a list of the other counts
            names_to_graph = focus_group_choices[user_inputs_1.focus_group] #grabs the name of focus group for the title (ex:'Gender')
        bar_graph(values_to_graph, names_to_graph, str(f'Number of Total Passing Grades for {user_inputs_1.focus_group}'))  
        #creates the bar graph with the function 'bar_graph' using the y values 'values_to_graph', the x values 'names_to_graph', and the title as the last argument

    if user_inputs_1.graph_choice == 'Histogram': #creates a histogram graph if the user requests it for the first data
        plt.figure(1)
        values_to_graph = []
        count=0
        for group in focus_group_choices[user_inputs_1.focus_group]:    #this grabs each of the groups (example: male and female)
            count+=1
            sorted_list = sort_list(computeing_array_1, group)      #creates a list of the grades for that group in the requested data set
            values_to_graph = histogram_values(sorted_list)         #creates a list of the number of grades within each 5% intervul
            names_to_graph = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]  #list for the x_values
            histogram(values_to_graph, names_to_graph, len(focus_group_choices[user_inputs_1.focus_group]), count, str(f'{group} sub-section of {user_inputs_1.focus_group}',))
            #creates the histogram using the y_values created earlier as 'values_to_graph', the x_values as 'names_to_graph', the total number of subgraphs in the len() function
            #'count' is the position of the current subplot, and last is part of the title for the graph

    #OUTPUS FOR SECOND USER INPUTS

    if num_of_graphs == 2: #the same two steps are repeated here but for the second graphs and second data sets
        plt.figure(2)
        computeing_array_2 = data_list_generator(focus_group_choices[user_inputs_2.focus_group],user_inputs_2.test_choice, array_dict) #a list of only the useful values are created using the data_list_generator
        list_of_calculated_values = []
        #Formatted Print statements for chosen analyzed data
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(f'Results for {user_inputs_2.data_analysis}s of the focus groups in the {user_inputs_2.test_choice} test')
        print('---------------------------------------------------------------------------')
        for group in focus_group_choices[user_inputs_2.focus_group]:                                        #This for loop goes through each sub-section of a chosen focus group printing the chosen data
            calculated_data = analysis(sort_list(computeing_array_2, group), user_inputs_2.data_analysis)   #Obtains the data
            list_of_calculated_values.append(calculated_data)                                               #Adds the data to a list so it can be indexed as part of the for loop
            print(f'{user_inputs_2.data_analysis} for {group}: {list_of_calculated_values[focus_group_choices[user_inputs_2.focus_group].index(group)]:.2f}') #Formatted print statement for the data that was just obtained
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        
        if user_inputs_2.graph_choice == 'Bar Graph': #creates a Bar graph if the user requests it for the second data
            values_to_graph = []
            plt.figure(2)
            for group in focus_group_choices[user_inputs_2.focus_group]:    #this grabs each of the groups (example: male and female)
                sorted_list = sort_list(computeing_array_2, group)          #creates a list of the grades for that group in the requested data set
                count = 0
                for i in sorted_list:    #counts each of the passing grades (above 59%)
                    if int(i) >= 60:
                        count += 1
                values_to_graph.append(count)   #adds the count to a list of the other counts
                names_to_graph = focus_group_choices[user_inputs_2.focus_group] #grabs the name of focus group for the title (ex:'Gender')
            bar_graph(values_to_graph, names_to_graph, str(f'Number of Total Passing Grades for {user_inputs_2.focus_group}'))
            #creates the bar graph with the function 'bar_graph' using the y values 'values_to_graph', the x values 'names_to_graph', and the title as the last argument

        if user_inputs_2.graph_choice == 'Histogram':   #creates a histogram graph if the user requests it for the second data
            plt.figure(2)
            values_to_graph = []
            pos_count=0
            for group in focus_group_choices[user_inputs_2.focus_group]:    #this grabs each of the groups (example: male and female)
                pos_count+=1
                sorted_list = sort_list(computeing_array_2, group)          #creates a list of the grades for that group in the requested data set
                values_to_graph = histogram_values(sorted_list)             #creates a list of the number of grades within each 5% intervul
                names_to_graph = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100] #list for the x_values
                histogram(values_to_graph, names_to_graph, len(focus_group_choices[user_inputs_2.focus_group]), pos_count, str(f'{group} sub-section of {user_inputs_1.focus_group}'))
                #creates the histogram using the y_values created earlyier as 'values_to_graph', the x_values as 'names_to_graph', the total number of subgraphs in the len() function
                #'count' is the position of the current subplot, and last is part of the title for the graph


    plt.show()

    #so i finished the graphs to 1.work (as it they don't break and the histogram is now measuring in 5% intervals), and 2.look pretty
    #I changed the functionality of the histogram_values function, messed with lines 270-335, and made some changes to the graphing_functions.py
    #I was also trying to set up the scatter graph, then while testing i realized that the scatter will look super stupid and display like no relevant information, so if u wanna try to get that going
    #   I left my work hashed out in lines 57-63 (i moved the input to ask for a scatter into the class so that it would ask twice if 2 graphs were selected by user) lines 337-344, and lines 25-26 in the graphing_functions.py
    #   (ur also gonna need to unhash line 5 if u wanna try the scatter for the function import)
    # i've commented most of my lines, ik most of urs is done but some stuff isn't commented yet so when you get the chance if u can finish the commenting that would be coooool
    #also removed the import sort line at like line 4 or som, we weren't using it so idk
    #i also think we should just move the graphing functions form graphing_funcitons.py to the main.py, just so the markers have an easyier time but it works as is
    #i'd say after we finish comments and make the write up we are done, unless u can think of something or do think we need the scatter