def first_iteration(numbers):
    output_numbers = numbers[:1]
    replace_even = numbers[0] % 2 != 0

    for num in numbers[1:]:
        is_num_even = num % 2 == 0
        if replace_even == is_num_even: # if number parity == replace parity, skip
            continue

        output_numbers.append(num)

    return output_numbers

def next_iterations(iteration, numbers):
    skip_every_n = numbers[iteration]
    skipped_numbers = list(range(0, len(numbers), skip_every_n))
    output_numbers = []

    for i, num in enumerate(numbers):
        if i + 1 in skipped_numbers and i > iteration:
            continue
        
        output_numbers.append(num)
    return output_numbers

def happy_numbers(numbers):
    output = first_iteration(numbers)
    iteration = 1

    while len(output) > output[iteration]:
        output = next_iterations(iteration, output)
        iteration += 1

    return output

def run_function_tests(function, tests):
    print("testing {0} function".format(function.__name__))

    for i, test in enumerate(tests):
        print("running test #{0}".format(i))
        output = function(*test[0])
        if output != test[1]:
            print ("input: {0}, output: {1}, expected: {2}".format(test[0], output, test[1]))
        else:
            print ("test #{0} passed".format(i))

def run_first_iteration_tests():
    tests_first_iteration = [
        ([list(range(1, 26))], [1,3,5,7,9,11,13,15,17,19,21,23,25])
    ]

    run_function_tests(first_iteration, tests_first_iteration)

def run_next_iteration_tests():
    tests_next_iteration = [
        ([1, [1,3,5,7,9,11,13,15,17,19,21,23,25]], [1,3,7,9,13,15,19,21,25]),
        ([2, [1,3,7,9,13,15,19,21,25]], [1, 3, 7, 9, 13, 15, 21, 25])
    ]

    run_function_tests(next_iterations, tests_next_iteration)

def run_happy_numbers_tests():
    tests_happy_numbers = [
        ([list(range(1,26))], [1,3,7,9,13,15,21,25])
    ]

    run_function_tests(happy_numbers, tests_happy_numbers)

def run_tests():
    run_first_iteration_tests()
    run_next_iteration_tests()
    run_happy_numbers_tests()

if __name__ == "__main__":
    run_tests()
