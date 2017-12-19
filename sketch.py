#!/usr/bin/env python3
"""
A play on files and exceptions. 
    * Reading data from files
    * Exception handling
Persistance
    * Saving data to files
"""

# Init
man = []
other_man = []

try: # Check that file exists
    # Init
    the_file = open('sketch.txt') # Open file and assign object

    # Process data, extract each part from each line, append to list and 
    # save to appropriate file

    for each_line in the_file:
    # Skip lines that dont contain separator
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other_man.append(line_spoken)
        
        except ValueError as data_err:
            print(data_err, ': Line skipped (ignored)')
            print('No separator (:) in Line ->',each_line)
            
    the_file.close() # Close file object

except IOError as no_file_err:
    print(no_file_err)

try:
    # Open output data files in write mode, assign to file objects
    man_file = open('man_data.txt', 'w')
    other_man_file = open('other_man_data.txt', 'w')
    # Write to disk files
    print(man, file=man_file)
    print(other_man, file=other_man_file)

except IOError as file_err:
    print('File Error', file_err)

finally:
    man_file.close()
    other_man_file.close()
