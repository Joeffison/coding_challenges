#!/usr/bin/python
#
# Simple program for testing prospective Python developers

from copy import copy
import sys
import json
import math


# Allowable names for voltage, current, and power factor
V_NAMES = {'v', 'V', 'Volts', 'Voltage'}
I_NAMES = {'i', 'I', 'Amps', 'Amperes', 'Current'}
PF_NAMES = {'pf', 'PF', 'Power Factor'}


def calc_power(volts, amps, pf):
    '''Returns tuple of (p, q, s) powers from the inputs.'''
    try:
        s = volts * amps
        p = s * pf
        # TODO: calculate reactive power
        return (p, q, s)
    except (ValueError, TypeError):
        return (None, None, None)


# Run the program; expects a single argument which is the name of JSON file
if __name__ == "__main__":
    print("Hello World!")
    # Step 1: Read in the file "data1.json" and clean it so that we
    #       semantically understand and have known quantities for
    #       voltage, current, and power factor

    # Step 2: Create a new dictionary that has the same location
    #       as the primary key, but the value is three new
    #       calculated quantities:
    #           s = apparent power
    #           p = real power
    #           q = reactive power
    #
    #   Can use the "calc_power" function to help with this job

    # Step 3: Print out this new dictionary
