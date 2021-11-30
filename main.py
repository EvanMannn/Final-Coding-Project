import numpy as np
import matplotlib.pyplot as plt

class menu:

    def __init__(self):
        self.grade = ''
        self.group = ''
        self.data_analysis = ''
    

    def print_instructions(self):
        '''
        Summary: Function to print the instructions to the user
        
        Parameters: self
        
        Returns: None
        '''
        print(
'''
Where prompted please input a focus group and test type.
Once finished please input the grade you would like to compare.
''')


    def print_menu_input(self):
        '''
        Summary: A function to ask the user if they are content with their selections of time period, country and data 
        analysis type. If the user inputs no, the function will return False which is read by the program telling it to 
        re-request inputs. 
        
        Parameters: Self
        
        Returns: True or False
        '''
        print(f'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
CHOSEN MENU OPTIONS: Student Focus Group: {self.group}, Grade: {self.grade}, Analysis type {self.data_analysis}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
        print()
        valid_input = False
        while valid_input == False:
            yes_or_no = input('Are you satisfed with this input? (yes/no) -> ').title() #Asks if the user is ok with their choice
            print()
            if yes_or_no == 'No' or yes_or_no == 'N': return False             #If not return False
            elif yes_or_no == 'Yes' or yes_or_no == 'Y': return True          #If yes return True
            else:
                print('Invalid entry, please try again')
                continue


    def request_inputs(self):
        '''
        Summary: Function to request the inputs for time period and country from the user.
        
        Parameters: Self, List of countries 

        Returns: Tuple containing self.time and self.country
        '''
        valid_input = False
        while valid_input == False:
            self.group = input(f'Please input the time period you wish to analyze [Gender, Race, Parental Education, Lunch, or Test Prep] -> ').title() #Asks for an time period input
            print()
            if (self.group) not in ['Gender','Race','Parental Education','Lunch','Test Prep']:  #If the input is not in this list the program asks for a new one
                print('Invalid entry, please try again')
                print()
                continue
            valid_input = True

        valid_input = False
        while valid_input == False:
            self.grade = input(f'Now please input the test grade you\'d wish to take data from [Math, Writing, or Reading]-> ').title() #Asks for a country input
            print()
            if self.grade not in ['Math','Writing','Reading']:   #If the input is not within the countries list the program asks for a new one
                print('Invalid entry, please try again')
                print()
                continue
            valid_input = True    
        return [self.group,self.grade]


    def request_data_analysis(self):
        '''
        Summary: Function to request the input of a data analysis type for the section of data a user chose to analyze.

        Parameters: self

        Returns: self.data_analysis which is a variable containing the user's choice
        '''
        valid_input = False
        while valid_input == False:
            #Asks for a analysis type input
            self.data_analysis = input('Finally please input the way you\' wish to analyze the chosen data set. Options include: [Mean, Max, Min and Percent Change]. input here -> ').title()
            #If not part of this list the program asks for a new one
            if self.data_analysis not in ['Mean','Max','Min','Percent Change']:
                print('Invalid entry, please try again')
                print()
                continue
            valid_input = True
        return self.data_analysis 

def array_generator(focus_group, grade_array):
    '''
    Summary: A function to scan through the attached CSV files and pull out the chosen data for the user.
    The function looks through the first column till it find a row starting with the country the user chose
    then copies that row and returns it so it may be used for computations later. 

    Parameters: User chosen country name, User chosen time period

    Returns: A single row array pretaining to the chosen country and time period
    '''
    func_dict={                                         #Dictionary containg keys based on inputed time periods and values for the file they pretain to
        'Writing':writing_score_array,
        'Math':math_scores_array,
        'Reading':reading_scores_array}
    '''
    for i in range(len(func_dict[input_grade][:,0])):   #For loop used to search through the first column till the specified country is found
        if focus_group == func_dict[input_grade][i,0]:
            return func_dict[input_grade][i,1:]         #Returning the row for said country
    '''
    output_list=[]
    for pos_1 in range(0,299):
        for pos_2 in range(0,6):
            if func_dict[grade_array][pos_1][pos_2] in focus_group:
                x=str(func_dict[grade_array][pos_1][pos_2]).replace("b'", "").replace("'","")
                output_list.append([x,func_dict[grade_array][pos_1][6]])
    return output_list

def analysis(input_array,analysis_type):
    if analysis_type=='Min':
        return np.min(input_array)
    elif analysis_type=='Max':
        return np.max(input_array)
    else:
        return np.mean(input_array)

def sort_array(input_list,keyword):
    output_list=[]
    for each_student in input_list:
        if each_student[0]==str(keyword).replace("b'", "").replace("'",""):
            output_list.append(each_student[1])
    return output_list

def prep_arrays_for_graphing(input_list):
    output_list=[]
    for percent in range(0,100):
        count=0
        for element in input_list:
            if percent == element:
                count+=1
        output_list.append(count)
    return np.array(output_list)

def graph_figure(input_array,title,subplot_pos):
    plt.plot(np.array(range(100)),input_array, label=title)
#Importing Data
writing_score_array=np.loadtxt(open('Writing Scores.csv'),dtype={'names':('Student Number','Gender','Race','Parental Education','Lunch','Test Prep','Grade'),'formats':('f4','S20','S20','S20','S20','S20','f4')},delimiter=','or'\n',skiprows=1)
math_scores_array=np.loadtxt(open('Math Scores.csv'),dtype={'names':('Student Number','Gender','Race','Parental Education','Lunch','Test Prep','Grade'),'formats':('f4','S20','S20','S20','S20','S20','f4')},delimiter=','or'\n',skiprows=1)
reading_scores_array=np.loadtxt(open('Reading Scores.csv'),dtype={'names':('Student Number','Gender','Race','Parental Education','Lunch','Test Prep','Grade'),'formats':('f4','S20','S20','S20','S20','S20','f4')},delimiter=','or'\n',skiprows=1)
#writing_score_array=np.loadtxt(open('.venv\Writing Scores.csv'),dtype={'names':('Student Number','Gender','Race','Parental Education','Lunch','Test Prep','Grade'),'formats':('f4','S20','S20','S20','S20','S20','f4')},delimiter=','or'\n',skiprows=1)
#math_scores_array=np.loadtxt(open('.venv\Math Scores.csv'),dtype={'names':('Student Number','Gender','Race','Parental Education','Lunch','Test Prep','Grade'),'formats':('f4','S20','S20','S20','S20','S20','f4')},delimiter=','or'\n',skiprows=1)
#reading_scores_array=np.loadtxt(open('.venv\Reading Scores.csv'),dtype={'names':('Student Number','Gender','Race','Parental Education','Lunch','Test Prep','Grade'),'formats':('f4','S20','S20','S20','S20','S20','f4')},delimiter=','or'\n',skiprows=1)

#creates the list of students (since they are numbered 1-300 we can just use a range function ;)
list_of_students=[i for i in range(1,301)]

#exit clause for the menu loop
exit_clause = False

user_inputs = menu()                                                            #Creating a menu class instance
user_inputs.print_instructions()                                                #Calling the print_instructions function
while exit_clause == False:                                                     #While loop that checks the boolean value that is returned by the function print_menu_input
    input_list=user_inputs.request_inputs()
    user_analysis_choice = user_inputs.request_data_analysis()                  #Gets the users choice for analysis of the data
    exit_clause = user_inputs.print_menu_input()                                #Obtains the boolean value from whether the user was satisfied with their choice

focus_group_choices={'Gender':[b'male',b'female'],'Race':[b'group A',b'group B',b'group C',b'group D',b'group E'],'Parental Education':[b'standard',b'free/reduced'],'Lunch':[b'standard',b'free/reduced'],'Test Prep':[b'none',b'completed']}

#Creating the computing list
computeing_list = array_generator(focus_group_choices[input_list[0]],input_list[1]) #If the user did not select all only one array is stored in computing array
all_computed_values=[]
plt.figure(1)
x=str(input_list[1]).replace("b'", "").replace("'","")
for i in range(len(focus_group_choices[input_list[0]])):
    y=str(focus_group_choices[input_list[0]][i]).replace("b'", "").replace("'","").title()
    print(f"The {user_analysis_choice} of {y}'s {x} grade is: {analysis(sort_array(computeing_list,focus_group_choices[input_list[0]][i]),user_analysis_choice)}")
    all_computed_values.append(analysis(sort_array(computeing_list,focus_group_choices[input_list[0]][i]),user_analysis_choice))
    plt.subplot(len(focus_group_choices[input_list[0]]),2,i*2+1)
    graph_figure(prep_arrays_for_graphing(sort_array(computeing_list,focus_group_choices[input_list[0]][i])),(f'{input_list[0]}'),i)
print(f'The {user_analysis_choice} of All Groups is: {analysis(np.array(all_computed_values),user_analysis_choice)}\n')
plt.show()

#sorry i was lazy and not commenting. Everything works rn, i had to change quite a bit for the new data to work but it's all good. The max min mean shit is done,
#i have the graphing set up, right now the graphs don't looks super pretty but i can fix that or if u wanna take a crack. I might notice that all of the graphs
#are all to the left of the figures, that's cuss i wanna interpolate the data on the right to make a nice swooping graph, if u get ideas for that u can fuck with it in the
#graph_figure() function, but the data for the graphs are totally correct and set up, all that's left is making the graphs look good and the interpolation.
#           <3
#also, where we import the csv there are some hashed code, don't delete those pls
#if ur csv's can't be located then feel free to fuck with the unhashed lines, the csv wasn't working for me so i had it set up to pull from my pc
#but it should be back to normal now