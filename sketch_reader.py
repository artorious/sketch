#!/usr/bin/env python3
"""
Loads some previously pickled data.
Uses pickle with nester to display data pickled by sketch.py
"""

import pickle
from scripts.nester import nester

new_man = []

try:
    with open('static/man_data.pickle', 'rb') as man_data:
        new_man = pickle.load(man_data)

except IOError as ioerr:
    print('File Error ->', ioerr)

except pickle.PickleError as perr:
    print('Pickling Error ->', perr)

nester(new_man)