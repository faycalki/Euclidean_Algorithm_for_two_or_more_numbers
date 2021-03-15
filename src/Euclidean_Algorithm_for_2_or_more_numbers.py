#   Purpose and version of program
__purpose__ = "This program computes the highest common factor and lowest common multiple of any n number of integers."
__version__ = "Program Version: 2.0"

#   License and Author
__author__ = "Faycal Kilali"
__copyright__ = "Copyright (C) 2021 Faycal Kilali"
__license__ = "GNU GENERAL PUBLIC LICENSE"
__license_version__ = "3.0"

#   Display purpose and version, license and version of license.
print(__purpose__, "\n", __version__)
print(__copyright__, "\n", __license__, __license_version__, "\n")

# Importing License disclaimer and extra details input
from license_input import *
reveal_license_options()

# Importing exit implementation
from exit_with_q_module import quit_program


def errormessage_function(number):
    if number == 1:
        print("Please input an integer, and make sure the integer is not zero.")
    elif number == 2:
        print("Input at least two integers to compute the hcf and lcm of.")
    else:
        pass


def inductive_traversal_lcm(list_of_discretes, hcf):
    result = 1
    for t in list_of_discretes:
        result = result * t
    return result / hcf


halt = False
while halt == False:
    string_n = input(
        "Input the number of integers for which you would like to compute the hcf and lcm: "
    )
    try:
        int(string_n)
    except ValueError:
        errormessage_function(1)
        continue
    if int(string_n) < 2:
        errormessage_function(2)
    else:
        discrete_n = int(string_n)
        count_discrete_number = 0
        discrete_n_list = []
        discrete_n_list_copy = []
        while count_discrete_number < discrete_n:
            string_int = input("Input an integer: ")
            if string_int == "q":
                quit_program()
            try:
                int(string_int)
            except ValueError:
                errormessage_function(1)
                continue
            else:
                input_int = int(string_int)
                if input_int == 0:
                    errormessage_function(1)
                    continue
                else:
                    discrete_n_list.append(input_int)
                    discrete_n_list_copy.append(input_int)
                    count_discrete_number += 1

        iterate_count = 1
        while iterate_count < discrete_n:
            if discrete_n_list[0] >= discrete_n_list[1]:
                r_i = discrete_n_list[0] % discrete_n_list[1]

                def recursive_euclidean_algorithm(a, b, r_i):
                    if r_i == 0:
                        print(
                            "hcf of %d and %d is: %d"
                            % (discrete_n_list[0], discrete_n_list[1], b)
                        )
                        discrete_n_list.pop(0)
                        discrete_n_list.pop(0)
                        discrete_n_list.append(b)
                    else:
                        (a, b) = (b, r_i)
                        r_i = a % b
                        recursive_euclidean_algorithm(a, b, r_i)

                recursive_euclidean_algorithm(
                    discrete_n_list[0], discrete_n_list[1], r_i
                )
                iterate_count += 1

            elif discrete_n_list[1] > discrete_n_list[0]:
                r_i = discrete_n_list[1] % discrete_n_list[0]

                def recursive_euclidean_algorithm(a, b, r_i):
                    if r_i == 0:
                        print(
                            "hcf of %d and %d is: %d"
                            % (discrete_n_list[0], discrete_n_list[1], a)
                        )
                        discrete_n_list.pop(0)
                        discrete_n_list.pop(0)
                        discrete_n_list.append(a)
                    else:
                        (a, b) = (r_i, a)
                        r_i = b % a
                        recursive_euclidean_algorithm(a, b, r_i)

                recursive_euclidean_algorithm(
                    discrete_n_list[0], discrete_n_list[1], r_i
                )
                iterate_count += 1
            else:
                print("This message shouldn't appear.")
                iterate_count += 1
                break
        print(
            "Number of iterations performed for computations: %d" % (iterate_count - 1)
        )
        if iterate_count == count_discrete_number:
            print(
                "The highest common factor of the the integers in the list",
                discrete_n_list_copy,
                "is %d." % discrete_n_list[0],
            )
            print(
                "The lowest common multiple of the integers in the list %s is %d."
                % (
                    discrete_n_list_copy,
                    inductive_traversal_lcm(discrete_n_list_copy, discrete_n_list[0]),
                )
            )
        else:
            halt = True
            break