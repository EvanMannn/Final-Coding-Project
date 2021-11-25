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
        Returns: none
        '''
        print(
'''
Where prompted please input the time period and country you wish to analyze.
Once finished please input the way you wish to analyze the data.
''')

    def print_menu_input(self):
        print(f'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
CHOSEN MENU OPTIONS: Time Period: {self.time}, Country: {self.country}, Analysis type {self.data_analysis}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
        print()
        valid_input = False
        while valid_input == False:
            yes_or_no = input('Are you satisfed with this input? (yes/no) -> ')
            print()
            if yes_or_no == 'no' or yes_or_no == 'No': return False
            elif yes_or_no == 'Yes' or yes_or_no == 'yes': return True
            else:
                print('Invalid entry, please try again')
                continue

    def request_inputs(self, countries):
        valid_input = False
        while valid_input == False:
            self.time = input(f'Please input the time period you wish to analyze [2000-2006, 2007-2013, 2014-2020 or all] -> ')
            print()
            if self.time not in ['2000-2006', '2007-2013', '2014-2020', 'All', 'all']:
                print('Invalid entry, please try again')
                print()
                continue
            valid_input = True

        valid_input = False
        while valid_input == False:
            self.country = input(f'Now please input the country you\'d wish to take data from -> ')
            print()
            if self.country not in countries:
                print('Invalid entry, please try agan')
                print()
                continue
            valid_input = True    
        return self.time, self.country

    def request_data_analysis(self):
        valid_input = False
        while valid_input == False:
            self.data_analysis = input('Finally please input the way you\' wish to analyze the chosen data set. Options include: [Mean, Max, Min and Percent Change]. input here -> ')
            if self.data_analysis not in ['Mean','mean','Max','max','Min','min','Percent Change','Percent change','percent Change','percent change']:
                print('Invalid entry, please try again')
                print()
                continue
            valid_input = True
        return self.data_analysis 

#Importing Data
array_2000_2006 = np.genfromtxt('populations 2000-2006.csv', skip_header=(True), delimiter=(','), dtype=str)
array_2007_2013 = np.genfromtxt('populations 2007-2013.csv', skip_header=(True), delimiter=(','), dtype=str)
array_2014_2020 = np.genfromtxt('populations 2014-2020.csv', skip_header=(True), delimiter=(','), dtype=str)

def array_generator(country_name, time_period):
    func_dict={
        '2000-2006':array_2000_2006,
        '2007-2013':array_2007_2013,
        '2014-2020':array_2014_2020}
    
    for i in range(len(func_dict[time_period][:,0])):
        if country_name == func_dict[time_period][i,0]:
            return func_dict[time_period][i,1:]

countries_list = []
for i in range(0,193):
    countries_list.append(array_2000_2006[i,0])


exit_clause = False

user_inputs = menu()
user_inputs.print_instructions()
while exit_clause == False:
    user_time_and_country = list(user_inputs.request_inputs(countries_list))
    user_analysis_choice = user_inputs.request_data_analysis()
    exit_clause = user_inputs.print_menu_input()

if user_time_and_country[0] == 'All' or user_time_and_country[0] == 'all':
    computing_array = np.array([array_generator(user_time_and_country[1],'2000-2006' ),array_generator(user_time_and_country[1], '2007-2013'),array_generator(user_time_and_country[1], '2014-2020')])
else:
    computing_array = array_generator(user_time_and_country[1], user_time_and_country[0])

#Okay Ethan I've set it up so that the user will choose the country and the analysis type
#The two variables you should need to use are "computing_array" (lines: 99 and 101) and "user_analysis_choice" (line: 95)
#I've also set up the four functions people are allowed to choose being mean, max, min, and percent change for when you want to work with the computng array
#have fun
#-Big Man