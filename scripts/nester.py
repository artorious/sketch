#!/usr/bin/env python3
""" nester
module provides a function nester() 
Prints out python any lists to stdout.
"""
import sys
def nester(the_list, indent=False, level=0, data_output=sys.stdout):
    """ (list) -> stdout
    Takes a positional arg <the_list>, any python list.
    A second optional arg <indent>', initally set to value False.
    That is......do not switch indentation by default. 
    Third optional arg indent <level>, inserts tab-stops when a nested list is 
    encountered.
    A fourth optianal arg <data_output> identifies a place to write data to.
    Default is set to stdout

    Prints each item in the provided list recursively on it's own line.
    """

    if isinstance(the_list, list):
        for each_item in the_list :
            if isinstance(each_item, list):
                nester(each_item, indent, level + 1, data_output) # Increament indent level on each recursive call
            else:
                if indent:
                    for tab_stop in range(level): # No. of tab-stops used
                        print('\t', end='') # Display a TAB char for each level of inentation
                print(each_item, file=data_output)
    else:
        raise TypeError

    

