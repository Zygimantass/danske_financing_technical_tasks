def replace_duplicate_letters(input_word):
    output_word = input_word[0]
    prev = input_word[0]
    for i, curr in enumerate(input_word[1:]): # enumerate string except last letter
        if curr == prev:
            continue

        prev = curr
        output_word += curr 

    return output_word

def replace_pi(input_word):
    return "3.14" if input_word == "pi" else input_word

def replace_pi_and_duplicate(sentence):
    words = sentence.split(" ")
    
    output_words = []

    for word in words:
        unduplicated_word = replace_duplicate_letters(word)
        replaced_pi_word = replace_pi(unduplicated_word)
        output_words.append(replaced_pi_word)

    return " ".join(output_words)

def run_function_tests(tests, function):
    print("testing {0} function".format(function.__name__))

    for i, test in enumerate(tests):
        print("running test #{0}".format(i))
        output = function(test[0])
        if output != test[1]:
            print ("input: {0}, output: {1}, expected: {2}".format(test[0], output, test[1]))
        else:
            print ("test #{0} passed".format(i))

def run_duplicate_tests():
    tests_duplicate = [
        ("worrld", "world"),
        ("helloo", "helo"),
        ("hiii", "hi")
    ]

    run_function_tests(tests_duplicate, replace_duplicate_letters)

def run_pi_tests():
    tests_pi = [
        ("pie", "pie"),
        ("pi", "3.14"),
        ("api", "api")
    ]

    run_function_tests(tests_pi, replace_pi)

def run_autocorrect_tests():
    tests_autocorrect = [
        ("I donn’t knoow pii value, so I will go eat my ppiie…", "I don’t know 3.14 value, so I wil go eat my pie…")
    ]

    run_function_tests(tests_autocorrect, replace_pi_and_duplicate)

def run_tests():
    run_duplicate_tests()
    run_pi_tests()
    run_autocorrect_tests()

if __name__ == "__main__":
    run_tests()
