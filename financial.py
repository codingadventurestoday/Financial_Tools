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
                                  'jointly': {'tier 1': +(adjusted_state_income-)*..02,
                                              'tier 2': +(adjusted_state_income-)*.04,
                                              'tier 3': +(adjusted_state_income-)*.05},
                                  'seperate': {'tier 1': +(adjusted_state_income-)*.02,
                                               'tier 2': +(adjusted_state_income-)*.04,
                                               'tier 3': +(adjusted_state_income-)*.05},
                                  'head of house':{'tier 1': +(adjusted_state_income-)*.02,
                                                   'tier 2': +(adjusted_state_income-)*.04,
                                                   'tier 3': +(adjusted_state_income-)*.05}
                                  }
                     'arizona':{'single': , {'tier 1': adjusted_state_income*.0259,
                                             'tier 2': +(adjusted_state_income-)*.0334,
                                             'tier 3': +(adjusted_state_income-)*.0417,
                                             'tier 4': +(adjusted_state_income-)*.045},
                                'jointly': {'tier 1': +(adjusted_state_income-)*.0259,
                                            'tier 2': +(adjusted_state_income-)*.0334,
                                            'tier 3': +(adjusted_state_income-)*.0417,
                                            'tier 4': +(adjusted_state_income-)*.045},
                                'seperate': {'tier 1': +(adjusted_state_income-)*.0259,
                                             'tier 2': +(adjusted_state_income-)*.0334,
                                             'tier 3': +(adjusted_state_income-)*.0417,
                                             'tier 4': +(adjusted_state_income-)*.045},
                                'head of house':{'tier 1': +(adjusted_state_income-)*.0259,
                                                 'tier 2': +(adjusted_state_income-)*.0334,
                                                 'tier 3': +(adjusted_state_income-)*.0417,
                                                 'tier 4': +(adjusted_state_income-)*.045}
                                 } ,
                     'arkansas': {'single': , {'tier 1': adjusted_state_income*.02,
                                               'tier 2': +(adjusted_state_income-)*.04,
                                               'tier 3': +(adjusted_state_income-)*.05},
                                  'jointly': {'tier 1': +(adjusted_state_income-)*.02,
                                              'tier 2': +(adjusted_state_income-)*.04,
                                              'tier 3': +(adjusted_state_income-)*.05},
                                  'seperate': {'tier 1': +(adjusted_state_income-)*.02,
                                               'tier 2': +(adjusted_state_income-)*.04,
                                               'tier 3': +(adjusted_state_income-)*.05},
                                  'head of house':{'tier 1': +(adjusted_state_income-)*.02,
                                                   'tier 2': +(adjusted_state_income-)*.04,
                                                   'tier 3': +(adjusted_state_income-)*.05}
                                  },
                     'california': {'single': , {'tier 1': adjusted_state_income*.01,
                                                 'tier 2': +(adjusted_state_income-)*.02,
                                                 'tier 3': +(adjusted_state_income-)*.04,
                                                 'tier 4': +(adjusted_state_income-)*.06,
                                                 'tier 5': +(adjusted_state_income-)*.08,
                                                 'tier 6': +(adjusted_state_income-)*.093,
                                                 'tier 7': +(adjusted_state_income-)*.103,
                                                 'tier 8': +(adjusted_state_income-)*.113,
                                                 'tier 9': +(adjusted_state_income-)*.123},
                                    'jointly': {'tier 1': +(adjusted_state_income-)*.01,
                                                'tier 2': +(adjusted_state_income-)*.02,
                                                'tier 3': +(adjusted_state_income-)*.04,
                                                'tier 4': +(adjusted_state_income-)*.06,
                                                'tier 5': +(adjusted_state_income-)*.08,
                                                'tier 6': +(adjusted_state_income-)*.093,
                                                'tier 7': +(adjusted_state_income-)*.103,
                                                'tier 8': +(adjusted_state_income-)*.113,
                                                'tier 9': +(adjusted_state_income-)*.12},
                                    'seperate': {'tier 1': +(adjusted_state_income-)*.01,
                                                 'tier 2': +(adjusted_state_income-)*.02,
                                                 'tier 3': +(adjusted_state_income-)*.04,
                                                 'tier 4': +(adjusted_state_income-)*.06,
                                                 'tier 5': +(adjusted_state_income-)*.08,
                                                 'tier 6': +(adjusted_state_income-)*.093,
                                                 'tier 7': +(adjusted_state_income-)*.103,
                                                 'tier 8': +(adjusted_state_income-)*.113,
                                                 'tier 9': +(adjusted_state_income-)*.12},
                                   'head of house':{'tier 1': +(adjusted_state_income-)*.01,
                                                    'tier 2': +(adjusted_state_income-)*.02,
                                                    'tier 3': +(adjusted_state_income-)*.04,
                                                    'tier 4': +(adjusted_state_income-)*.06,
                                                    'tier 5': +(adjusted_state_income-)*.08,
                                                    'tier 6': +(adjusted_state_income-)*.093,
                                                    'tier 7': +(adjusted_state_income-)*.103,
                                                    'tier 8': +(adjusted_state_income-)*.113,
                                                    'tier 9': +(adjusted_state_income-)*.123}
                                  }, 
                     'colorado': adjusted_state_income*.0455, 
                     'connecticut': {'single': , {'tier 1': adjusted_state_income*.03,
                                                  'tier 2': +(adjusted_state_income-)*.05,
                                                  'tier 3': +(adjusted_state_income-)*.055,
                                                  'tier 4': +(adjusted_state_income-)*.06,
                                                  'tier 5': +(adjusted_state_income-)*.065,
                                                  'tier 6': +(adjusted_state_income-)*.069,
                                                  'tier 7': +(adjusted_state_income-)*.0699},
                                    'jointly': {'tier 1': +(adjusted_state_income-)*.03,
                                                'tier 2': +(adjusted_state_income-)*.05,
                                                'tier 3': +(adjusted_state_income-)*.055,
                                                'tier 4': +(adjusted_state_income-)*.06,
                                                'tier 5': +(adjusted_state_income-)*.065,
                                                'tier 6': +(adjusted_state_income-)*.069,
                                                'tier 7': +(adjusted_state_income-)*.0699},
                                    'seperate': {'tier 1': +(adjusted_state_income-)*.03,
                                                 'tier 2': +(adjusted_state_income-)*.05,
                                                 'tier 3': +(adjusted_state_income-)*.055,
                                                 'tier 4': +(adjusted_state_income-)*.06,
                                                 'tier 5': +(adjusted_state_income-)*.065,
                                                 'tier 6': +(adjusted_state_income-)*.069,
                                                 'tier 7': +(adjusted_state_income-)*.0699},
                                    'head of house':{'tier 1': +(adjusted_state_income-)*.03,
                                                     'tier 2': +(adjusted_state_income-)*.05,
                                                     'tier 3': +(adjusted_state_income-)*.055,
                                                     'tier 4': +(adjusted_state_income-)*.06,
                                                     'tier 5': +(adjusted_state_income-)*.065,
                                                     'tier 6': +(adjusted_state_income-)*.069,
                                                     'tier 7': +(adjusted_state_income-)*.0699}
                                     }, 
                     'delaware': {'single': , {'tier 1': adjusted_state_income*.022,
                                               'tier 2': +(adjusted_state_income-)*.039,
                                               'tier 3': +(adjusted_state_income-)*.048,
                                               'tier 4': +(adjusted_state_income-)*.052,
                                               'tier 5': +(adjusted_state_income-)*.0555,
                                               'tier 6': +(adjusted_state_income-)*.066,
                                  'jointly': {'tier 1': +(adjusted_state_income-)*.022},
                                              'tier 2': +(adjusted_state_income-)*.039,
                                              'tier 3': +(adjusted_state_income-)*.048,
                                              'tier 4': +(adjusted_state_income-)*.052,
                                              'tier 5': +(adjusted_state_income-)*.0555,
                                              'tier 6': +(adjusted_state_income-)*.066},
                                  'seperate': {'tier 1': +(adjusted_state_income-)*.022,
                                               'tier 2': +(adjusted_state_income-)*.039,
                                               'tier 3': +(adjusted_state_income-)*.048,
                                               'tier 4': +(adjusted_state_income-)*.052,
                                               'tier 5': +(adjusted_state_income-)*.0555,
                                               'tier 6': +(adjusted_state_income-)*.066},
                                 'head of house':{'tier 1': +(adjusted_state_income-)*.022,
                                                  'tier 2': +(adjusted_state_income-)*.039,
                                                  'tier 3': +(adjusted_state_income-)*.048,
                                                  'tier 4': +(adjusted_state_income-)*.052,
                                                  'tier 5': +(adjusted_state_income-)*.0555,
                                                  'tier 6': +(adjusted_state_income-)*.066}
                                 }
                     'georgia': {'single': , {'tier 1': adjusted_state_income*.01,
                                              'tier 2': +(adjusted_state_income-)*.02,
                                              'tier 3': +(adjusted_state_income-)*.03,
                                              'tier 4': +(adjusted_state_income-)*.04,
                                              'tier 5': +(adjusted_state_income-)*.05,
                                              'tier 6': +(adjusted_state_income-)*.0575},
                                 'jointly': {'tier 1': +(adjusted_state_income-)*.01,
                                             'tier 2': +(adjusted_state_income-)*.02,
                                             'tier 3': +(adjusted_state_income-)*.03,
                                             'tier 4': +(adjusted_state_income-)*.04,
                                             'tier 5': +(adjusted_state_income-)*.05,
                                             'tier 6': +(adjusted_state_income-)*.0575},
                                  'seperate': {'tier 1': +(adjusted_state_income-)*.01,
                                               'tier 2': +(adjusted_state_income-)*.02,
                                               'tier 3': +(adjusted_state_income-)*.03,
                                               'tier 4': +(adjusted_state_income-)*.04,
                                               'tier 5': +(adjusted_state_income-)*.05,
                                               'tier 6': +(adjusted_state_income-)*.0575},
                                   'head of house':{'tier 1': +(adjusted_state_income-)*.01,
                                                    'tier 2': +(adjusted_state_income-)*.02,
                                                    'tier 3': +(adjusted_state_income-)*.03,
                                                    'tier 4': +(adjusted_state_income-)*.04,
                                                    'tier 5': +(adjusted_state_income-)*.05,
                                                    'tier 6': +(adjusted_state_income-)*.0575}
                               }, 
                     'hawaii': {'single': , {'tier 1': adjusted_state_income*.014,
                                             'tier 2': +(adjusted_state_income-)*.032,
                                             'tier 3': +(adjusted_state_income-)*.055,
                                             'tier 4': +(adjusted_state_income-)*.064,
                                             'tier 5': +(adjusted_state_income-)*.068,
                                             'tier 6': +(adjusted_state_income-)*.072,
                                             'tier 7': +(adjusted_state_income-)*.076,
                                             'tier 8': +(adjusted_state_income-)*.079,
                                             'tier 9': +(adjusted_state_income-)*.0825,
                                             'tier 10': +(adjusted_state_income-)*.09,
                                             'tier 11': +(adjusted_state_income-)*.1,
                                             'tier 12': +(adjusted_state_income-)*.11},
                                'jointly': {'tier 1': +(adjusted_state_income-)*.014,
                                            'tier 2': +(adjusted_state_income-)*.032,
                                            'tier 3': +(adjusted_state_income-)*.055,
                                            'tier 4': +(adjusted_state_income-)*.064,
                                            'tier 5': +(adjusted_state_income-)*.068,
                                            'tier 6': +(adjusted_state_income-)*.072,
                                            'tier 7': +(adjusted_state_income-)*.076,
                                            'tier 8': +(adjusted_state_income-)*.079,
                                            'tier 9': +(adjusted_state_income-)*.0825,
                                            'tier 10': +(adjusted_state_income-)*.09,
                                            'tier 11': +(adjusted_state_income-)*.1,
                                            'tier 12': +(adjusted_state_income-)*.11},
                                 'seperate': {'tier 1': +(adjusted_state_income-)*.014,
                                              'tier 2': +(adjusted_state_income-)*.032,
                                              'tier 3': +(adjusted_state_income-)*.055,
                                              'tier 4': +(adjusted_state_income-)*.064,
                                              'tier 5': +(adjusted_state_income-)*.068,
                                              'tier 6': +(adjusted_state_income-)*.072,
                                              'tier 7': +(adjusted_state_income-)*.076,
                                              'tier 8': +(adjusted_state_income-)*.079,
                                              'tier 9': +(adjusted_state_income-)*.0825,
                                              'tier 10': +(adjusted_state_income-)*.09,
                                              'tier 11': +(adjusted_state_income-)*.1,
                                              'tier 12': +(adjusted_state_income-)*.11},
                                 'head of house':{'tier 1': +(adjusted_state_income-)*.014,
                                                  'tier 2': +(adjusted_state_income-)*.032,
                                                  'tier 3': +(adjusted_state_income-)*.055,
                                                  'tier 4': +(adjusted_state_incomem-)*.064,
                                                  'tier 5': +(adjusted_state_income-)*.068,
                                                  'tier 6': +(adjusted_state_income-)*.072,
                                                  'tier 7': +(adjusted_state_income-)*.076,
                                                  'tier 8': +(adjusted_state_income-)*.079,
                                                  'tier 9': +(adjusted_state_income-)*.0825,
                                                  'tier 10': +(adjusted_state_income-)*.09,
                                                  'tier 11': +(adjusted_state_income-)*.1,
                                                  'tier 12': +(adjusted_state_income-)*.11}
                                  }, 
                     'idaho': {'single': , {'tier 1': adjusted_state_income*.01,
                                            'tier 2': +(adjusted_state_income-)*.031,
                                            'tier 3': +(adjusted_state_income-)*.045,
                                            'tier 4': +(adjusted_state_income-)*.055,
                                            'tier 5': +(adjusted_state_income-)*.065},
                                'jointly': {'tier 1': +(adjusted_state_income-)*.01,
                                            'tier 2': +(adjusted_state_income-)*.031,
                                            'tier 3': +(adjusted_state_income-)*.045,
                                            'tier 4': +(adjusted_state_income-)*.055,
                                            'tier 5': +(adjusted_state_income-)*.065},
                                 'seperate': {'tier 1': +(adjusted_state_income-)*.01,
                                              'tier 2': +(adjusted_state_income-)*.031,
                                              'tier 3': +(adjusted_state_income-)*.045,
                                              'tier 4': +(adjusted_state_income-)*.055,
                                              'tier 5': +(adjusted_state_income-)*.065},
                                 'head of house':{'tier 1': +(adjusted_state_income-)*.01,
                                                  'tier 2': +(adjusted_state_income-)*.031,
                                                  'tier 3': +(adjusted_state_income-)*.045,
                                                  'tier 4': +(adjusted_state_income-)*.055,
                                                  'tier 5': +(adjusted_state_income-)*.065}
                              }, 
                     'illinois': sum*.0495,
                     'indiana': sum*.0323,
                     'iowa': {'single': , {'tier 1': adjusted_state_income*.0033,
                                           'tier 2': 5.75+(adjusted_state_income-1743)*.0067,
                                           'tier 3': 17.43+(adjusted_state_income-3486)*.0225,
                                           'tier 4': 95.87+(adjusted_state_income-6972)*.0414,
                                           'tier 5': 456.67+(adjusted_state_income-15687)*.0563,
                                           'tier 6': 1045.46+(adjusted_state_income-26145)*.0596,
                                           'tier 7': 1564.87+(adjusted_state_income-34860)*.0625,
                                           'tier 8': 2654.25+(adjusted_state_income-52290)*.0744,
                                           'tier 9': 4599.44+(adjusted_state_income-78435)*.0853},
                               'jointly': {'tier 1': +(adjusted_state_income-)*.0033,
                                           'tier 2': +(adjusted_state_income-)*.0067,
                                           'tier 3': +(adjusted_state_income-)*.0225,
                                           'tier 4': +(adjusted_state_income-)*.0414,
                                           'tier 5': +(adjusted_state_income-)*.0563,
                                           'tier 6': +(adjusted_state_income-)*.0596,
                                           'tier 7': +(adjusted_state_income-)*.0625,
                                           'tier 8': +(adjusted_state_income-)*.0744,
                                           'tier 9': +(adjusted_state_income-)*.0853},
                                'seperate': {'tier 1': +(adjusted_state_income-)*.0033,
                                             'tier 2': +(adjusted_state_income-)*.0067,
                                             'tier 3': +(adjusted_state_income-)*.0225,
                                             'tier 4': +(adjusted_state_income-)*.0414,
                                             'tier 5': +(adjusted_state_income-)*.0563,
                                             'tier 6': +(adjusted_state_income-)*.0596,
                                             'tier 7': +(adjusted_state_income-)*.0625,
                                             'tier 8': +(adjusted_state_income-)*.0744,
                                             'tier 9': +(adjusted_state_income-)*.0853},
                               'head of house':{'tier 1': +(adjusted_state_income-)*.0033,
                                                'tier 2': +(adjusted_state_income-)*.0067,
                                                'tier 3': +(adjusted_state_income-)*.0225,
                                                'tier 4': +(adjusted_state_income-)*.0414,
                                                'tier 5': +(adjusted_state_income-)*.0563,
                                                'tier 6': +(adjusted_state_income-)*.0596,
                                                'tier 7': +(adjusted_state_income-)*.0625,
                                                'tier 8': +(adjusted_state_income-)*.0744,
                                                'tier 9': +(adjusted_state_income-)*.0853}
                             }, 
                     'kansas': {'single': , {'tier 1': adjusted_state_income*.031,
                                             'tier 2': 465+(adjusted_state_income-15000)*.0525,
                                             'tier 3': 1252.5+(adjusted_state_income-30000)*.057},
                                'jointly': {'tier 1': adjusted_state_income*.031,
                                            'tier 2': 930+(adjusted_state_income-30000)*.0525,
                                            'tier 3': 2505+(adjusted_state_income-60000)*.057},
                                'seperate': {'tier 1': adjusted_state_income*.031,
                                             'tier 2': 465+(adjusted_state_income-15000)*.0525,
                                             'tier 3': 1252.5+(adjusted_state_income-30000)*.057},
                                'head of house':{'tier 1': adjusted_state_income*.031,
                                                 'tier 2': 930+(adjusted_state_income-15000)*.0525,
                                                 'tier 3': 2505+(adjusted_state_income-60000)*.057}
                             }, 
                     'kentucky': .05, 
                     'louisiana': {'single': , {'tier 1': adjusted_state_income*.0185,
                                                'tier 2': 231.25+(adjusted_state_income-12500)*.0350,
                                                'tier 3': 1543.75+(adjusted_state_income-50000)*.0425},
                                   'jointly': {'tier 1': adjusted_state_income*.0185,
                                               'tier 2': 462.5+(adjusted_state_income-25000)*.0350,
                                               'tier 3': 3087.50+(adjusted_state_income-100000)*.0425},
                                   'seperate': {'tier 1': adjusted_state_income*.0185,
                                                'tier 2': 231.25+(adjusted_state_income-12500)*.0350,
                                                'tier 3': 1543.75+(adjusted_state_income-50000)*.0425},
                                   'head of house':{'tier 1': adjusted_state_income*.0185,
                                                    'tier 2': 231.25+(adjusted_state_income-12500)*.0350,
                                                    'tier 3': 1543.75+(adjusted_state_income-50000)*.0425}
                                   }, 
                     'maine': {'single': , {'tier 1': adjusted_state_income*.058,
                                            'tier 2': 133.4+(adjusted_state_income-23000)*.0675,
                                            'tier 3': 2382.08+(adjusted_state_income-54450)*.0715},
                               'jointly': {'tier 1': adjusted_state_income*.058,
                                           'tier 2': 2668+(adjusted_state_income-46000)*.0675,
                                           'tier 3': 6914+(adjusted_state_income-108900)*.0715},
                               'seperate': {'tier 1': adjusted_state_income*.058,
                                            'tier 2': 133.4+(adjusted_state_income-23000)*.0675,
                                            'tier 3': 2382.08+(adjusted_state_income-54450)*.0715},
                               'head of house':{'tier 1': adjusted_state_income*.058,
                                                'tier 2': 2001+(adjusted_state_income-34500)*.0675,
                                                'tier 3': 5187+(adjusted_state_income-81700)*.0715}
                              }, 
                     'maryland': {'single': , {'tier 1': adjusted_state_income*.02,
                                               'tier 2': 20+(adjusted_state_income-1000)*.03,
                                               'tier 3': 50+(adjusted_state_income-2000)*.04,
                                               'tier 4': 90+(adjusted_state_income-3000)*.0475,
                                               'tier 5': 4697.5+(adjusted_state_income-100000)*.05,
                                               'tier 6': 5947.5+(adjusted_state_income-125000)*.0525,
                                               'tier 7': 7260+(adjusted_state_income-150000)*.055,
                                               'tier 8': 12760+(adjusted_state_income-250000)*.0575},
                                  'jointly': {'tier 1': adjusted_state_income*.02,
                                              'tier 2': 20+(adjusted_state_income-1000)*.03,
                                              'tier 3': 50+(adjusted_state_income-2000)*.04,
                                              'tier 4': 90+(adjusted_state_income-3000)*.0475,
                                              'tier 5': 7072.5+(adjusted_state_income-150000)*.05,
                                              'tier 6': 8332.5+(adjusted_state_income-175000)*.0525,
                                              'tier 7': 10947.5+(adjusted_state_income-225000)*.055,
                                              'tier 8': 15072.5+(adjusted_state_income-300000)*.0575},
                                  'seperate': {'tier 1': adjusted_state_income*.02,
                                               'tier 2': 20+(adjusted_state_income-1000)*.03,
                                               'tier 3': 50+(adjusted_state_income-2000)*.04,
                                               'tier 4': 90+(adjusted_state_income-3000)*.0475,
                                               'tier 5': 4697.5+(adjusted_state_income-100000)*.05,
                                               'tier 6': 5947.5+(adjusted_state_income-125000)*.0525,
                                               'tier 7': 7260+(adjusted_state_income-150000)*.055,
                                               'tier 8': 12760+(adjusted_state_income-250000)*.0575},
                                  'head of house':{'tier 1': adjusted_state_income*.02,
                                                   'tier 2': 20+(adjusted_state_income-1000)*.03,
                                                   'tier 3': 50+(adjusted_state_income-2000)*.04,
                                                   'tier 4': 90+(adjusted_state_income-3000)*.0475,
                                                   'tier 5': 7072.50+(adjusted_state_income-150000)*.05,
                                                   'tier 6': 8332.5+(adjusted_state_income-175000)*.0525,
                                                   'tier 7': 10947.5+(adjusted_state_income-225000)*.055,
                                                   'tier 8': 15072.5+(adjusted_state_income-300000)*.0575}
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
                     'montana': {'single': , {'tier 1': adjusted_state_income*.1,
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
                     'nebraska': {'single': , {'tier 1': adjusted_state_income*.1,
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
                             }
                     'new hampshire': adjusted_state_income*.05, 
                     'new jersey': {'single': , {'tier 1': adjusted_state_income*.1,
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
                     'new mexico': {'single': , {'tier 1': adjusted_state_income*.1,
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
                                      }, 
                     'new york': {'single': , {'tier 1': adjusted_state_income*.1,
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
                     'north carolina': adjusted_state_income*.0525,
                     'north dakota': {'single': , {'tier 1': adjusted_state_income*.1,
                                                   'tier 2': +(adjusted_state_income-)*.12,
                                                   'tier 3': +(adjusted_state_income-)*.12,
                                                   'tier 4': +(adjusted_state_income-)*.12,
                                                   'tier 5': +(adjusted_state_income-)*.12},
                                       'jointly': {'tier 1': +(adjusted_state_income-)*.12,
                                                   'tier 2': +(adjusted_state_income-)*.12,
                                                   'tier 3': +(adjusted_state_income-)*.12,
                                                   'tier 4': +adjusted_state_income-)*.12,
                                                   'tier 5': +(adjusted_state_income-)*.12},
                                        'seperate': {'tier 1': +(adjusted_state_income-)*.12,
                                                     'tier 2': +(adjusted_state_income-)*.12,
                                                     'tier 3': +(adjusted_state_income-)*.12,
                                                     'tier 4': +(adjusted_state_income-)*.12,
                                                     'tier 5': +(adjusted_state_income-)*.12},
                                        'head of house':{'tier 1': +(adjusted_state_income-)*.12,
                                                         'tier 2': +(adjusted_state_income-)*.12,
                                                         'tier 3': +(adjusted_state_income-)*.12,
                                                         'tier 4': +(adjusted_state_income-)*.12,
                                                         'tier 5': +(adjusted_state_income-)*.12}
                                      }, 
                     'ohio': {'single': , {'tier 1': adjusted_state_income*.1,
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
                     'oklahoma': {'single': , {'tier 1': adjusted_state_income*.1,
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
                     'oregon': {'single': , {'tier 1': adjusted_state_income*.1,
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
                                }, 
                     'pennsylvania': adjusted_state_income*.0307, 
                     'rhode island': {'single': , {'tier 1': adjusted_state_income*.1,
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
                     'south carolina': {'single': , {'tier 1': adjusted_state_income*.1,
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
                      } 
                     'tennessee': {'single': , {'tier 1': adjusted_state_income*.1,
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
                                                   'tier 17': +(adjusted_state_income-)*.12}
                                   }
                     'utah': adjusted_state_income*.0495, 
                     'vermont': {'single': , {'tier 1': adjusted_state_income*.1,
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
                                }, 
                     'virginia': {'single': , {'tier 1': adjusted_state_income*.1,
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
                                }
                     'west virginia': {'single': , {'tier 1': adjusted_state_income*.1,
                                                    'tier 2': +(adjusted_state_income-)*.12,
                                                    'tier 3': +(adjusted_state_income-)*.12,
                                                    'tier 4': +(adjusted_state_income-)*.12,
                                                    'tier 5': +(adjusted_state_income-)*.12},
                                      'jointly': {'tier 1': +(adjusted_state_income-)*.12,
                                                  'tier 2': +(adjusted_state_income-)*.12,
                                                  'tier 3': +(adjusted_state_income-)*.12,
                                                  'tier 4': +(adjusted_state_income-)*.12,
                                                  'tier 5': +(adjusted_state_income-)*.12},
                                      'seperate': {'tier 1': +(adjusted_state_income-)*.12,
                                                   'tier 2': +(adjusted_state_income-)*.12,
                                                   'tier 3': +(adjusted_state_income-)*.12,
                                                   'tier 4': +(adjusted_state_income-)*.12,
                                                   'tier 5': +(adjusted_state_income-)*.12},
                                     'head of house':{'tier 1': +(adjusted_state_income-)*.12,
                                                      'tier 2': +(adjusted_state_income-)*.12,
                                                      'tier 3': +(adjusted_state_income-)*.12,
                                                      'tier 4': +(adjusted_state_income-)*.12,
                                                      'tier 5': +(adjusted_state_income-)*.12}
                                     }, 
                     'wisconsin': {'single': , {'tier 1': adjusted_state_income*.1,
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
                                                     'tier 4': +(adjusted_state_income-)*.12}   }     }

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
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income -          
     elif state.lower() = 'arkansas':
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income -          
     elif state.lower() = 'california':
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income -          
     elif state.lower() = 'colorado':
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income -          
     elif state.lower() = 'connecticut':
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income -          
     elif state.lower() = 'delware':
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income -          
     elif state.lower() = 'georgia':
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income -          
     elif state.lower() = 'hawaii':
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income -          
     elif state.lower() = 'idaho':
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income -          
     elif state.lower() = 'illinois':
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income -          
     elif state.lower() = 'indiana':
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income -          
     elif state.lower() = 'iowa':
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 2210
          elif filing_status == 'jointly' or 'head of household': 
              adjusted_state_income = gross_income - 5450
     elif state.lower() = 'kansas':
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 12950
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 25900
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income - 19400
     elif state.lower() = 'kentucky':
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 2690
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 2690
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income - 2690 
          
     elif state.lower() = 'louisiana':
          if filing_status == 'single' or 'seperate' or 'head of household':
              adjusted_state_income = gross_income - 4500
              if adjusted_state_income <= 12500: 
                  state_tax_bracket[state][filling_status]['tier 1']
              elif 1250 < adjusted_state_income < 50000: 
                  state_tax_bracket[state][filling_status]['tier 2']          
              elif adjusted_state_income > 50000: 
                  state_tax_bracket[state][filling_status]['tier 3']          
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 9000
              if adjusted_state_income <= 25000: 
                  state_tax_bracket[state][filling_status]['tier 1']          
              elif 25000 < adjusted_state_income <100000: 
                  state_tax_bracket[state][filling_status]['tier 2']          
              elif adjusted_state_income > 10000: 
                  state_tax_bracket[state][filling_status]['tier 3']
          
     elif state.lower() = 'maine':
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 12950 
                  if adjusted_state_income <= 23000:
                      state_tax_bracket[state][filling_status]['tier 1']
                  elif 23000 < adjusted_state_income <= 54450: 
                      state_tax_bracket[state][filling_status]['tier 2']
                  elif adjusted_state_income > 54450: 
                      state_tax_bracket[state][filling_status]['tier 3']
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 25900
                  if adjusted_state_income <= 46000: 
                      state_tax_bracket[state][filling_status]['tier 1']
                  elif 46000 < adjusted_state_income <= 108900: 
                      state_tax_bracket[state][filling_status]['tier 2']
                  elif adjusted_state_income >108900 : 
                      state_tax_bracket[state][filling_status]['tier 3'] 
          
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income - 19400 
                  if adjusted_state_income <= 34500:
                      state_tax_bracket[state][filling_status]['tier 1']
                  elif 34500 < adjusted_state_income <= 81700 : 
                      state_tax_bracket[state][filling_status]['tier 2']
                  elif adjusted_state_income > 81700: 
                      state_tax_bracket[state][filling_status]['tier 3']
          
     elif state.lower() = 'maryland':
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 2350
              if adjusted_state_income <= 1000: 
                  state_tax_bracket[state][filling_status]['tier 1']
              elif 1000< adjusted_state_income <= 2000: 
                  state_tax_bracket[state][filling_status]['tier 2']
              elif 2000< adjusted_state_income <= 3000: 
                  state_tax_bracket[state][filling_status]['tier 3']
              elif 3000< adjusted_state_income <= 100000: 
                  state_tax_bracket[state][filling_status]['tier 4']
              elif 100000< adjusted_state_income <= 125000: 
                  state_tax_bracket[state][filling_status]['tier 5']
              elif 125000< adjusted_state_income <= 150000: 
                  state_tax_bracket[state][filling_status]['tier 6']
              elif 150000< adjusted_state_income <= 250000 : 
                  state_tax_bracket[state][filling_status]['tier 7']
              elif adjusted_state_income < 250000 : 
                  state_tax_bracket[state][filling_status]['tier 8']            
          elif filing_status == 'jointly' or 'head of household': 
              adjusted_state_income = gross_income -4700 
              if adjusted_state_income <= 1000: 
                  state_tax_bracket[state][filling_status]['tier 1']
              elif 1000< adjusted_state_income <= 2000: 
                  state_tax_bracket[state][filling_status]['tier 2']
              elif 2000< adjusted_state_income <= 3000: 
                  state_tax_bracket[state][filling_status]['tier 3']
              elif 3000< adjusted_state_income <=150000 : 
                  state_tax_bracket[state][filling_status]['tier 4']
              elif 150000< adjusted_state_income <=175000 : 
                  state_tax_bracket[state][filling_status]['tier 5']
              elif 175000< adjusted_state_income <= 225000: 
                  state_tax_bracket[state][filling_status]['tier 6']
              elif 225000< adjusted_state_income <= 300000: 
                  state_tax_bracket[state][filling_status]['tier 7']        
              elif adjusted_state_income < 300000 : 
                  state_tax_bracket[state][filling_status]['tier 8']          
          
     elif state.lower() = 'massachuetts':
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income -          
     elif state.lower() = 'michigan':               
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income -          
     elif state.lower() = 'minnesota':
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income -          
     elif state.lower() = 'mississippi':
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income -          
     elif state.lower() = 'missouri':
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income -          
     elif state.lower() = 'montana':
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income -          
     elif state.lower() = 'nebraska':
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income -          
     elif state.lower() = 'new hampshire':
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income -          
     elif state.lower() = 'new jersey':
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income -          
     elif state.lower() = 'new mexico':
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income -          
     elif state.lower() = 'new york':
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income -          
     elif state.lower() = 'north carolina': 
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income -          
     elif state.lower() = 'north dakota':
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income -          
     elif state.lower() = 'ohio':
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income -          
     elif state.lower() = 'oklahoma':
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income -          
     elif state.lower() = 'oregon':
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income -          
     elif state.lower() = 'pennslyvania':
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income -          
     elif state.lower() = 'rhode island':
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income -          
     elif state.lower() = 'south carolina': 
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income -          
     elif state.lower() = 'tennessee':
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income -          
     elif state.lower() = 'utah':
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income -          
     elif state.lower() = 'vermont':         
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income -          
     elif state.lower() = 'virgina':
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income -          
     elif state.lower() = 'west virgina':
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income -          
     elif state.lower() = 'wisconsin':
          if filing_status == 'single' or 'seperate':
              adjusted_state_income = gross_income - 
          elif filing_status == 'jointly': 
              adjusted_state_income = gross_income - 
          elif filing_status == 'head of household': 
              adjusted_state_income = gross_income -     
          
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
