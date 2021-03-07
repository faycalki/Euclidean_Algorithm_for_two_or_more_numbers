#!/usr/bin/python
# -*- coding: utf-8 -*-
#   License and Author

__author__ = 'Faycal Kilali'
__copyright__ = 'Copyright (C) 2021 Faycal Kilali'
__license__ = '\nGNU GENERAL PUBLIC LICENSE'
__license_version__ = '3.0'

#   Purpose and version of program

purpose = \
    'This program computes the highest common factor of any two integers as well as their lowest common multiple.'
__version__ = '\nProgram Version: 1.1'

#   Display purpose and version, license and version of license.

print (purpose, __version__)
print (__copyright__, __license__, __license_version__)


def errormessage_function():
    print ('Please input an integer, and make sure the integer is not zero.')


halt = False
while halt == False:
    try:
        string_a = input('Input an integer: ')  # Obtain user input as a string
        try:
            float(string_a)
        except ValueError:
            errormessage_function()
            continue
        if len(string_a) == 0:
            errormessage_function()
            continue
        else:
            a = int(string_a)  # Assign user input as an integer to the variable a
        if a == 0:
            errormessage_function()
            continue
        string_b = input('Input a second integer: ')  # Obtain second user input as a string
        try:
            float(string_b)
        except ValueError:
            errormessage_function()
            continue
        if len(string_b) == 0:
            errormessage_function()
            continue
        else:
            b = int(string_b)  # Assign second user input string into an integer then assign to b
        if b == 0:
            errormessage_function()
            continue
        else:

   # Placeholder variables in order for LCM computation to work

            a_x = a
            b_x = b

   # Further conditionals required for the euclidean algorithm

        if a > b:
            r_i = a % b


            def recursive_euclidean_algorithm(a, b, r_i):  # Recursion for when a is larger than or equal to b. This function is defined for the conditional above.
                if r_i == 0:
                    lcm_ab = a_x * b_x // b
                    print ('hcf =', b)
                    print ('lcm =', lcm_ab)
                    return
                else:
                    (a, b) = (b, r_i)
                    r_i = a % b
                    recursive_euclidean_algorithm(a, b, r_i)


            recursive_euclidean_algorithm(a, b, r_i)
        elif b >= a:
            r_i = b % a


            def recursive_euclidean_algorithm(a, b, r_i):  # Recursion for when b is larger than or equal to a. This function is defined for the conditional above.
                if r_i == 0:
                    lcm_ab = a_x * b_x // a
                    print ('hcf =', a)
                    print ('lcm =', lcm_ab)
                    return
                else:
                    (a, b) = (r_i, a)
                    r_i = b % a
                    recursive_euclidean_algorithm(a, b, r_i)


            recursive_euclidean_algorithm(a, b, r_i)
    except EOFError as e:

        # Prevents end of file error

        print (e)
        halt = True
