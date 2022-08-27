"""this program helps individuals with their finances by providing four useful tools. 
1. A calculator that helps to determine the duration or amount needed to save for a future purchase. 
2. A calculator that helps to determine the duration it will take to pay off a previous purchase.
3. A process that creates a spending plan based off of an individual's income. 
4. A simple estimation for yearly taxes. 
"""

def future_purchase(): 
    return None 
  
def previous_purchase_payoff():
    return None 

def spending_plan():
    return None

def estimated_taxes():
    return None 
  
def return_to_homepage(): 
    user_decision = input('''You have successfully completed the use of one of our finance tools. Would you like to return to our homepage to use another tool? 
          Yes/No: ''')
    if user_decision.lower() == 'yes' or 'y':
        continue 
        
    elif user_decision.lower() == 'no' or 'n':
        current_status = False 
        return current_status 
    else: 
        print('Your input was not a yes or no')
        print('We will return you to the homepage. \n\n')
    

#this is the home page of the project which users will select the tool they would like to use 
current_status = True 
while current_status == True: 
    tool_selection = input('''We have four useful tools you can use. Please select the number of which tool you 
    would like to use:
    1. 
    2. 
    3. 
    4. 
    5. To EXIT '''
    try: 
        tool_selection = int(tool_selection)
                           
    except: 
        print('There was a problem with your entry. Please ensure you are entering the numerial. For example: 2 \n\n')
        
    try:          
        if tool_selection == 1:
            future_purchase()
                     
        elif tool_selection == 2: 
            previous_purchase_payoff()               
                           
        elif tool_selection == 3: 
            spending_plan()               
              
        elif tool_selection == 4:                   
            estimated_taxes()  
                           
        elif tool_selection == 5: 
            current_status = False 
            break 
                           
        else:
            print('It looks like you selected a number other than our five options. Please enter a number for the tool you would like to use.\n\n')  
                           
     except: 
         print('There was a problem starting the tool. Please try again.')
