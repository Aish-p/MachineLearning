'''
Assume df is a pandas dataframe object of the dataset given
'''

import numpy as np
import pandas as pd
import random

'''Calculate the entropy of the enitre dataset'''
# input:pandas_dataframe
# output:int/float
def get_entropy_of_dataset(df):
    # TODO
    entropy = 0
    target = df[[df.columns[-1]]].values
    _, counts = np.unique(target, return_counts=True)
    total_count = np.sum(counts)
    for freq in counts:
        temp = freq/total_count
        if temp != 0:
            entropy -= temp*(np.log2(temp))
    return entropy

'''Return avg_info of the attribute provided as parameter'''
# input:pandas_dataframe,str   {i.e the column name ,ex: Temperature in the Play tennis dataset}
# output:int/float
def get_avg_info_of_attribute(df, attribute):
    # TODO
    avg_info = 0
    target, target_count = np.unique(df[attribute], return_counts=True)
    att_count = target_count / target_count.sum()
    entropy = np.array([])

    for i in range(len(target)):
        split = df.loc[df[attribute] == target[i]]
        x, count = np.unique(split.iloc[:,-1], return_counts=True)
        value = count / count.sum()
        entropy = np.append(entropy,-(value * np.log2(value)).sum())
    avg_info = (att_count * entropy).sum()
    return avg_info

'''Return Information Gain of the attribute provided as parameter'''
# input:pandas_dataframe,str
# output:int/float
def get_information_gain(df, attribute):
    # TODO
    information_gain = 0
    information_gain = get_entropy_of_dataset(df) - get_avg_info_of_attribute(df, attribute)
    return information_gain

#input: pandas_dataframe
#output: ({dict},'str')
def get_selected_attribute(df):
    '''
    Return a tuple with the first element as a dictionary which has IG of all columns 
    and the second element as a string with the name of the column selected

    example : ({'A':0.123,'B':0.768,'C':1.23} , 'C')
    '''
    # TODO
    information_gains = {}
    max_information_gain = float("-inf")
    for attribute in df.columns[:-1]:
        information_gain_of_attribute = get_information_gain(df, attribute)
        if information_gain_of_attribute > max_information_gain:
            selected_column = attribute
            max_information_gain = information_gain_of_attribute
        information_gains[attribute] = information_gain_of_attribute
    return (information_gains, selected_column)
    pass
