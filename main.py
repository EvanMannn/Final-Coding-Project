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
        Summary: A function to ask the user if they are content with their selections of focus group, grade and data 
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
        Summary: Function to request the inputs for focus group and grade from the user.
        
        Parameters: Self, List of countries 

        Returns: Tuple containing self.group and self.grade
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
        'Math':math_scores_array,
        'Reading':reading_scores_array}

    output_list=[]
    for pos_1 in range(0,299):      #these two for loops goes through each value of a 299x7 array, first loop is for the 300 rows
        for pos_2 in range(0,6):    #and the second is for the 7 columns
            if array_dict[grade_array][pos_1][pos_2] in focus_group:                            #checks to see if the requested array (called using the array_dict) matches any of the bytes in the focus_group list
                #if true a list is made then appended to a larger list
                x=str(array_dict[grade_array][pos_1][pos_2]).replace("b'", "").replace("'","")  #first value of the smaller list is the found byte converted to a string and manually striped of it's byte notation ("b'")
                output_list.append([x,array_dict[grade_array][pos_1][6]])                       #second value is the grade in that row (found in column 6) then the list is appended into the larger list to be returned
    return output_list

def analysis(input_array,analysis_type):
    '''Summary: A function that preformes one of the possible calculations on an array: min, max, or mean

    Args:
        input_array (array): An array that will have numpy calculations preformed on it
        analysis_type (str): A string that must be one of the folowing: 'Min', 'Max', or 'Mean'. This is the calculation that the user would like to preform on the input_array

    Returns:
        int: the returned number from the requested operation done on the input_array'''
    if analysis_type=='Min':        #looks for which operation is requested
        return np.min(input_array)  #then preforms that operation and returns
    elif analysis_type=='Max':
        return np.max(input_array)
    else:
        return np.mean(input_array)

def sort_list(input_list,keyword):
    '''Summary: A function that goes through a list of lists (input_list) looking for the first value of each smaller list to equal the given keyword, if it is, the second value is appended to an output_list

    Args:
        input_list (list): A list where the values are lists whose values are a string and an int (example: =[['male', 80.0], ['female', 64.0]])
        keyword (byte): A byte that will be converted to a string then used by the program to find matching values within input_list

    Returns:
        output_list (list): a list of int values (grades) for each of the extracted students that meet the keyword'''
    output_list=[]
    for each_student in input_list:                                             #grabs each list within the input_list in a for loop
        if each_student[0]==str(keyword).replace("b'", "").replace("'",""):     #then checks if the first value of that list matches the keyword in string form and is manually striped of it's byte notation ("b'")
            output_list.append(each_student[1])                                 #if true the second value in the list is then appended to the output_list to be returned
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
    return np.array(output_list)    #returns the output_list as an array

def graph_figure(input_array,title,subplot_pos,estimation):
    modify_number=0
    x_values=np.array(range(len(input_array)))
    plt.subplot(len(focus_group_choices[input_list[0]]),2,(subplot_pos*2)+1)
    plt.plot(x_values,input_array, label=title)
    graphing_array=np.stack((x_values,input_array),axis=1)
    for estimation_value in range(1,estimation):
        print(estimation_value)
        for i, element in enumerate(graphing_array):
            if i == len(graphing_array)-estimation_value:
                break
            elif element[1]*1.5<graphing_array[round(i+estimation_value)][1] or element[1]>graphing_array[round(i-estimation_value)][1]*1.5:
                graphing_array[i] = [graphing_array[i][0],(graphing_array[round(i+estimation_value)][1]+graphing_array[round(i-estimation_value)][1])/2]
                modify_number+=1
    y_values=[i[1] for i in graphing_array]

    plt.subplot(len(focus_group_choices[input_list[0]]),2,(subplot_pos+1)*2)
    plt.plot(x_values,y_values, label=title)
    return modify_number
#Importing Data
writing_score_array=np.loadtxt(open('Writing Scores.csv'),dtype={'names':('Student Number','Gender','Race','Parental Education','Lunch','Test Prep','Grade'),'formats':('f4','S20','S20','S20','S20','S20','f4')},delimiter=','or'\n',skiprows=1)
math_scores_array=np.loadtxt(open('Math Scores.csv'),dtype={'names':('Student Number','Gender','Race','Parental Education','Lunch','Test Prep','Grade'),'formats':('f4','S20','S20','S20','S20','S20','f4')},delimiter=','or'\n',skiprows=1)
reading_scores_array=np.loadtxt(open('Reading Scores.csv'),dtype={'names':('Student Number','Gender','Race','Parental Education','Lunch','Test Prep','Grade'),'formats':('f4','S20','S20','S20','S20','S20','f4')},delimiter=','or'\n',skiprows=1)
#writing_score_array=np.loadtxt(open('.venv\Writing Scores.csv'),dtype={'names':('Student Number','Gender','Race','Parental Education','Lunch','Test Prep','Grade'),'formats':('f4','S20','S20','S20','S20','S20','f4')},delimiter=','or'\n',skiprows=1)
#math_scores_array=np.loadtxt(open('.venv\Math Scores.csv'),dtype={'names':('Student Number','Gender','Race','Parental Education','Lunch','Test Prep','Grade'),'formats':('f4','S20','S20','S20','S20','S20','f4')},delimiter=','or'\n',skiprows=1)
#reading_scores_array=np.loadtxt(open('.venv\Reading Scores.csv'),dtype={'names':('Student Number','Gender','Race','Parental Education','Lunch','Test Prep','Grade'),'formats':('f4','S20','S20','S20','S20','S20','f4')},delimiter=','or'\n',skiprows=1)

#exit clause for the menu loop
exit_clause = False

user_inputs = menu()                                                            #Creating a menu class instance
user_inputs.print_instructions()                                                #Calling the print_instructions function
while exit_clause == False:                                                     #While loop that checks the boolean value that is returned by the function print_menu_input
    input_list=user_inputs.request_inputs()
    user_analysis_choice = user_inputs.request_data_analysis()                  #Gets the users choice for analysis of the data
    exit_clause = user_inputs.print_menu_input()                                #Obtains the boolean value from whether the user was satisfied with their choice

#a dictionary for the program to call to receve a list of possible row values for each column (focus groups)
focus_group_choices={'Gender':[b'male',b'female'],'Race':[b'group A',b'group B',b'group C',b'group D',b'group E'],'Parental Education':[b'standard',b'free/reduced'],'Lunch':[b'standard',b'free/reduced'],'Test Prep':[b'none',b'completed']}

computeing_list = data_list_generator(focus_group_choices[input_list[0]],input_list[1]) #a list of only the useful values are created using the data_list_generator
all_computed_values=[]  #all_computed_values is a list of each of the calculated values, meaning if the mean for male and female, each of those would be appended to here
plt.figure(1)
for i in range(len(focus_group_choices[input_list[0]])):    #makes a loop for each of the possible rows for the focus group column (example: Gender has Male and Female so the loop will repeat twice)
    group=str(focus_group_choices[input_list[0]][i]).replace("b'", "").replace("'","").title()  #preps the group (ex: 'Male' or 'Female') to be printed
    print(f"The {user_analysis_choice} of {group}'s {input_list[1]} grade is: {analysis(sort_list(computeing_list,focus_group_choices[input_list[0]][i]),user_analysis_choice)}")
    #prints the analysis the user chose for each of the possible groups for the chosen test grade, 
    #then calculates the requested value by first sorting the list into it's needed form (ex:only males tested in math), then uses the analysis function to do the requested operation
    all_computed_values.append(analysis(sort_list(computeing_list,focus_group_choices[input_list[0]][i]),user_analysis_choice)) #the calculation step is repeated here to be appended to the list of all calculations (all_computed_values)
    #a subplot for this loop is created, the "i*2+1" makes these subplots only occur on the left side of the figure
print(f'The {user_analysis_choice} of All Groups is: {analysis(np.array(all_computed_values),user_analysis_choice)}\n') #then the operation for All groups is done using the all_computed_values list and the analysis function
estimation_value=int(input('Please enter the level of estimation for your graph (0 for no estimation and 10 for maximum) the recommended is 5: '))
for i in range(len(focus_group_choices[input_list[0]])):
    group=str(focus_group_choices[input_list[0]][i]).replace("b'", "").replace("'","").title()
    print(f"The estimated graph for {group}'s {input_list[1]} grade has {graph_figure(prep_arrays_for_graphing(sort_list(computeing_list,focus_group_choices[input_list[0]][i])),(f'{input_list[0]}'),i,estimation_value)}\n")
plt.show()
# NOV 29: sorry i was lazy and not commenting. Everything works rn, i had to change quite a bit for the new data to work but it's all good. The max min mean shit is done,
#i have the graphing set up, right now the graphs don't looks super pretty but i can fix that or if u wanna take a crack. I might notice that all of the graphs
#are all to the left of the figures, that's cuss i wanna interpolate the data on the right to make a nice swooping graph, if u get ideas for that u can fuck with it in the
#graph_figure() function, but the data for the graphs are totally correct and set up, all that's left is making the graphs look good and the interpolation.
#           <3
#also, where we import the csv there are some hashed code, don't delete those pls
#if ur csv's can't be located then feel free to fuck with the unhashed lines, the csv wasn't working for me so i had it set up to pull from my pc
#but it should be back to normal now

#NOV 30:
#most of the comments are now up, if ur confused just text me
#i was working on the estimating graph, it's looking great, i got somemore ideas for it to further improve it but that can wait, if u can work on making the UI look nicer
#and make the graphs look better that would be cool