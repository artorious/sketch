#!/usr/bin/env python3
"""
A play on files and exceptions. 
    * Reading data from files
    * Exception handling
Persistance
    * Saving data to files
    * Pickling data
"""
# from scripts.nester import nester
import pickle

# Init
man = []
other_man = []

try: # Check that file exists
    # Init: Open file and assign object
    with open('text/sketch.txt') as the_file:
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
                print('No separator (:) in Line ->', each_line)
                
except IOError as no_file_err:
    print(no_file_err)

# try:
#     # Open output data files in write mode, assign to file objects
#     with open('text/man_data.txt', 'w') as man_file, \
#     open('text/other_man_data.txt', 'w') as other_man_file:
#         # Write to disk files in readable format
#         nester(man, data_output=man_file)
#         nester(other_man, data_output=other_man_file)  
    
# except IOError as file_err:
#     print('File Error', file_err)

# Save with dump and restore with load
try:
    with open('static/man_data.pickle', 'wb') as man_file, \
        open('static/other_man_data.pickle', 'wb') as other_man_file: # Access mode "writable, binary"
        pickle.dump(man, man_file)
        pickle.dump(other_man, other_man_file)
        
except pickle.PickleError as perr:
    print('Ooops...', perr)
