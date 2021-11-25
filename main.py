import numpy as np
import matplotlib as plt

class menu:

    def __init__(self):
        self.time = 0
        self.country = ''
        self.data_analysis = ''
    

    def print_instructions(self):
        '''
        Summary: Function to print the instructions to the user
        
        Parameters: self
        
        Returns: None
        '''
        print(
'''
Where prompted please input the time period and country you wish to analyze.
Once finished please input the way you wish to analyze the data.
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
CHOSEN MENU OPTIONS: Time Period: {self.time}, Country: {self.country}, Analysis type {self.data_analysis}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
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


    def request_inputs(self, countries):
        '''
        Summary: Function to request the inputs for time period and country from ther user.
        
        Parameters: Self, List of countries 

        Returns: Tuple containing self.time and self.country
        '''
        valid_input = False
        while valid_input == False:
            self.time = input(f'Please input the time period you wish to analyze [2000-2006, 2007-2013, 2014-2020 or all] -> ') #Asks for an time period input
            print()
            if self.time not in ['2000-2006', '2007-2013', '2014-2020', 'All', 'all']:  #If the input is not in this list the program asks for a new one
                print('Invalid entry, please try again')
                print()
                continue
            valid_input = True

        valid_input = False
        while valid_input == False:
            self.country = input(f'Now please input the country you\'d wish to take data from -> ').title() #Asks for a country input
            print()
            if self.country not in countries:   #If the input is not within the countries list the program asks for a new one
                print('Invalid entry, please try agan')
                print()
                continue
            valid_input = True    
        return self.time, self.country


    def request_data_analysis(self):
        '''
        Summary: Function to request the input of a data analysis type for the section of data a user chose to analyze.

        Parameters: self

        Returns: self.data_analysis which is a variable containing the user's choice
        '''
        valid_input = False
        while valid_input == False:
            #Asks for a analysis type input
            self.data_analysis = input('Finally please input the way you\' wish to analyze the chosen data set. Options include: [Mean, Max, Min and Percent Change]. input here -> ')
            #If not part of this list the program asks for a new one
            if self.data_analysis not in ['Mean','mean','Max','max','Min','min','Percent Change','Percent change','percent Change','percent change']:
                print('Invalid entry, please try again')
                print()
                continue
            valid_input = True
        return self.data_analysis 


#Importing Data
array_2000_2006 = np.genfromtxt('populations 2000-2006.csv', skip_header=(True), delimiter=(','), dtype=None)   #Population data for 2000-2006
array_2007_2013 = np.genfromtxt('populations 2007-2013.csv', skip_header=(True), delimiter=(','), dtype=None)   #Population data for 2007-2013
array_2014_2020 = np.genfromtxt('populations 2014-2020.csv', skip_header=(True), delimiter=(','), dtype=None)   #Population data for 2014-2020


def array_generator(country_name, time_period):
    '''
    Summary: A function to scan through the attached CSV files and pull out the chosen data for the user.
    The function looks through the first column till it find a row starting with the country the user chose
    then copies that row and returns it so it may be used for computations later. 

    Parameters: User chosen country name, User chosen time period

    Returns: A single row array pretaining to the chosen country and time period
    '''
    func_dict={                                         #Dictionary containg keys based on inputed time periods and values for the file they pretain to
        '2000-2006':array_2000_2006,
        '2007-2013':array_2007_2013,
        '2014-2020':array_2014_2020}
    
    for i in range(len(func_dict[time_period][:,0])):   #For loop used to search through the first column till the specified country is found
        if country_name == func_dict[time_period][i,0]:
            return func_dict[time_period][i,1:]         #Returning the row for said country

#creating a list of valid countries from the first column of one of the CSV files (all countries are the same within them)
countries_list = []
for i in range(0,193): 
    countries_list.append(array_2000_2006[i,0])

#exit clause for the menu loop
exit_clause = False

user_inputs = menu()                                                            #Creating a menu class instance
user_inputs.print_instructions()                                                #Calling the print_instructions function
while exit_clause == False:                                                     #While loop that checks the boolean value that is returned by the function print_menu_input
    user_time_and_country = list(user_inputs.request_inputs(countries_list))    #Creates a list with the first enrty being the user chosen time and the second entry being the user chosen country
    user_analysis_choice = user_inputs.request_data_analysis()                  #Gets the users choice for analysis of the data
    exit_clause = user_inputs.print_menu_input()                                #Obtains the boolean value from whether the user was satisfied with their choice

#Creating the computing array
if user_time_and_country[0] == 'All' or user_time_and_country[0] == 'all': #checking if the user selected all for their time period
    #This line calls the array_generator function three times if the user selected all for their time period. 
    #Each call of the function uses the same country but each individual time period
    #These three arrays are then stored in the computing_array variable to be used for future computations
    computing_array = np.array([array_generator(user_time_and_country[1],'2000-2006' ),array_generator(user_time_and_country[1], '2007-2013'),array_generator(user_time_and_country[1], '2014-2020')])
else:
    computing_array = array_generator(user_time_and_country[1], user_time_and_country[0]) #If the user did not select all only one array is stored in computing array



#Okay Ethan I've set it up so that the user will choose the country and the analysis type
#The two variables you should need to use are "computing_array" (lines: 99 and 101) and "user_analysis_choice" (line: 95)
#I've also set up the four functions people are allowed to choose being mean, max, min, and percent change for when you want to work with the computng array
#have fun
#-Big Man