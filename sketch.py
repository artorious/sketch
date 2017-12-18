#!/usr/bin/env python3
"""
A play on files and exceptions. 
    * Reading data from files
    * Exception handling
"""

# Init
the_file = open('sketch.txt') # Open file and assign object

print(the_file.readlines(), end='') # Print data in the file as list

the_file.close() # Close file object