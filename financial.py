"""this program helps individuals with their finances by providing four useful tools. 
1. A calculator that helps to determine the duration or amount needed to save for a future purchase. 
2. A calculator that helps to determine the duration it will take to pay off a previous purchase.
3. A process that creates a spending plan based off of an individual's income. 
4. A simple estimation for yearly taxes. 
"""
import re

federal_tax_bracket = {'single': , {10: 10275,
                                    12: 41775,
                                    22: 89075,
                                    24: 170050,
                                    32: 215950,
                                    35: 539900,
                                    37: None
                                   }
                       'jointly': {10: 20550,
                                 12: 83550,
                                 22: 178150,
                                 24: 340100,
                                 32: 431900,
                                 35: 647850,
                                 37: None
                                 },
                       'seperate': {10: ,
                                    12: ,
                                    22: ,
                                    24: ,
                                    32: ,
                                    35: ,
                                    37: None
                                   },
                       'head of house':{10: ,
                                        12: ,
                                        22: ,
                                        24: ,
                                        32: ,
                                        35: ,
                                        37: None
                                        }
                      }

state_tax_bracket = {'alamaba' : {'single': , {10: 10275,
                                    12: 41775,
                                    22: 89075,
                                    24: 170050,
                                    32: 215950,
                                    35: 539900,
                                    37: None
                                   }
                       'jointly': {10: 20550,
                                 12: 83550,
                                 22: 178150,
                                 24: 340100,
                                 32: 431900,
                                 35: 647850,
                                 37: None
                                 },
                       'seperate': {10: ,
                                    12: ,
                                    22: ,
                                    24: ,
                                    32: ,
                                    35: ,
                                    37: None
                                   },
                       'head of house':{10: ,
                                        12: ,
                                        22: ,
                                        24: ,
                                        32: ,
                                        35: ,
                                        37: None
                                        }
                      },
                     'alamaba' : {'single': , {10: 10275,
                                    12: 41775,
                                    22: 89075,
                                    24: 170050,
                                    32: 215950,
                                    35: 539900,
                                    37: None
                                   }
                       'jointly': {10: 20550,
                                 12: 83550,
                                 22: 178150,
                                 24: 340100,
                                 32: 431900,
                                 35: 647850,
                                 37: None
                                 },
                       'seperate': {10: ,
                                    12: ,
                                    22: ,
                                    24: ,
                                    32: ,
                                    35: ,
                                    37: None
                                   },
                       'head of house':{10: ,
                                        12: ,
                                        22: ,
                                        24: ,
                                        32: ,
                                        35: ,
                                        37: None
                                        }
                      },
                     'alamaba' : {'single': , {10: 10275,
                                    12: 41775,
                                    22: 89075,
                                    24: 170050,
                                    32: 215950,
                                    35: 539900,
                                    37: None
                                   }
                       'jointly': {10: 20550,
                                 12: 83550,
                                 22: 178150,
                                 24: 340100,
                                 32: 431900,
                                 35: 647850,
                                 37: None
                                 },
                       'seperate': {10: ,
                                    12: ,
                                    22: ,
                                    24: ,
                                    32: ,
                                    35: ,
                                    37: None
                                   },
                       'head of house':{10: ,
                                        12: ,
                                        22: ,
                                        24: ,
                                        32: ,
                                        35: ,
                                        37: None
                                        }
                      },
                     'alamaba' : {'single': , {10: 10275,
                                    12: 41775,
                                    22: 89075,
                                    24: 170050,
                                    32: 215950,
                                    35: 539900,
                                    37: None
                                   }
                       'jointly': {10: 20550,
                                 12: 83550,
                                 22: 178150,
                                 24: 340100,
                                 32: 431900,
                                 35: 647850,
                                 37: None
                                 },
                       'seperate': {10: ,
                                    12: ,
                                    22: ,
                                    24: ,
                                    32: ,
                                    35: ,
                                    37: None
                                   },
                       'head of house':{10: ,
                                        12: ,
                                        22: ,
                                        24: ,
                                        32: ,
                                        35: ,
                                        37: None
                                        }
                      },
                     'alamaba' : {'single': , {10: 10275,
                                    12: 41775,
                                    22: 89075,
                                    24: 170050,
                                    32: 215950,
                                    35: 539900,
                                    37: None
                                   }
                       'jointly': {10: 20550,
                                 12: 83550,
                                 22: 178150,
                                 24: 340100,
                                 32: 431900,
                                 35: 647850,
                                 37: None
                                 },
                       'seperate': {10: ,
                                    12: ,
                                    22: ,
                                    24: ,
                                    32: ,
                                    35: ,
                                    37: None
                                   },
                       'head of house':{10: ,
                                        12: ,
                                        22: ,
                                        24: ,
                                        32: ,
                                        35: ,
                                        37: None
                                        }
                      },
                     'alamaba' : {'single': , {10: 10275,
                                    12: 41775,
                                    22: 89075,
                                    24: 170050,
                                    32: 215950,
                                    35: 539900,
                                    37: None
                                   }
                       'jointly': {10: 20550,
                                 12: 83550,
                                 22: 178150,
                                 24: 340100,
                                 32: 431900,
                                 35: 647850,
                                 37: None
                                 },
                       'seperate': {10: ,
                                    12: ,
                                    22: ,
                                    24: ,
                                    32: ,
                                    35: ,
                                    37: None
                                   },
                       'head of house':{10: ,
                                        12: ,
                                        22: ,
                                        24: ,
                                        32: ,
                                        35: ,
                                        37: None
                                        }
                      },
                     'alamaba' : {'single': , {10: 10275,
                                    12: 41775,
                                    22: 89075,
                                    24: 170050,
                                    32: 215950,
                                    35: 539900,
                                    37: None
                                   }
                       'jointly': {10: 20550,
                                 12: 83550,
                                 22: 178150,
                                 24: 340100,
                                 32: 431900,
                                 35: 647850,
                                 37: None
                                 },
                       'seperate': {10: ,
                                    12: ,
                                    22: ,
                                    24: ,
                                    32: ,
                                    35: ,
                                    37: None
                                   },
                       'head of house':{10: ,
                                        12: ,
                                        22: ,
                                        24: ,
                                        32: ,
                                        35: ,
                                        37: None
                                        }
                      },
                     'alamaba' : {'single': , {10: 10275,
                                    12: 41775,
                                    22: 89075,
                                    24: 170050,
                                    32: 215950,
                                    35: 539900,
                                    37: None
                                   }
                       'jointly': {10: 20550,
                                 12: 83550,
                                 22: 178150,
                                 24: 340100,
                                 32: 431900,
                                 35: 647850,
                                 37: None
                                 },
                       'seperate': {10: ,
                                    12: ,
                                    22: ,
                                    24: ,
                                    32: ,
                                    35: ,
                                    37: None
                                   },
                       'head of house':{10: ,
                                        12: ,
                                        22: ,
                                        24: ,
                                        32: ,
                                        35: ,
                                        37: None
                                        }
                      },
                     'alamaba' : {'single': , {10: 10275,
                                    12: 41775,
                                    22: 89075,
                                    24: 170050,
                                    32: 215950,
                                    35: 539900,
                                    37: None
                                   }
                       'jointly': {10: 20550,
                                 12: 83550,
                                 22: 178150,
                                 24: 340100,
                                 32: 431900,
                                 35: 647850,
                                 37: None
                                 },
                       'seperate': {10: ,
                                    12: ,
                                    22: ,
                                    24: ,
                                    32: ,
                                    35: ,
                                    37: None
                                   },
                       'head of house':{10: ,
                                        12: ,
                                        22: ,
                                        24: ,
                                        32: ,
                                        35: ,
                                        37: None
                                        }
                      },
                     
                     

def future_purchase(): 
    print('let\'s work on a game plan to save up for a future purchase!')
    check_purchase_amount = True
    while check_purchase_amount == True: 
        purchase_amount = input('How much does the future purchase cost?: $')
        try: 
            amount_to_purchase = int(purchase_amount)
            check_purchase_amount = False
            break
        except: 
            print('Please ensure that you enter the mount of the purchase in numerical form')
    
    check_decide_path = True 
    while check_decide_path == True: 
        decide_path = input(f'''Now that we know your purchase will be ${amount_to_purchase} we can decide how to plan for it.\n
        Would you like to save by:\n
        -A fixed amount of savings each month. Please enter fixed.
            -or-
        -A timeline. Please enter timeline.\n
        ''')
        if re.search('fixed',decide_path.lower()) != None: 
            #enter fixed monthly savings pathway
            print('A fixed monthly saving is a great plan for future payments.')
            check_monthly_savings = True: 
            while check_monthly_savings == True: 
                monthly_savings = input('How much would you like to save each month?: $')
                try: 
                    monthly_savings = int(monthly_savings)
                except: 
                    print('Please enter the amount you will be saving each month is numerical form. Example: 300.\n')
            amount_of_months_to_save = amount_to_purchase/monthly_savings
            output_name = f'You will be able to make a purchase of ${amount_to_purchase} in {amount_of_months_to_save} by saving ${monthly_savings} each month.'
            check_decide_path = False 
            break
            
        elif re.search('timeline', decide_path.lower()) != None:
            #enter timeline saving pathway
            print('Let\'s work on finding how much money you need to save a month,')
            check_months_to_save = True
            while check_months_to_save == True:
                months_to_save = input('')
                try: 
                    months_to_save = int(months_to_save)
                except: 
                    print('Please enter the amount of months you would like to make the purchase in numerical form. Example: 15\n')
                amount_to_save_monthly = amount_to_purchase/months_to_save
                output_name = f'You will be able to make a purchase of ${amount_to_purchase} by saving ${months_to_save} in {months_to_save}months.'
                check_months_to_save = False
                break 
                
            check_decide_path = False
            break
            
        else:
            print('Please ensure that you enter either fixed or timeline.\n\n')
            continue
    return output_name  
  
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
    1. Plan for a future purchase
    2. Plan to pay off a previous purchase
    3. Create a spending plan
    4. Estimate the amount of taxes you will pay
    5. To EXIT '''
    try: 
        tool_selection = int(tool_selection)
                           
    except: 
        print('There was a problem with your entry. Please ensure you are entering the numerial. For example: 2 \n\n')
        
    try:          
        if tool_selection == 1:
            statement_to_print = future_purchase()
            print(f'{statement_to_print}')
            return_to_homepage()
                     
        elif tool_selection == 2: 
            previous_purchase_payoff() 
            print('Currently under reconstruction. Please try again September 7th\n')
            return_to_homepage()
                           
        elif tool_selection == 3: 
            spending_plan()     
            print('Currently under reconstruction. Please try again September 7th\n')
            return_to_homepage()
              
        elif tool_selection == 4:                   
            estimated_taxes()
            print('Currently under reconstruction. Please try again September 7th\n')               
            return_to_homepage()
                           
        elif tool_selection == 5: 
            current_status = False 
            break 
                           
        else:
            print('It looks like you selected a number other than our five options. Please enter a number for the tool you would like to use.\n\n')  
                           
     except: 
         print('There was a problem starting the tool. Please try again.')
