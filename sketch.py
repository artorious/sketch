#!/usr/bin/env python3
"""
A play on files and exceptions. 
    * Reading data from files
    * Exception handling
Persistance
    * Saving data to files
"""

try: # Check that file exists
    # Init
    the_file = open('sketch.txt') # Open file and assign object

    # Process data, extract each part from each line and display on screen

    for each_line in the_file:
    # Skip lines that dont contain separator
        try:
            (role, line_spoken) = each_line.split(':', 1)
            print(role, end='')
            print(' SAID: ', end='')
            print(line_spoken, end='')
        
        except ValueError as data_err:
            print(data_err)
            

    the_file.close() # Close file object

except IOError as no_file_err:
    print(no_file_err)