import numpy as np
import matplotlib as plt
from numpy.lib.function_base import append

class menu:

    def __init__(self):
        self.test_choice = ''
        self.focus_group = ''
        self.data_analysis = ''


    def print_instructions(self):
        '''
        Summary: Function to print the instructions to the user
        
        Parameters: self
        
        Returns: None
        '''
        print(
'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This is a school grade statistics analysis program.
You will be prompted with various choices including what data set you wish to analyze and how you want to analyze it.
Using this program you will be able to find any individual students grades for writing, reading or math.
You will also be able to find a students average across all three.
Other search criteria include:
Searching based off ethnicity, what students ate for lunch, parents schooling and whether test prep was completed.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')


    def print_menu_input(self):
        '''
        Summary: A function to ask the user if they are content with their selections of data and data 
        analysis type. If the user inputs no, the function will return False which is read by the program telling it to 
        re-request inputs. 
        
        Parameters: Self
        
        Returns: True or False
        '''
        print(f'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
CHOSEN MENU OPTIONS: Test score: {self.test_choice}, Focus group: {self.focus_group}, Analysis type {self.data_analysis}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
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
            self.data_analysis = input('Finally please input the way you would like to analyze the data you\'ve chosen [Highest Mark, Lowest Mark, Test Average] -> ').title() #Asks for how the user wishes to analyze the data
            print()
            if self.data_analysis not in ['Highest Mark', 'Lowest Mark', 'Test Average']:
                print('Invalid entry, please try again')
                print()
                continue
            break

        return self.test_choice, self.focus_group, self.data_analysis


    


#Importing Data
math_scores = np.genfromtxt('Math Scores.csv', skip_header=(True), delimiter=(','), dtype=str)   #Population data for 2000-2006
reading_scores = np.genfromtxt('Reading Scores.csv', skip_header=(True), delimiter=(','), dtype=str)   #Population data for 2007-2013
writing_scores = np.genfromtxt('Writing Scores.csv', skip_header=(True), delimiter=(','), dtype=str)   #Population data for 2014-2020

print(math_scores)
print(reading_scores)
print(writing_scores)


def array_generator(chosen_test, focus_group):
    '''
    Summary: A function to scan through the attached CSV files and pull out the chosen data for the user.
    The function looks through the first column till it find a row starting with the country the user chose
    then copies that row and returns it so it may be used for computations later. 

    Parameters: User chosen country name, User chosen time period

    Returns: A single row array pretaining to the chosen country and time period
    '''
    tests_dict={                                         #Dictionary containg keys based on inputed time periods and values for the file they pretain to
        'Math':math_scores,
        'Reading':reading_scores,
        'Writing':writing_scores}
    
    focus_dict={
        'Gender':1,
        'Ethnicity':2,
        'Parent Education':3,
        'Lunch':4,
        'Test Prep':5}
    
    computing_array = np.array([[' ',' ']])
    for i in range(len(tests_dict[chosen_test])):
        concatenating_array = np.array(tests_dict[chosen_test][i,focus_dict[focus_group]:7:(6-(focus_dict[focus_group]))],ndmin=2, dtype=None)
        computing_array = np.concatenate((computing_array, concatenating_array), axis=0)
    computing_array = np.delete(computing_array, 0, 0)
    print(computing_array)
    
    return computing_array



#exit clause for the menu loop
exit_clause = False

get_inputs = menu()                                         #Creating a menu class instance
get_inputs.print_instructions()                             #Calling the print_instructions function
while exit_clause == False:                                 #While loop that checks the boolean value that is returned by the function print_menu_input
    user_chosen_inputs = list(get_inputs.request_inputs())  #Creates a list with the first enrty being the user chosen test, second entry being the user chosen focus group and third being the data analysis type
    exit_clause = get_inputs.print_menu_input()             #Obtains the boolean value from whether the user was satisfied with their choice

#Creating the computing array
computing_array = array_generator(user_chosen_inputs[0], user_chosen_inputs[1]) 

if user_chosen_inputs[2] == 'Max':
    user_wanted_data = np.max(computing_array, axis=0)
elif user_chosen_inputs[2] == 'Min':
    user_wanted_data = np.min(computing_array, axis=0)
elif user_chosen_inputs[2] == 'Test Average':
    user_wanted_data = np.average(computing_array, axis=0)

print(user_wanted_data)

#Okay big man I've got the menu up, the computing array forming and what not but you now get to figure out how to deal with average max and min
#The computing array is still stored under computing_array and the data analysis type is index 2 of user_chosen_input
#The code block right above this was me attempting to do average max and min but it didn't work so give it shot and have fun with the graphs
#Also remind me to comment this shit later I just don't wanna deal with my shitty I key
#see ya nerd