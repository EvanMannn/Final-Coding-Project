import numpy as np
import matplotlib.pyplot as plt



class menu:

    def __init__(self):
        self.test_choice = ''
        self.focus_group = ''
        self.data_analysis = ''
        self.graph_choice = ''

    def print_menu_input(self):
        '''
        Summary: A function to ask the user if they are content with their selections of data and data 
        analysis type. If the user inputs no, the function will return False which is read by the program telling it to 
        re-request inputs. 
        
        Parameters: Self
        
        Returns: True or False
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
            yes_or_no = input('Are you satisfed with this input? (yes/no) -> ') #Asks if the user is ok with their choice
            print()
            if yes_or_no == 'no' or yes_or_no == 'No': return False             #If not reutrn False
            elif yes_or_no == 'Yes' or yes_or_no == 'yes': return True          #If yes return True
            else:
                print('Invalid entry, please try again')
                continue


    def request_inputs(self):
        '''
        Summary: Function to request the inputs for time period and country from ther user.
        
        Parameters: Self, List of countries 

        Returns: Tuple containing self.time and self.country
        '''
        valid_input = False
        while valid_input == False:
            self.test_choice = input('Please input the test you wish to analyze [Math, Writing, Reading] -> ').title() #Asks for an test input
            print()
            if self.test_choice not in ['Math', 'Writing', 'Reading']:  #If the input is not in this list the program asks for a new one
                print('Invalid entry, please try again')
                print()
                continue
            break
            
        while valid_input == False:
            self.focus_group = input('Now please input the focus group you wish to analyze [Gender, Ethnicity, Parent Education, Lunch, Test Prep] -> ').title() #Ask for focus group input
            print()
            if self.focus_group not in ['Gender', 'Ethnicity', 'Parent Education', 'Lunch', 'Test Prep']:
                print('Invalid entry, please try again')
                print()
                continue
            break

        while valid_input == False:
            self.data_analysis = input('Please input the way you would like to analyze the data you\'ve chosen [Highest Mark, Lowest Mark, Test Average] -> ').title() #Asks for how the user wishes to analyze the data
            print()
            if self.data_analysis not in ['Highest Mark', 'Lowest Mark', 'Test Average']:
                print('Invalid entry, please try again')
                print()
                continue
            break

        while valid_input == False:
            self.graph_choice = input('Finally, please input the type of graph you would like to see for this data [Histogram or Bar Graph] -> ').title()
            print()
            if self.graph_choice not in ['Histogram', 'Bar Graph']:
                print('Invalid entry, please try again')
                print()
                continue
            break



def data_list_generator(focus_group, grade_array):
    '''Summary: A function to go through a requested array (though the string 'grade_array') to match a value to a list of possible 'keywords' within a given list,
                when found, a list is created with he first value being the found 'keyword' (something like 'male' or 'female') and the second value is the 7th column (being the grade)
                this list is then appended to another list to be returned.
            It basically grabs only the necessary data for the program

    Args:
        focus_group (list): A list of all requested bytes the function needs to locate (Example: 'must extract all necessary data for Gender' then focus_group=[d'male, d'female])
        grade_array (str): A string that must be one of the folowing: 'Writing', 'Math', or 'Reading'. This pertains to the grade array the user would like to pull information from

    Returns:
        output_list (list): A list of lists, each of the larger lists relate to each student, and each smaller list has two values, first is the found 'keyword' and the second is the grade found in the requested array'''
    array_dict={                                         #Dictionary to call the correct array for a given string as the key
        'Writing':writing_score_array,
        'Math':math_score_array,
        'Reading':reading_score_array}

    output_list=[]
    for pos_1 in range(0,299):      #these two for loops goes through each value of a 299x7 array, first loop is for the 300 rows
        for pos_2 in range(0,6):    #and the second is for the 7 columns
            if array_dict[grade_array][pos_1][pos_2] in focus_group:                            #checks to see if the requested array (called using the array_dict) matches any of the bytes in the focus_group list
                #if true a list is made then appended to a larger list
                x=str(array_dict[grade_array][pos_1][pos_2]) #first value of the smaller list is the found byte converted to a string and manually striped of it's byte notation ("b'")
                output_list.append([x,array_dict[grade_array][pos_1][6]])                       #second value is the grade in that row (found in column 6) then the list is appended into the larger list to be returned
    return output_list



def analysis(input_list,analysis_type):
    '''Summary: A function that preformes one of the possible calculations on an array: min, max, or mean

    Args:
        input_array (array): An array that will have numpy calculations preformed on it
        analysis_type (str): A string that must be one of the folowing: 'Min', 'Max', or 'Mean'. This is the calculation that the user would like to preform on the input_array

    Returns:
        int: the returned number from the requested operation done on the input_array'''
    int_array_list = [int(i) for i in input_list]
    computing_array = np.array(int_array_list)

    if analysis_type=='Lowest Mark':        #looks for which operation is requested
        return np.min(computing_array)  #then preforms that operation and returns
    elif analysis_type=='Highest Mark':
        return np.max(computing_array)
    else:
        return np.mean(computing_array)



def sort_list(input_list,keyword):
    '''Summary: A function that goes through a list of lists (input_list) looking for the first value of each smaller list to equal the given keyword, if it is, the second value is appended to an output_list

    Args:
        input_list (list): A list where the values are lists whose values are a string and an int (example: =[['male', 80.0], ['female', 64.0]])
        keyword (byte): A byte that will be converted to a string then used by the program to find matching values within input_list

    Returns:
        output_list (list): a list of int values (grades) for each of the extracted students that meet the keyword'''
    output_list=[]
    for each_student in input_list:                                             #grabs each list within the input_list in a for loop
        if each_student[0]==keyword:     #then checks if the first value of that list matches the keyword in string form and is manually striped of it's byte notation ("b'")
            output_list.append(each_student[1])                                 #if true the second value in the list is then appended to the output_list to be returned
    #print('sort list function return') #~~Evan Testing~~#
    #print(output_list) #~~Evan Testing~~#
    return output_list



def prep_arrays_for_graphing(input_list):
    '''Summary: A function that counts each time any of the values within the input_list is between 0-100 and returns a list of 100 values, where each value is the number of times the value was found in the input_list

    Args:
        input_list (list): A list where the values are floats that are between 0-100

    Returns:
        array: an array of 100 floats, where it's position is the "requested value" and the value being the number of times that requested value was found in the input_list'''
    output_list=[]
    for percent in range(0,101):    #runs through each value between 0-100
        count=0                     #resets the counter
        for element in input_list:  #check each value in input_list
            if percent == element:
                count+=1            #if the value in input_list is the same as the percent then the count is increased
        output_list.append(count)   #and appends the count to output_list
    #print('prep arrays function return') #~~Evan Testing~~#
    #print(np.array(output_list)) #~~Evan Testing~~#
    return np.array(output_list)    #returns the output_list as an array



#Importing Data
writing_score_array=np.genfromtxt('Writing Scores.csv',skip_header = True, delimiter=',', encoding='utf-8', dtype=str)
math_score_array=np.genfromtxt('Reading Scores.csv',skip_header = True, delimiter=',', encoding='utf-8', dtype=str)
reading_score_array=np.genfromtxt('Math Scores.csv',skip_header = True, delimiter=',', encoding='utf-8', dtype=str)
#writing_score_array=np.loadtxt(open('.venv\Writing Scores.csv'),dtype={'names':('Student Number','Gender','Race','Parental Education','Lunch','Test Prep','Grade'),'formats':('f4','S20','S20','S20','S20','S20','f4')},delimiter=','or'\n',skiprows=1)
#math_scores_array=np.loadtxt(open('.venv\Math Scores.csv'),dtype={'names':('Student Number','Gender','Race','Parental Education','Lunch','Test Prep','Grade'),'formats':('f4','S20','S20','S20','S20','S20','f4')},delimiter=','or'\n',skiprows=1)
#reading_scores_array=np.loadtxt(open('.venv\Reading Scores.csv'),dtype={'names':('Student Number','Gender','Race','Parental Education','Lunch','Test Prep','Grade'),'formats':('f4','S20','S20','S20','S20','S20','f4')},delimiter=','or'\n',skiprows=1)

#exit clause for the menu loop
exit_clause = False
focus_group_choices={'Gender':['male','female'],'Ethnicity':['group A','group B','group C','group D','group E'],'Parent Education':["bachelor's degree",'some college',"master's degree","associate's degree",'high school'],'Lunch':['standard','free/reduced'],'Test Prep':['none','completed']}

#Main code block, everything below here is managing the menu class, print statments and calling graphing functions DO NOT ADD GRAPHING FUNCTIONS TO THIS FILE ITS ALREADY TOO LONG!!!!!!!!
#I made a new file for it :)
print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This is a school grade statistics analysis program.
You will be prompted with various choices including what data set you wish to analyze and how you want to analyze it.
Using this program you will be able to find any individual students grades for writing, reading or math.
You will also be able to find a students average across all three.
Other search criteria include:
Searching based off ethnicity, what students ate for lunch, parents schooling and whether test prep was completed.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')
while exit_clause == False:
    num_of_graphs = int(input('How many graphs would you like to compare? [1 or 2] -> '))
    if num_of_graphs not in [1,2]:
        print('Invalid entry, please try again')
        continue
    print()
    break
    

while exit_clause == False:
    see_scatterplot = input('would you like to see the scatterplot of all data? [yes or no] -> ').title()
    if see_scatterplot not in ['Yes','No']:
        print('Invalid entry, please try again')
        continue
    print()
    break

user_inputs_1 = menu()
while exit_clause == False:    
    user_inputs_1.request_inputs()
    exit_clause = user_inputs_1.print_menu_input()

exit_clause = False
if num_of_graphs == 2:
    print('Now select your second input options')
    user_inputs_2 = menu()
    while exit_clause == False:     
        user_inputs_2.request_inputs()
        exit_clause = user_inputs_2.print_menu_input()

computeing_array_1 = data_list_generator(focus_group_choices[user_inputs_1.focus_group],user_inputs_1.test_choice) #a list of only the useful values are created using the data_list_generator

list_of_calculated_values = []
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(f'Restults for {user_inputs_1.data_analysis}s of the focus groups in the {user_inputs_1.test_choice} test')
for group in focus_group_choices[user_inputs_1.focus_group]:
    calculated_data = analysis(sort_list(computeing_array_1, group), user_inputs_1.data_analysis)
    list_of_calculated_values.append(calculated_data)
    print(f'{user_inputs_1.data_analysis} for {group}: {list_of_calculated_values[focus_group_choices[user_inputs_1.focus_group].index(group)]:.2f}')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(f'{user_inputs_1.graph_choice} goes here')

if num_of_graphs == 2:
    computeing_array_2 = data_list_generator(focus_group_choices[user_inputs_2.focus_group],user_inputs_2.test_choice) #a list of only the useful values are created using the data_list_generator
    list_of_calculated_values = []
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'Restults for {user_inputs_2.data_analysis}s of the focus groups in the {user_inputs_2.test_choice} test')
    print('---------------------------------------------------------------------------')
    for group in focus_group_choices[user_inputs_2.focus_group]:
        calculated_data = analysis(sort_list(computeing_array_2, group), user_inputs_2.data_analysis)
        list_of_calculated_values.append(calculated_data)
        print(f'{user_inputs_2.data_analysis} for {group}: {list_of_calculated_values[focus_group_choices[user_inputs_2.focus_group].index(group)]:.2f}')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'{user_inputs_2.graph_choice} goes here')