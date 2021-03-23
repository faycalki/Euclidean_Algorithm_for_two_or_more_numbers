# To do: improve the modularity functionality by restructuring the modular function in such a way that you can call its modularity when modularity == 1 for more than two integers. Right now i'm just using a workaround.


def errormessage_function(number):
    if number == 1:
        print("Please input an integer, and make sure the integer is not zero.")
    elif number == 2:
        print("Input at least two integers to compute the hcf and lcm of.")
    else:
        pass


# Finds the smallest s,t integers such that sa + tb = hcf(a,b)


def bezouts_identity(a, b):
    if b == 0:
        return 1, 0, a
    else:
        q, r = divmod(a, b)
        x, y, g = bezouts_identity(b, r)
        return y, x - q * y, g

    # Finds positive integer s such that ya + sb = hcf(a,b)


def bezouts_identity_positive(s, a, b):
    if s < 0:
        while s * b < 0:
            s = s + a * b
        return s


def inductive_traversal_lcm(list_of_discretes, hcf):
    result = 1
    for t in list_of_discretes:
        result = result * t
    return result // hcf


def modular_euclidean_algorithm(
    string_n,
    modularity,
    first_factor_modularity,
    second_factor_modularity,
    *args,
    **kwargs
):
    discrete_n = int(string_n)
    discrete_n_list = []
    discrete_n_list_copy = []

    def ints_feeder(
        modularity,
        discrete_n,
        discrete_n_list,
        discrete_n_list_copy,
    ):

        count_discrete_number = 0
        if modularity == 0:
            while count_discrete_number < discrete_n:
                string_int = input("Input an integer: ")
                if string_int == "q":
                    quit_program()
                try:
                    int(string_int)
                except ValueError:
                    errormessage_function(1)
                else:
                    if int(string_int) == 0:
                        errormessage_function(1)
                    else:
                        discrete_n_list.append(int(string_int))
                        discrete_n_list_copy.append(int(string_int))
                        count_discrete_number += 1
        else:
            try:
                int(first_factor_modularity)
                int(second_factor_modularity)

            except ValueError:
                errormessage_function(1)
            else:
                if (
                    int(first_factor_modularity) == 0
                    or int(second_factor_modularity) == 0
                ):
                    errormessage_function(1)
                else:
                    discrete_n_list.append(int(first_factor_modularity))
                    discrete_n_list_copy.append(int(first_factor_modularity))
                    discrete_n_list.append(int(second_factor_modularity))
                    discrete_n_list_copy.append(int(second_factor_modularity))
                    count_discrete_number += 1

    if modularity == 0:
        ints_feeder(
            modularity,
            discrete_n,
            discrete_n_list,
            discrete_n_list_copy,
        )
    elif modularity == 1:
        ints_feeder(
            modularity,
            discrete_n,
            discrete_n_list,
            discrete_n_list_copy,
        )

    iterate_count = 1
    while iterate_count < discrete_n:
        if discrete_n_list[0] >= discrete_n_list[1]:
            r_i = discrete_n_list[0] % discrete_n_list[1]

            def recursive_euclidean_algorithm(a, b, r_i):
                if r_i == 0:
                    if modularity == 0:
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

            recursive_euclidean_algorithm(discrete_n_list[0], discrete_n_list[1], r_i)
            iterate_count += 1

        elif discrete_n_list[1] > discrete_n_list[0]:
            r_i = discrete_n_list[1] % discrete_n_list[0]

            def recursive_euclidean_algorithm(a, b, r_i):
                if r_i == 0:
                    if modularity == 0:
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

            recursive_euclidean_algorithm(discrete_n_list[0], discrete_n_list[1], r_i)
            iterate_count += 1
    if modularity == 0:
        print(
            "Number of iterations performed for computations: %d" % (iterate_count - 1)
        )
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
        list_to_return = []
        list_to_return.append(discrete_n_list[0])
        list_to_return.append(
            inductive_traversal_lcm(discrete_n_list_copy, discrete_n_list[0])
        )
        return list_to_return
