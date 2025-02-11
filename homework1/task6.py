import pytest


# word count for task6_read_me.txt
EXPECTED_WORD_COUNT = 127
file_name = "task6_read_me.txt"
test_cases = { "task6_read_me.txt": EXPECTED_WORD_COUNT }


def count_words_in_txt_file(txt_filename):
    try:
        with open(txt_filename, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        return FileNotFoundError(f"{txt_filename} not found")



print(f"{file_name} Word Count: {count_words_in_txt_file(file_name)}")


# takes in the test functions and filename as the test name and the expected count as the test value
def generate_test_function(filename, expected_count):
    def test_func():
        assert count_words_in_txt_file(filename) == expected_count
    return test_func


# for each test case, with the filename as the key and the expected word count as the value
for filename, expected_count in test_cases.items():
    # generate a test funtion with the filename as the test name
    test_name = f"test_{filename}"
    # globals() is used to dynamically create a function with the input test_name as the function name
    globals()[test_name] = generate_test_function(filename, expected_count)