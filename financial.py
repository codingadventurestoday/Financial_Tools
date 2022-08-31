"""this program helps individuals with their finances by providing four useful tools. 
1. A calculator that helps to determine the duration or amount needed to save for a future purchase. 
2. A calculator that helps to determine the duration it will take to pay off a previous purchase.
3. A process that creates a spending plan based off of an individual's income. 
4. A simple estimation for yearly taxes. 
"""
import re

federal_deducibles = {'single': 12950,
                      'jointly': 25900,
                      'seperate': 12950,
                      'head of household': 19400}


federal_tax_bracket = {'single': , {'tier 1': adjusted_federal_income*.1,
                                    'tier 2': 1027.5+(adjusted_federal_income-10275)*.12,
                                    'tier 3': 4807.5+(adjusted_federal_income-41775)*.22,
                                    'tier 4': 15213.5+(adjusted_federal_income-89075)*.24,
                                    'tier 5': 34647.5+(adjusted_federal_income-170050)*.32,
                                    'tier 6': 49335.5+(adjusted_federal_income-215950)*.35,
                                    'tier 7': 113382.5+(adjusted_federal_income-539900)*.37
                                   }
                       'jointly': {'tier 1': adjusted_federal_income*.10,
                                  'tier 2': +(adjusted_federal_income-20550)*.12,
                                  'tier 3': +(adjusted_federal_income-83550)*.22,
                                  'tier 4': +(adjusted_federal_income-178150)*.34,
                                  'tier 5': +(adjusted_federal_income-340100)*.32,
                                  'tier 6': +(adjusted_federal_income-431900)*.35,
                                  'tier 7': +(adjusted_federal_income-647850)*.37
                                 },
                       'seperate': {'tier 1': adjusted_federal_income*.10,
                                    'tier 2': 1027.5+(adjusted_federal_income-10275)*.12,
                                    'tier 3': 4807.5+(adjusted_federal_income-41775)*.22,
                                    'tier 4': 15213.5+(adjusted_federal_income-89075)*.24,
                                    'tier 5': 34647.5+(adjusted_federal_income-170050)*.32,
                                    'tier 6': +(adjusted_federal_income-215950)*.35,
                                    'tier 7': +(adjusted_federal_income-323925)*.37
                                   },
                       'head of house':{'tier 1': adjusted_federal_income*.10,
                                        'tier 2': +(adjusted_federal_income-14650)*.12,
                                        'tier 3': +(adjusted_federal_income-55900)*.22,
                                        'tier 4': +(adjusted_federal_income-89050)*.24,
                                        'tier 5': +(adjusted_federal_income-170050)*.32,
                                        'tier 6': +(adjusted_federal_income-215950)*.35,
                                        'tier 17': +(adjusted_federal_income-53900)*.37
                                        }
                      }

state_tax_bracket = {'alabama' : {'single': , {'tier 1': adjusted_state_income*..02,
                                               'tier 2': +(adjusted_state_income-)*.04,
                                               'tier 3': +(adjusted_state_income-)*.05},
                                  'jointly': {'tier 1': +(adjusted_state_income-)*.12,
                                              'tier 2': +(adjusted_state_income-)*.12,
                                              'tier 3': +(adjusted_state_income-)*.12},
                                  'seperate': {'tier 1': +(adjusted_state_income-)*.12,
                                               'tier 2': +(adjusted_state_income-)*.12,
                                               'tier 3': +(adjusted_state_income-)*.12},
                                  'head of house':{'tier 1': +(adjusted_state_income-)*.12,
                                                   'tier 2': +(adjusted_state_income-)*.12,
                                                   'tier 3': +(adjusted_state_income-)*.12}
                                  }
                     'arizona':{'single': , {'tier 1': adjusted_state_income*.1,
                                             'tier 2': +(adjusted_state_income-)*.12,
                                             'tier 3': +(adjusted_state_income-)*.12,
                                             'tier 4': +(adjusted_state_income-)*.12},
                                'jointly': {'tier 1': +(adjusted_state_income-)*.12,
                                            'tier 2': +(adjusted_state_income-)*.12,
                                            'tier 3': +(adjusted_state_income-)*.12,
                                            'tier 4': +(adjusted_state_income-)*.12},
                                'seperate': {'tier 1': +(adjusted_state_income-)*.12,
                                             'tier 2': +(adjusted_state_income-)*.12,
                                             'tier 3': +(adjusted_state_income-)*.12,
                                             'tier 4': +(adjusted_state_income-)*.12},
                                'head of house':{'tier 1': +(adjusted_state_income-)*.12,
                                                 'tier 2': +(adjusted_state_income-)*.12,
                                                 'tier 3': +(adjusted_state_income-)*.12,
                                                 'tier 4': +(adjusted_state_income-)*.12}
                                 } ,
                     'arkansas': {'single': , {'tier 1': adjusted_state_income*.1,
                                               'tier 2': +(adjusted_state_income-)*.12,
                                               'tier 3': +(adjusted_state_income-)*.12},
                                  'jointly': {'tier 1': +(adjusted_state_income-)*.12,
                                              'tier 2': +(adjusted_state_income-)*.12,
                                              'tier 3': +(adjusted_state_income-)*.12},
                                  'seperate': {'tier 1': +(adjusted_state_income-)*.12,
                                               'tier 2': +(adjusted_state_income-)*.12,
                                               'tier 3': +(adjusted_state_income-)*.12},
                                  'head of house':{'tier 1': +(adjusted_state_income-)*.12,
                                                   'tier 2': +(adjusted_state_income-)*.12,
                                                   'tier 3': +(adjusted_state_income-)*.12}
                                  },
                     'california': {'single': , {'tier 1': adjusted_state_income*.1,
                                                 'tier 2': +(adjusted_state_income-)*.12,
                                                 'tier 3': +(adjusted_state_income-)*.12,
                                                 'tier 4': +(adjusted_state_income-)*.12,
                                                 'tier 5': +(adjusted_state_income-)*.12,
                                                 'tier 6': +(adjusted_state_income-)*.12,
                                                 'tier 7': +(adjusted_state_income-)*.12,
                                                 'tier 8': +(adjusted_state_income-)*.12,
                                                 'tier 9': +(adjusted_state_income-)*.12},
                                    'jointly': {'tier 1': +(adjusted_state_income-)*.12,
                                                'tier 2': +(adjusted_state_income-)*.12,
                                                'tier 3': +(adjusted_state_income-)*.12,
                                                'tier 4': +(adjusted_state_income-)*.12,
                                                'tier 5': +(adjusted_state_income-)*.12,
                                                'tier 6': +(adjusted_state_income-)*.12,
                                                'tier 7': +(adjusted_state_income-)*.12,
                                                'tier 8': +(adjusted_state_income-)*.12,
                                                'tier 9': +(adjusted_state_income-)*.12},
                                    'seperate': {'tier 1': +(adjusted_state_income-)*.12,
                                                 'tier 2': +(adjusted_state_income-)*.12,
                                                 'tier 3': +(adjusted_state_income-)*.12,
                                                 'tier 4': +(adjusted_state_income-)*.12,
                                                 'tier 5': +(adjusted_state_income-)*.12,
                                                 'tier 6': +(adjusted_state_income-)*.12,
                                                 'tier 7': +(adjusted_state_income-)*.12,
                                                 'tier 8': +(adjusted_state_income-)*.12,
                                                 'tier 9': +(adjusted_state_income-)*.12},
                                   'head of house':{'tier 1': +(adjusted_state_income-)*.12,
                                                    'tier 2': +(adjusted_state_income-)*.12,
                                                    'tier 3': +(adjusted_state_income-)*.12,
                                                    'tier 4': +(adjusted_state_income-)*.12,
                                                    'tier 5': +(adjusted_state_income-)*.12,
                                                    'tier 6': +(adjusted_state_income-)*.12,
                                                    'tier 7': +(adjusted_state_income-)*.12,
                                                    'tier 8': +(adjusted_state_income-)*.12,
                                                    'tier 9': +(adjusted_state_income-)*.12}
                                  }, 
                     'colorado': adjusted_state_income*.0455, 
                     'connecticut': {'single': , {'tier 1': adjusted_state_income*.1,
                                                  'tier 2': +(adjusted_state_income-)*.12,
                                                  'tier 3': +(adjusted_state_income-)*.12,
                                                  'tier 4': +(adjusted_state_income-)*.12,
                                                  'tier 5': +(adjusted_state_income-)*.12,
                                                  'tier 6': +(adjusted_state_income-)*.12,
                                                  'tier 7': +(adjusted_state_income-)*.12},
                                    'jointly': {'tier 1': +(adjusted_state_income-)*.12,
                                                'tier 2': +(adjusted_state_income-)*.12,
                                                'tier 3': +(adjusted_state_income-)*.12,
                                                'tier 4': +(adjusted_state_income-)*.12,
                                                'tier 5': +(adjusted_state_income-)*.12,
                                                'tier 6': +(adjusted_state_income-)*.12,
                                                'tier 7': +(adjusted_state_income-)*.12},
                                    'seperate': {'tier 1': +(adjusted_state_income-)*.12,
                                                 'tier 2': +(adjusted_state_income-)*.12,
                                                 'tier 3': +(adjusted_state_income-)*.12,
                                                 'tier 4': +(adjusted_state_income-)*.12,
                                                 'tier 5': +(adjusted_state_income-)*.12,
                                                 'tier 6': +(adjusted_state_income-)*.12,
                                                 'tier 7': +(adjusted_state_income-)*.12},
                                    'head of house':{'tier 1': +(adjusted_state_income-)*.12,
                                                     'tier 2': +(adjusted_state_income-)*.12,
                                                     'tier 3': +(adjusted_state_income-)*.12,
                                                     'tier 4': +(adjusted_state_income-)*.12,
                                                     'tier 5': +(adjusted_state_income-)*.12,
                                                     'tier 6': +(adjusted_state_income-)*.12,
                                                     'tier 7': +(adjusted_state_income-)*.12}
                                     }, 
                     'delaware': {'single': , {'tier 1': adjusted_state_income*.1,
                                               'tier 2': +(adjusted_state_income-)*.12,
                                               'tier 3': +(adjusted_state_income-)*.12,
                                               'tier 4': +(adjusted_state_income-)*.12,
                                               'tier 5': +(adjusted_state_income-)*.12,
                                               'tier 6': +(adjusted_state_income-)*.12,
                                               'tier 7': +(adjusted_state_income-)*.12},
                                  'jointly': {'tier 1': +(adjusted_state_income-)*.12,
                                              'tier 2': +(adjusted_state_income-)*.12,
                                              'tier 3': +(adjusted_state_income-)*.12,
                                              'tier 4': +(adjusted_state_income-)*.12,
                                              'tier 5': +(adjusted_state_income-)*.12,
                                              'tier 6': +(adjusted_state_income-)*.12,
                                              'tier 7': +(adjusted_state_income-)*.12},
                                  'seperate': {'tier 1': +(adjusted_state_income-)*.12,
                                               'tier 2': +(adjusted_state_income-)*.12,
                                               'tier 3': +(adjusted_state_income-)*.12,
                                               'tier 4': +(adjusted_state_income-)*.12,
                                               'tier 5': +(adjusted_state_income-)*.12,
                                               'tier 6': +(adjusted_state_income-)*.12,
                                               'tier 7': +(adjusted_state_income-)*.12},
                                 'head of house':{'tier 1': +(adjusted_state_income-)*.12,
                                                  'tier 2': +(adjusted_state_income-)*.12,
                                                  'tier 3': +(adjusted_state_income-)*.12,
                                                  'tier 4': +(adjusted_state_income-)*.12,
                                                  'tier 5': +(adjusted_state_income-)*.12,
                                                  'tier 6': +(adjusted_state_income-)*.12,
                                                  'tier 7': +(adjusted_state_income-)*.12}
                                 }
                     'georgia': {'single': , {'tier 1': adjusted_state_income*.1,
                                              'tier 2': +(adjusted_state_income-)*.12,
                                              'tier 3': +(adjusted_state_income-)*.12,
                                              'tier 4': +(adjusted_state_income-)*.12,
                                              'tier 5': +(adjusted_state_income-)*.12,
                                              'tier 6': +(adjusted_state_income-)*.12},
                                 'jointly': {'tier 1': +(adjusted_state_income-)*.12,
                                             'tier 2': +(adjusted_state_income-)*.12,
                                             'tier 3': +(adjusted_state_income-)*.12,
                                             'tier 4': +(adjusted_state_income-)*.12,
                                             'tier 5': +(adjusted_state_income-)*.12,
                                             'tier 6': +(adjusted_state_income-)*.12},
                                  'seperate': {'tier 1': +(adjusted_state_income-)*.12,
                                               'tier 2': +(adjusted_state_income-)*.12,
                                               'tier 3': +(adjusted_state_income-)*.12,
                                               'tier 4': +(adjusted_state_income-)*.12,
                                               'tier 5': +(adjusted_state_income-)*.12,
                                               'tier 6': +(adjusted_state_income-)*.12},
                                   'head of house':{'tier 1': +(adjusted_state_income-)*.12,
                                                    'tier 2': +(adjusted_state_income-)*.12,
                                                    'tier 3': +(adjusted_state_income-)*.12,
                                                    'tier 4': +(adjusted_state_income-)*.12,
                                                    'tier 5': +(adjusted_state_income-)*.12,
                                                    'tier 6': +(adjusted_state_income-)*.12}
                               }, 
                     'hawaii': {'single': , {'tier 1': adjusted_state_income*.1,
                                             'tier 2': +(adjusted_state_income-)*.12,
                                             'tier 3': +(adjusted_state_income-)*.12,
                                             'tier 4': +(adjusted_state_income-)*.12,
                                             'tier 5': +(adjusted_state_income-)*.12,
                                             'tier 6': +(adjusted_state_income-)*.12,
                                             'tier 7': +(adjusted_state_income-)*.12,
                                             'tier 8': +(adjusted_state_income-)*.12,
                                             'tier 9': +(adjusted_state_income-)*.12,
                                             'tier 10': +(adjusted_state_income-)*.12,
                                             'tier 11': +(adjusted_state_income-)*.12,
                                             'tier 12': +(adjusted_state_income-)*.12},
                                'jointly': {'tier 1': +(adjusted_state_income-)*.12,
                                            'tier 2': +(adjusted_state_income-)*.12,
                                            'tier 3': +(adjusted_state_income-)*.12,
                                            'tier 4': +(adjusted_state_income-)*.12,
                                            'tier 5': +(adjusted_state_income-)*.12,
                                            'tier 6': +(adjusted_state_income-)*.12,
                                            'tier 7': +(adjusted_state_income-)*.12,
                                            'tier 8': +(adjusted_state_income-)*.12,
                                            'tier 9': +(adjusted_state_income-)*.12,
                                            'tier 10': +(adjusted_state_income-)*.12,
                                            'tier 11': +(adjusted_state_income-)*.12,
                                            'tier 12': +(adjusted_state_income-)*.12},
                                 'seperate': {'tier 1': +(adjusted_state_income-)*.12,
                                              'tier 2': +(adjusted_state_income-)*.12,
                                              'tier 3': +(adjusted_state_income-)*.12,
                                              'tier 4': +(adjusted_state_income-)*.12,
                                              'tier 5': +(adjusted_state_income-)*.12,
                                              'tier 6': +(adjusted_state_income-)*.12,
                                              'tier 7': +(adjusted_state_income-)*.12,
                                              'tier 8': +(adjusted_state_income-)*.12,
                                              'tier 9': +(adjusted_state_income-)*.12,
                                              'tier 10': +(adjusted_state_income-)*.12,
                                              'tier 11': +(adjusted_state_income-)*.12,
                                              'tier 12': +(adjusted_state_income-)*.12},
                                 'head of house':{'tier 1': +(adjusted_state_income-)*.12,
                                                  'tier 2': +(adjusted_state_income-)*.12,
                                                  'tier 3': +(adjusted_state_income-)*.12,
                                                  'tier 4': +(adjusted_state_incomem-)*.12,
                                                  'tier 5': +(adjusted_state_income-)*.12,
                                                  'tier 6': +(adjusted_state_income-)*.12,
                                                  'tier 7': +(adjusted_state_income-)*.12,
                                                  'tier 8': +(adjusted_state_income-)*.12,
                                                  'tier 9': +(adjusted_state_income-)*.12,
                                                  'tier 10': +(adjusted_state_income-)*.12,
                                                  'tier 11': +(adjusted_state_income-)*.12,
                                                  'tier 12': +(adjusted_state_income-)*.12}
                                  }, 
                     'idaho': {'single': , {'tier 1': adjusted_state_income*.1,
                                            'tier 2': +(adjusted_state_income-)*.12,
                                            'tier 3': +(adjusted_state_income-)*.12,
                                            'tier 4': +(adjusted_state_income-)*.12,
                                            'tier 5': +(adjusted_state_income-)*.12,
                                            'tier 6': +(adjusted_state_income-)*.12,
                                            'tier 7': +(adjusted_state_income-)*.12},
                                'jointly': {'tier 1': +(adjusted_state_income-)*.12,
                                            'tier 2': +(adjusted_state_income-)*.12,
                                            'tier 3': +(adjusted_state_income-)*.12,
                                            'tier 4': +(adjusted_state_income-)*.12,
                                            'tier 5': +(adjusted_state_income-)*.12,
                                            'tier 6': +(adjusted_state_income-)*.12,
                                            'tier 7': +(adjusted_state_income-)*.12},
                                 'seperate': {'tier 1': +(adjusted_state_income-)*.12,
                                              'tier 2': +(adjusted_state_income-)*.12,
                                              'tier 3': +(adjusted_state_income-)*.12,
                                              'tier 4': +(adjusted_state_income-)*.12,
                                              'tier 5': +(adjusted_state_income-)*.12,
                                              'tier 6': +(adjusted_state_income-)*.12,
                                              'tier 7': +(adjusted_state_income-)*.12},
                                 'head of house':{'tier 1': +(adjusted_state_income-)*.12,
                                                  'tier 2': +(adjusted_state_income-)*.12,
                                                  'tier 3': +(adjusted_state_income-)*.12,
                                                  'tier 4': +(adjusted_state_income-)*.12,
                                                  'tier 5': +(adjusted_state_income-)*.12,
                                                  'tier 6': +(adjusted_state_income-)*.12,
                                                  'tier 7': +(adjusted_state_income-)*.12}
                              }, 
                     'illinois': sum*.0495,
                     'indiana': sum*.0323,
                     'iowa': {'single': , {'tier 1': adjusted_state_income*.1,
                                           'tier 2': +(adjusted_state_income-)*.12,
                                           'tier 3': +(adjusted_state_income-)*.12,
                                           'tier 4': +(adjusted_state_income-)*.12,
                                           'tier 5': +(adjusted_state_income-)*.12,
                                           'tier 6': +(adjusted_state_income-)*.12,
                                           'tier 7': +(adjusted_state_income-)*.12,
                                           'tier 8': +(adjusted_state_income-)*.12,
                                           'tier 9': +(adjusted_state_income-)*.12},
                               'jointly': {'tier 1': +(adjusted_state_income-)*.12,
                                           'tier 2': +(adjusted_state_income-)*.12,
                                           'tier 3': +(adjusted_state_income-)*.12,
                                           'tier 4': +(adjusted_state_income-)*.12,
                                           'tier 5': +(adjusted_state_income-)*.12,
                                           'tier 6': +(adjusted_state_income-)*.12,
                                           'tier 7': +(adjusted_state_income-)*.12,
                                           'tier 8': +(adjusted_state_income-)*.12,
                                           'tier 9': +(adjusted_state_income-)*.12},
                                'seperate': {'tier 1': +(adjusted_state_income-)*.12,
                                             'tier 2': +(adjusted_state_income-)*.12,
                                             'tier 3': +(adjusted_state_income-)*.12,
                                             'tier 4': +(adjusted_state_income-)*.12,
                                             'tier 5': +(adjusted_state_income-)*.12,
                                             'tier 6': +(adjusted_state_income-)*.12,
                                             'tier 7': +(adjusted_state_income-)*.12,
                                             'tier 8': +(adjusted_state_income-)*.12,
                                             'tier 9': +(adjusted_state_income-)*.12},
                               'head of house':{'tier 1': +(adjusted_state_income-)*.12,
                                                'tier 2': +(adjusted_state_income-)*.12,
                                                'tier 3': +(adjusted_state_income-)*.12,
                                                'tier 4': +(adjusted_state_income-)*.12,
                                                'tier 5': +(adjusted_state_income-)*.12,
                                                'tier 6': +(adjusted_state_income-)*.12,
                                                'tier 7': +(adjusted_state_income-)*.12,
                                                'tier 8': +(adjusted_state_income-)*.12,
                                                'tier 9': +(adjusted_state_income-)*.12}
                             }, 
                     'kansas': {'single': , {'tier 1': adjusted_state_income*.1,
                                             'tier 2': +(adjusted_state_income-)*.12,
                                             'tier 3': +(adjusted_state_income-)*.12},
                                'jointly': {'tier 1': +(adjusted_state_income-)*.12,
                                            'tier 2': +(adjusted_state_income-)*.12,
                                            'tier 3': +(adjusted_state_income-)*.12},
                                'seperate': {'tier 1': +(adjusted_state_income-)*.12,
                                             'tier 2': +(adjusted_state_income-)*.12,
                                             'tier 3': +(adjusted_state_income-)*.12},
                                'head of house':{'tier 1': +(adjusted_state_income-)*.12,
                                                 'tier 2': +(adjusted_state_income-)*.12,
                                                 'tier 3': +(adjusted_state_income-)*.12}
                             }, 
                     'kentucky': .05, 
                     'louisiana': {'single': , {'tier 1': adjusted_state_income*.1,
                                                'tier 2': +(adjusted_state_income-)*.12,
                                                'tier 3': +(adjusted_state_income-)*.12},
                                   'jointly': {'tier 1': +(adjusted_state_income-)*.12,
                                               'tier 2': +(adjusted_state_income-)*.12,
                                               'tier 3': +(adjusted_state_income-)*.12},
                                   'seperate': {'tier 1': +(adjusted_state_income-)*.12,
                                                'tier 2': +(adjusted_state_income-)*.12,
                                                'tier 3': +(adjusted_state_income-)*.12},
                                   'head of house':{'tier 1': +(adjusted_state_income-)*.12,
                                                    'tier 2': +(adjusted_state_income-)*.12,
                                                    'tier 3': +(adjusted_state_income-)*.12}
                                   }, 
                     'maine': {'single': , {'tier 1': adjusted_state_income*.1,
                                            'tier 2': +(adjusted_state_income-)*.12,
                                            'tier 3': +(adjusted_state_income-)*.12},
                               'jointly': {'tier 1': +(adjusted_state_income-)*.12,
                                           'tier 2': +(adjusted_state_income-)*.12,
                                           'tier 3': +(adjusted_state_income-)*.12},
                               'seperate': {'tier 1': +(adjusted_state_income-)*.12,
                                            'tier 2': +(adjusted_state_income-)*.12,
                                            'tier 3': +(adjusted_state_income-)*.12},
                               'head of house':{'tier 1': +(adjusted_state_income-)*.12,
                                                'tier 2': +(adjusted_state_income-)*.12,
                                                'tier 3': +(adjusted_state_income-)*.12}
                              }, 
                     'maryland': {'single': , {'tier 1': adjusted_state_income*.1,
                                               'tier 2': +(adjusted_state_income-)*.12,
                                               'tier 3': +(adjusted_state_income-)*.12,
                                               'tier 4': +(adjusted_state_income-)*.12,
                                               'tier 5': +(adjusted_state_income-)*.12,
                                               'tier 6': +(adjusted_state_income-)*.12,
                                               'tier 7': +(adjusted_state_income-)*.12,
                                               'tier 8': +(adjusted_state_income-)*.12},
                                  'jointly': {'tier 1': +(adjusted_state_income-)*.12,
                                              'tier 2': +(adjusted_state_income-)*.12,
                                              'tier 3': +(adjusted_state_income-)*.12,
                                              'tier 4': +(adjusted_state_income-)*.12,
                                              'tier 5': +(adjusted_state_income-)*.12,
                                              'tier 6': +(adjusted_state_income-)*.12,
                                              'tier 7': +(adjusted_state_income-)*.12,
                                              'tier 8': +(adjusted_state_income-)*.12},
                                  'seperate': {'tier 1': +(adjusted_state_income-)*.12,
                                               'tier 2': +(adjusted_state_income-)*.12,
                                               'tier 3': +(adjusted_state_income-)*.12,
                                               'tier 4': +(adjusted_state_income-)*.12,
                                               'tier 5': +(adjusted_state_income-)*.12,
                                               'tier 6': +(adjusted_state_income-)*.12,
                                               'tier 7': +(adjusted_state_income-)*.12,
                                               'tier 8': +(adjusted_state_income-)*.12},
                                  'head of house':{'tier 1': +(adjusted_state_income-)*.12,
                                                   'tier 2': +(adjusted_state_income-)*.12,
                                                   'tier 3': +(adjusted_state_income-)*.12,
                                                   'tier 4': +(adjusted_state_income-)*.12,
                                                   'tier 5': +(adjusted_state_income-)*.12,
                                                   'tier 6': +(adjusted_state_income-)*.12,
                                                   'tier 7': +(adjusted_state_income-)*.12,
                                                   'tier 8': +(adjusted_state_income-)*.12}
                                      }, 
                     'massachusetts': adjusted_state_income*.05, 
                     'michigan': adjusted_state_income*.0425, 
                     'minnesota': {'single': , {'tier 1': sadjusted_state_income*.1,
                                                'tier 2': +(adjusted_state_income-)*.12,
                                                'tier 3': +(adjusted_state_income-)*.12,
                                                'tier 4': +(adjusted_state_income-)*.12}
                                   'jointly': {'tier 1': +(adjusted_state_income-)*.12,
                                               'tier 2': +(adjusted_state_income-)*.12,
                                               'tier 3': +(adjusted_state_income-)*.12,
                                               'tier 4': +(adjusted_state_income-)*.12},
                                    'seperate': {'tier 1': +(adjusted_state_income-)*.12,
                                                 'tier 2': +(adjusted_state_income-)*.12,
                                                 'tier 3': +(adjusted_state_income-)*.12,
                                                 'tier 4': +(adjusted_state_income-)*.12},
                                    'head of house':{'tier 1': +(adjusted_state_income-)*.12,
                                                     'tier 2': +(adjusted_state_income-)*.12,
                                                     'tier 3': +(adjusted_state_income-)*.12,
                                                     'tier 4': +(adjusted_state_income-)*.12}
                                 }, 
                     'mississippi': {'single': , {'tier 1': adjusted_state_income*.1,
                                                  'tier 2': +(adjusted_state_income-)*.12,
                                                  'tier 3': +(adjusted_state_income-)*.12},
                                     'jointly': {'tier 1': +(adjusted_state_income-)*.12,
                                                 'tier 2': +(adjusted_state_income-)*.12,
                                                 'tier 3': +(adjusted_state_income-)*.12},
                                     'seperate': {'tier 1': +(adjusted_state_income-)*.12,
                                                  'tier 2': +(adjusted_state_income-)*.12,
                                                  'tier 3': +(adjusted_state_income-)*.12},
                                     'head of house':{'tier 1': +(adjusted_state_income-)*.12,
                                                      'tier 2': +(adjusted_state_income-)*.12,
                                                      'tier 3': +(adjusted_state_income-)*.12}
                                    },
                     'missouri': {'single': , {'tier 1': adjusted_state_income*.1,
                                               'tier 2': +(adjusted_state_income-)*.12,
                                               'tier 3': +(adjusted_state_income-)*.12,
                                               'tier 4': +(sum-)*.12,
                                               'tier 5': +(sum-)*.12,
                                               'tier 6': +(sum-)*.12,
                                               'tier 7': +(sum-)*.12,
                                               'tier 8': +(sum-)*.12,
                                               'tier 9': +(sum-)*.12},
                                  'jointly': {'tier 1': +(sum-)*.12,
                                              'tier 2': +(sum-)*.12,
                                              'tier 3': +(sum-)*.12,
                                              'tier 4': +(sum-)*.12,
                                              'tier 5': +(sum-)*.12,
                                              'tier 6': +(sum-)*.12,
                                              'tier 7': +(sum-)*.12,
                                              'tier 8': +(sum-)*.12,
                                              'tier 9': +(sum-)*.12},
                                  'seperate': {'tier 1': +(sum-)*.12,
                                               'tier 2': +(sum-)*.12,
                                               'tier 3': +(sum-)*.12,
                                               'tier 4': +(sum-)*.12,
                                               'tier 5': +(sum-)*.12,
                                               'tier 6': +(sum-)*.12,
                                               'tier 7': +(sum-)*.12,
                                               'tier 8': +(sum-)*.12,
                                               'tier 9': +(sum-)*.12},
                                  'head of house':{'tier 1': +(sum-)*.12,
                                                   'tier 2': +(sum-)*.12,
                                                   'tier 3': +(sum-)*.12,
                                                   'tier 4': +(sum-)*.12,
                                                   'tier 5': +(sum-)*.12,
                                                   'tier 6': +(sum-)*.12,
                                                   'tier 7': +(sum-)*.12,
                                                   'tier 8': +(sum-)*.12,
                                                   'tier 9': +(sum-)*.12}
                                  }, 
                     'montana': {'single': , {'tier 1': sum*.1,
                                              'tier 2': +(sum-)*.12,
                                              'tier 3': +(sum-)*.12,
                                              'tier 4': +(sum-)*.12,
                                              'tier 5': +(sum-)*.12,
                                              'tier 6': +(sum-)*.12,
                                              'tier 7': +(sum-)*.12},
                                  'jointly': {'tier 1': +(sum-)*.12,
                                              'tier 2': +(sum-)*.12,
                                              'tier 3': +(sum-)*.12,
                                              'tier 4': +(sum-)*.12,
                                              'tier 5': +(sum-)*.12,
                                              'tier 6': +(sum-)*.12,
                                              'tier 7': +(sum-)*.12},
                                 'seperate': {'tier 1': +(sum-)*.12,
                                              'tier 2': +(sum-)*.12,
                                              'tier 3': +(sum-)*.12,
                                              'tier 4': +(sum-)*.12,
                                              'tier 5': +(sum-)*.12,
                                              'tier 6': +(sum-)*.12,
                                              'tier 7': +(sum-)*.12},
                                 'head of house':{'tier 1': +(sum-)*.12,
                                                  'tier 2': +(sum-)*.12,
                                                  'tier 3': +(sum-)*.12,
                                                  'tier 4': +(sum-)*.12,
                                                  'tier 5': +(sum-)*.12,
                                                  'tier 6': +(sum-)*.12,
                                                  'tier 7': +(sum-)*.12}
                              }, 
                     'nebraska': {'single': , {'tier 1': sum*.1,
                                               'tier 2': +(sum-)*.12,
                                               'tier 3': +(sum-)*.12,
                                               'tier 4': +(sum-)*.12}
                                   'jointly': {'tier 1': +(sum-)*.12,
                                               'tier 2': +(sum-)*.12,
                                               'tier 3': +(sum-)*.12,
                                               'tier 4': +(sum-)*.12},
                                  'seperate': {'tier 1': +(sum-)*.12,
                                               'tier 2': +(sum-)*.12,
                                               'tier 3': +(sum-)*.12,
                                              'tier 4': +(sum-)*.12},
                                 'head of house':{'tier 1': +(sum-)*.12,
                                                  'tier 2': +(sum-)*.12,
                                                  'tier 3': +(sum-)*.12,
                                                  'tier 4': +(sum-)*.12}
                             }
                     'new hampshire': sum*.05, 
                     'new jersey': {'single': , {'tier 1': sum*.1,
                                                 'tier 2': +(sum-)*.12,
                                                 'tier 3': +(sum-)*.12,
                                                 'tier 4': +(sum-)*.12,
                                                 'tier 5': +(sum-)*.12,
                                                 'tier 6': +(sum-)*.12,
                                                 'tier 7': +(sum-)*.12},
                                     'jointly': {'tier 1': +(sum-)*.12,
                                                 'tier 2': +(sum-)*.12,
                                                 'tier 3': +(sum-)*.12,
                                                 'tier 4': +(sum-)*.12,
                                                 'tier 5': +(sum-)*.12,
                                                 'tier 6': +(sum-)*.12,
                                                 'tier 7': +(sum-)*.12},
                                     'seperate': {'tier 1': +(sum-)*.12,
                                                  'tier 2': +(sum-)*.12,
                                                  'tier 3': +(sum-)*.12,
                                                  'tier 4': +(sum-)*.12,
                                                  'tier 5': +(sum-)*.12,
                                                  'tier 6': +(sum-)*.12,
                                                  'tier 7': +(sum-)*.12},
                                     'head of house':{'tier 1': +(sum-)*.12,
                                                      'tier 2': +(sum-)*.12,
                                                      'tier 3': +(sum-)*.12,
                                                      'tier 4': +(sum-)*.12,
                                                      'tier 5': +(sum-)*.12,
                                                      'tier 6': +(sum-)*.12,
                                                      'tier 7': +(sum-)*.12}
                                  }, 
                     'new mexico': {'single': , {'tier 1': sum*.1,
                                                 'tier 2': +(sum-)*.12,
                                                 'tier 3': +(sum-)*.12,
                                                 'tier 4': +(sum-)*.12},
                                    'jointly': {'tier 1': +(sum-)*.12,
                                                'tier 2': +(sum-)*.12,
                                                'tier 3': +(sum-)*.12,
                                                'tier 4': +(sum-)*.12},
                                    'seperate': {'tier 1': +(sum-)*.12,
                                                 'tier 2': +(sum-)*.12,
                                                 'tier 3': +(sum-)*.12,
                                                 'tier 4': +(sum-)*.12},
                                   'head of house':{'tier 1': +(sum-)*.12,
                                                    'tier 2': +(sum-)*.12,
                                                    'tier 3': +(sum-)*.12,
                                                    'tier 4': +(sum-)*.12}
                                      }, 
                     'new york': {'single': , {'tier 1': sum*.1,
                                               'tier 2': +(sum-)*.12,
                                               'tier 3': +(sum-)*.12,
                                               'tier 4': +(sum-)*.12,
                                               'tier 5': +(sum-)*.12,
                                               'tier 6': +(sum-)*.12,
                                               'tier 7': +(sum-)*.12,
                                               'tier 8': +(sum-)*.12},
                                  'jointly': {'tier 1': +(sum-)*.12,
                                              'tier 2': +(sum-)*.12,
                                              'tier 3': +(sum-)*.12,
                                              'tier 4': +(sum-)*.12,
                                              'tier 5': +(sum-)*.12,
                                              'tier 6': +(sum-)*.12,
                                              'tier 7': +(sum-)*.12,
                                              'tier 8': +(sum-)*.12},
                                  'seperate': {'tier 1': +(sum-)*.12,
                                               'tier 2': +(sum-)*.12,
                                               'tier 3': +(sum-)*.12,
                                               'tier 4': +(sum-)*.12,
                                               'tier 5': +(sum-)*.12,
                                               'tier 6': +(sum-)*.12,
                                               'tier 7': +(sum-)*.12,
                                               'tier 8': +(sum-)*.12},
                                  'head of house':{'tier 1': +(sum-)*.12,
                                                   'tier 2': +(sum-)*.12,
                                                   'tier 3': +(sum-)*.12,
                                                   'tier 4': +(sum-)*.12,
                                                   'tier 5': +(sum-)*.12,
                                                   'tier 6': +(sum-)*.12,
                                                   'tier 7': +(sum-)*.12,
                                                   'tier 8': +(sum-)*.12}
                                     },
                     'north carolina': sum*.0525,
                     'north dakota': {'single': , {'tier 1': sum*.1,
                                                   'tier 2': +(sum-)*.12,
                                                   'tier 3': +(sum-)*.12,
                                                   'tier 4': +(sum-)*.12,
                                                   'tier 5': +(sum-)*.12},
                                       'jointly': {'tier 1': +(sum-)*.12,
                                                   'tier 2': +(sum-)*.12,
                                                   'tier 3': +(sum-)*.12,
                                                   'tier 4': +(sum-)*.12,
                                                   'tier 5': +(sum-)*.12},
                                        'seperate': {'tier 1': +(sum-)*.12,
                                                     'tier 2': +(sum-)*.12,
                                                     'tier 3': +(sum-)*.12,
                                                     'tier 4': +(sum-)*.12,
                                                     'tier 5': +(sum-)*.12},
                                        'head of house':{'tier 1': +(sum-)*.12,
                                                         'tier 2': +(sum-)*.12,
                                                         'tier 3': +(sum-)*.12,
                                                         'tier 4': +(sum-)*.12,
                                                         'tier 5': +(sum-)*.12}
                                      }, 
                     'ohio': {'single': , {'tier 1': sum*.1,
                                           'tier 2': +(sum-)*.12,
                                           'tier 3': +(sum-)*.12,
                                           'tier 4': +(sum-)*.12,
                                           'tier 5': +(sum-)*.12,
                                           'tier 6': +(sum-)*.12},
                              'jointly': {'tier 1': +(sum-)*.12,
                                          'tier 2': +(sum-)*.12,
                                          'tier 3': +(sum-)*.12,
                                          'tier 4': +(sum-)*.12,
                                          'tier 5': +(sum-)*.12,
                                          'tier 6': +(sum-)*.12},
                              'seperate': {'tier 1': +(sum-)*.12,
                                           'tier 2': +(sum-)*.12,
                                           'tier 3': +(sum-)*.12,
                                           'tier 4': +(sum-)*.12,
                                           'tier 5': +(sum-)*.12,
                                           'tier 6': +(sum-)*.12},
                             'head of house':{'tier 1': +(sum-)*.12,
                                              'tier 2': +(sum-)*.12,
                                              'tier 3': +(sum-)*.12,
                                              'tier 4': +(sum-)*.12,
                                              'tier 5': +(sum-)*.12,
                                              'tier 6': +(sum-)*.12}
                        }, 
                     'oklahoma': {'single': , {'tier 1': sum*.1,
                                               'tier 2': +(sum-)*.12,
                                               'tier 3': +(sum-)*.12,
                                               'tier 4': +(sum-)*.12,
                                               'tier 5': +(sum-)*.12,
                                               'tier 6': +(sum-)*.12},
                                 'jointly': {'tier 1': +(sum-)*.12,
                                             'tier 2': +(sum-)*.12,
                                             'tier 3': +(sum-)*.12,
                                             'tier 4': +(sum-)*.12,
                                             'tier 5': +(sum-)*.12,
                                             'tier 6': +(sum-)*.12},
                                'seperate': {'tier 1': +(sum-)*.12,
                                             'tier 2': +(sum-)*.12,
                                             'tier 3': +(sum-)*.12,
                                             'tier 4': +(sum-)*.12,
                                             'tier 5': +(sum-)*.12,
                                             'tier 6': +(sum-)*.12},
                                'head of house':{'tier 1': +(sum-)*.12,
                                                 'tier 2': +(sum-)*.12,
                                                 'tier 3': +(sum-)*.12,
                                                 'tier 4': +(sum-)*.12,
                                                 'tier 5': +(sum-)*.12,
                                                 'tier 6': +(sum-)*.12}
                                 },
                     'oregon': {'single': , {'tier 1': sum*.1,
                                             'tier 2': +(sum-)*.12,
                                             'tier 3': +(sum-)*.12,
                                             'tier 4': +(sum-)*.12}, 
                                'jointly': {'tier 1': +(sum-)*.12,
                                            'tier 2': +(sum-)*.12,
                                            'tier 3': +(sum-)*.12,
                                            'tier 4': +(sum-)*.12},
                                'seperate': {'tier 1': +(sum-)*.12,
                                             'tier 2': +(sum-)*.12,
                                             'tier 3': +(sum-)*.12,
                                             'tier 4': +(sum-)*.12},
                                'head of house':{'tier 1': +(sum-)*.12,
                                                 'tier 2': +(sum-)*.12,
                                                 'tier 3': +(sum-)*.12,
                                                 'tier 4': +(sum-)*.12}
                                }, 
                     'pennsylvania': sum*.0307, 
                     'rhode island': {'single': , {'tier 1': sum*.1,
                                                   'tier 2': +(sum-)*.12,
                                                   'tier 3': +(sum-)*.12},
                                      'jointly': {'tier 1': +(sum-)*.12,
                                                  'tier 2': +(sum-)*.12,
                                                  'tier 3': +(sum-)*.12},
                                      'seperate': {'tier 1': +(sum-)*.12,
                                                   'tier 2': +(sum-)*.12,
                                                   'tier 3': +(sum-)*.12},
                                      'head of house':{'tier 1': +(sum-)*.12,
                                                       'tier 2': +(sum-)*.12,
                                                       'tier 3': +(sum-)*.12}
                                        }, 
                     'south carolina': {'single': , {'tier 1': sum*.1,
                                                    'tier 2': +(sum-)*.12,
                                                    'tier 3': +(sum-)*.12,
                                                    'tier 4': +(sum-)*.12,
                                                    'tier 5': +(sum-)*.12,
                                                    'tier 6': +(sum-)*.12},
                                       'jointly': {'tier 1': +(sum-)*.12,
                                                   'tier 2': +(sum-)*.12,
                                                   'tier 3': +(sum-)*.12,
                                                   'tier 4': +(sum-)*.12,
                                                   'tier 5': +(sum-)*.12,
                                                   'tier 6': +(sum-)*.12},
                                      'seperate': {'tier 1': +(sum-)*.12,
                                                   'tier 2': +(sum-)*.12,
                                                   'tier 3': +(sum-)*.12,
                                                   'tier 4': +(sum-)*.12,
                                                   'tier 5': +(sum-)*.12,
                                                   'tier 6': +(sum-)*.12},
                                      'head of house':{'tier 1': +(sum-)*.12,
                                                       'tier 2': +(sum-)*.12,
                                                       'tier 3': +(sum-)*.12,
                                                       'tier 4': +(sum-)*.12,
                                                       'tier 5': +(sum-)*.12,
                                                       'tier 6': +(sum-)*.12}
                      } 
                     'tennessee': {'single': , {'tier 1': sum*.1,
                                                'tier 2': +(sum-)*.12,
                                                'tier 3': +(sum-)*.12,
                                                'tier 4': +(sum-)*.12,
                                                'tier 5': +(sum-)*.12,
                                                'tier 6': +(sum-)*.12,
                                                'tier 7': +(sum-)*.12},
                                   'jointly': {'tier 1': +(sum-)*.12,
                                               'tier 2': +(sum-)*.12,
                                               'tier 3': +(sum-)*.12,
                                               'tier 4': +(sum-)*.12,
                                               'tier 5': +(sum-)*.12,
                                               'tier 6': +(sum-)*.12,
                                               'tier 7': +(sum-)*.12},
                                   'seperate': {'tier 1': +(sum-)*.12,
                                                'tier 2': +(sum-)*.12,
                                                'tier 3': +(sum-)*.12,
                                                'tier 4': +(sum-)*.12,
                                                'tier 5': +(sum-)*.12,
                                                'tier 6': +(sum-)*.12,
                                                'tier 7': +(sum-)*.12},
                                  'head of house':{'tier 1': +(sum-)*.12,
                                                   'tier 2': +(sum-)*.12,
                                                   'tier 3': +(sum-)*.12,
                                                   'tier 4': +(sum-)*.12,
                                                   'tier 5': +(sum-)*.12,
                                                   'tier 6': +(sum-)*.12,
                                                   'tier 17': +(sum-)*.12}
                                   }
                     'utah': sum*.0495, 
                     'vermont': {'single': , {'tier 1': sum*.1,
                                              'tier 2': +(sum-)*.12,
                                              'tier 3': +(sum-)*.12,
                                              'tier 4': +(sum-)*.12},
                                  'jointly': {'tier 1': +(sum-)*.12,
                                              'tier 2': +(sum-)*.12,
                                              'tier 3': +(sum-)*.12,
                                              'tier 4': +(sum-)*.12},
                                 'seperate': {'tier 1': +(sum-)*.12,
                                              'tier 2': +(sum-)*.12,
                                              'tier 3': +(sum-)*.12,
                                              'tier 4': +(sum-)*.12},
                                 'head of house':{'tier 1': +(sum-)*.12,
                                                  'tier 2': +(sum-)*.12,
                                                  'tier 3': +(sum-)*.12,
                                                  'tier 4': +(sum-)*.12}
                                }, 
                     'virginia': {'single': , {'tier 1': sum*.1,
                                               'tier 2': +(sum-)*.12,
                                               'tier 3': +(sum-)*.12,
                                               'tier 4': +(sum-)*.12},
                                  'jointly': {'tier 1': +(sum-)*.12,
                                              'tier 2': +(sum-)*.12,
                                              'tier 3': +(sum-)*.12,
                                              'tier 4': +(sum-)*.12},
                                   'seperate': {'tier 1': +(sum-)*.12,
                                                'tier 2': +(sum-)*.12,
                                                'tier 3': +(sum-)*.12,
                                                'tier 4': +(sum-)*.12},
                                   'head of house':{'tier 1': +(sum-)*.12,
                                                    'tier 2': +(sum-)*.12,
                                                    'tier 3': +(sum-)*.12,
                                                    'tier 4': +(sum-)*.12}
                                }
                     'west virginia': {'single': , {'tier 1': sum*.1,
                                                    'tier 2': +(sum-)*.12,
                                                    'tier 3': +(sum-)*.12,
                                                    'tier 4': +(sum-)*.12,
                                                    'tier 5': +(sum-)*.12},
                                      'jointly': {'tier 1': +(sum-)*.12,
                                                  'tier 2': +(sum-)*.12,
                                                  'tier 3': +(sum-)*.12,
                                                  'tier 4': +(sum-)*.12,
                                                  'tier 5': +(sum-)*.12},
                                      'seperate': {'tier 1': +(sum-)*.12,
                                                   'tier 2': +(sum-)*.12,
                                                   'tier 3': +(sum-)*.12,
                                                   'tier 4': +(sum-)*.12,
                                                   'tier 5': +(sum-)*.12},
                                     'head of house':{'tier 1': +(sum-)*.12,
                                                      'tier 2': +(sum-)*.12,
                                                      'tier 3': +(sum-)*.12,
                                                      'tier 4': +(sum-)*.12,
                                                      'tier 5': +(sum-)*.12}
                                     }, 
                     'wisconsin': {'single': , {'tier 1': sum*.1,
                                                'tier 2': +(sum-)*.12,
                                                'tier 3': +(sum-)*.12,
                                                'tier 4': +(sum-)*.12},
                                    'jointly': {'tier 1': +(sum-)*.12,
                                                'tier 2': +(sum-)*.12,
                                                'tier 3': +(sum-)*.12,
                                                'tier 4': +(sum-)*.12},
                                   'seperate': {'tier 1': +(sum-)*.12,
                                                'tier 2': +(sum-)*.12,
                                                'tier 3': +(sum-)*.12,
                                                'tier 4': +(sum-)*.12},
                                    'head of house':{'tier 1': +(sum-)*.12,
                                                     'tier 2': +(sum-)*.12,
                                                     'tier 3': +(sum-)*.12,
                                                     'tier 4': +(sum-)*.12}   }     }

list_of_states_with_taxes = ['alabama' , 'arizona' ,'arkansas' ,'california','colorado' , 'connecticut' ,'delaware' , 'georgia' , 'hawaii' , 'idaho' , 'illinois' ,
                  'indiana' , 'iowa' ,'kansas' , 'kentucky' ,'louisiana' , 'maine' , 'maryland', 'massachusetts' , 'michigan' ,'minnesota' , 'mississippi' ,'missouri' , 'montana' , 
                  'nebraska' , 'new hampshire' ,'new jersey' ,'new mexico' ,'new york' ,'north carolina', 'north dakota' ,'ohio' , 'oklahoma' ,'oregon' , 'pennsylvania' , 
                  'rhode island' , 'south carolina' ,'tennessee' , 'utah', 'vermont' , 'virginia' , 'west virginia' ,'wisconsin']
list_of_states_with_no_taxes = ['alaska', 'florida', 'south dakota','nevada', 'texas','washington', 'wyoming']

list_of_filling_status = ['single', 'jointly', 'seperate', 'head of household']                     

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
    print('''Please note that these estimated taxes are not considering itemizing deductable. This amount assumes a standard deductable. 
    As a result, there is a possibility that you will owe less taxes. You can consider this your tax ceiling.\n'''
    check_state = True
    while check_state == True: 
          state = input('We need to know the state that you live in. Please enter the whole name. Example: Mississippi.')
          if state.lower() in list_of_states_with_taxes or list_of_states_with_no_taxes: 
              check_state = False 
              break 
          elif: 
              print('You have entered something that is not a state. Please ensure that your spelling is correct.\n')
    check_gross_income = True 
    while check_gross_income == True: 
          gross_income_input = input('Now you will have to enter the amount of money you will make in this calendar year: $')
          try: 
              gross_income = int(gross_income_input)
              check_gross_income_input = False
              break 
          except: 
              print('Please enter the amount you will make in numerical form.')
    check_self_employment = True
    while check_self_employment == True: 
          self_employment_input = input('Please enter how much of that income was made by you being self employed. If none, please enter 0. $')
          try: 
              self_employment_income = int(self_employment_input)
              check_self_eployment = False
              break
          except: 
              print('please enter any amount that you made as self employed in numerical form.\n')
          
    self_employment_tax = self_employment_income*.153
          
    check_filing_status = True
    while check_filing_status == True: 
          filing_status = input('''Please enter the status you will be filing. Single, Jointly, Seperate, or Head of household''')
          if filing_status in list_of_filing_status:
              check_filing_status = False
              break 
          else: 
              print('Please enter one of the four options.')
          
    adjusted_federal_income = gross_income-self_employment_income-federal_deductibles[filing_status]
          
    if filing_status == 'single':    
        if adjusted_federal_income =< 10275: 
              federal_tax_amount = federal_tax_bracket[filing_status]['tier 1']
          
        elif 10276 <= adjusted_federal_income <41776: 
              federal_tax_amount = federal_tax_bracket[filing_status]['tier 2']          
          
        elif 41776 <= adjusted_federal_income <89076:
              federal_tax_amount = federal_tax_bracket[filing_status]['tier 3']
          
        elif 89076 <= adjusted_federal_income <170051: 
              federal_tax_amount = federal_tax_bracket[filing_status]['tier 4']          
          
        elif 170051 <= adjusted_federal_income <215951: 
              federal_tax_amount = federal_tax_bracket[filing_status]['tier 5']          
          
        elif 215951 <= adjusted_federal_income <539901: 
              federal_tax_amount = federal_tax_bracket[filing_status]['tier 6']          
          
        elif 539901 <= adjusted_federal_income: 
              federal_tax_amount = federal_tax_bracket[filing_status]['tier 7'] 
          
    elif filing_status == 'jointly':    
        if adjusted_federal_income =< 20550: 
              federal_tax_amount = federal_tax_bracket[filing_status]['tier 1']
          
        elif 20551<= adjusted_federal_income <83551: 
              federal_tax_amount = federal_tax_bracket[filing_status]['tier 2']  
          
        elif 83551<= adjusted_federal_income <178151: 
              federal_tax_amount = federal_tax_bracket[filing_status]['tier 3']
          
        elif 178151<= adjusted_federal_income <340101: 
              federal_tax_amount = federal_tax_bracket[filing_status]['tier 4']    
          
        elif 340101 <= adjusted_federal_income <431901 : 
              federal_tax_amount = federal_tax_bracket[filing_status]['tier 5']  
          
        elif 431901<= adjusted_federal_income <647851: 
              federal_tax_amount = federal_tax_bracket[filing_status]['tier 6']  
          
        elif 647851<= adjusted_federal_income: 
              federal_tax_amount = federal_tax_bracket[filing_status]['tier 7'] 
          
    elif filing_status == 'seperate':    
        if adjusted_federal_income =<10275: 
              federal_tax_amount = federal_tax_bracket[filing_status]['tier 1']
          
        elif 10276<= adjusted_federal_income <41776: 
              federal_tax_amount = federal_tax_bracket[filing_status]['tier 2']  
          
        elif 41776<= adjusted_federal_income <89076: 
              federal_tax_amount = federal_tax_bracket[filing_status]['tier 3']
          
        elif 89076<= adjusted_federal_income <170051: 
              federal_tax_amount = federal_tax_bracket[filing_status]['tier 4']      
          
        elif 170051<= adjusted_federal_income <215951: 
              federal_tax_amount = federal_tax_bracket[filing_status]['tier 5']   
          
        elif 215951<= adjusted_federal_income <323926: 
              federal_tax_amount = federal_tax_bracket[filing_status]['tier 6']  
          
        elif 323,926<= adjusted_federal_income  : 
              federal_tax_amount = federal_tax_bracket[filing_status]['tier 7']   
          
    elif filing_status == 'head of household':    
        if adjusted_federal_income =< 14650: 
              federal_tax_amount = federal_tax_bracket[filing_status]['tier 1']
          
        elif 14651<= adjusted_federal_income <55901: 
              federal_tax_amount = federal_tax_bracket[filing_status]['tier 2']  
          
        elif 55901<= adjusted_federal_income <89051: 
              federal_tax_amount = federal_tax_bracket[filing_status]['tier 3']
          
        elif 89051<= adjusted_federal_income <170051: 
              federal_tax_amount = federal_tax_bracket[filing_status]['tier 4'] 
          
        elif 170051< adjusted_federal_income <215951: 
              federal_tax_amount = federal_tax_bracket[filing_status]['tier 5'] 
          
        elif 215921< adjusted_federal_income <539901: 
              federal_tax_amount = federal_tax_bracket[filing_status]['tier 6']  
          
        elif 539901<= adjusted_federal_income  : 
              federal_tax_amount = federal_tax_bracket[filing_status]['tier 7']           
    
     if state.lower() in list_of_states_with_no_taxes: 
          state_tax_amount = 0
     elif state.lower() == 'alabama':
          if filing_status == 'single' or 'seperate' or 'head of household':
              adjusted_state_income = gross_income- 2500
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 7500
          
     elif state.lower() == 'arizona':
     elif state.lower() = 'arkansas':
     elif state.lower() = 'california':
     elif state.lower() = 'colorado':
     elif state.lower() = 'connecticut':
     elif state.lower() = 'delware':
     elif state.lower() = 'georgia':
     elif state.lower() = 'hawaii':
     elif state.lower() = 'idaho':
     elif state.lower() = 'illinois':
          
     elif state.lower() = 'indiana':
     elif state.lower() = 'iowa':
     elif state.lower() = 'kansas':
     elif state.lower() = 'kentucky':
     elif state.lower() = 'louisiana':
     elif state.lower() = 'maine':
     elif state.lower() = 'maryland':
     elif state.lower() = 'massachuetts':
     elif state.lower() = 'michigan':                             
     elif state.lower() = 'minnesota':
          
     elif state.lower() = 'mississippi':
     elif state.lower() = 'missouri':
     elif state.lower() = 'montana':
     elif state.lower() = 'nebraska':
     elif state.lower() = 'new hampshire':
     elif state.lower() = 'new jersey':
     elif state.lower() = 'new mexico':
     elif state.lower() = 'new york':
     elif state.lower() = 'north carolina': 
     elif state.lower() = 'north dakota':
          
     elif state.lower() = 'ohio':
     elif state.lower() = 'oklahoma':
     elif state.lower() = 'oregon':
     elif state.lower() = 'pennslyvania':
     elif state.lower() = 'rhode island':
     elif state.lower() = 'south carolina': 
     elif state.lower() = 'tennessee':
     elif state.lower() = 'utah':
     elif state.lower() = 'vermont':         
     elif state.lower() = 'virgina':
     elif state.lower() = 'west virgina':
     elif state.lower() = 'wisconsin':          
          
    if self_employment_income > 0:
          tax_statement = f"Your total amount of taxes due is ${}. This include ${federal_tax_amount} federal tax, ${self_employment_tax} in self employment, and ${state_tax_amount} {state} tax amount."
    elif self_employment_income == 0:      
        tax_statement = f"Your total amount of taxes due is ${}. This include ${federal_tax_amount} federal tax and ${state_tax_amount} {state} tax amount."
    return tax_statement 
  
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
