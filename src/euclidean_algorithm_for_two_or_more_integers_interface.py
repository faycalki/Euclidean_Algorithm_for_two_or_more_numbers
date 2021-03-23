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

# Additional directories to look for Modules
import sys

sys.path.append("Modules")

# Importing License disclaimer and extra details input
from license_input import *

reveal_license_options()

# Importing exit implementation
from exit_with_q_module import quit_program
import euclidean_algorithm_for_two_or_more_numbers_modular


def interface_main():
    modularity = 0
    first_factor_modularity = 7
    second_factor_modularity = 14
    third_factor_modularity = 27
    string_n = input(
        "Input the number of integers for which you would like to compute the hcf and lcm: "
    )
    if string_n == "q":
        exit_program()
    try:
        int(string_n)
    except ValueError:
        modular_euclidean_algorithm_for_two_or_more_numbers.errormessage_function(1)
    if int(string_n) < 2:
        modular_euclidean_algorithm_for_two_or_more_numbers.errormessage_function(2)
    else:

        euclidean_algorithm_for_two_or_more_numbers_modular.modular_euclidean_algorithm(
            string_n,
            modularity,
            first_factor_modularity,
            second_factor_modularity,
            third_factor_modularity,
        )

        interface_main()


interface_main()