import re

def is_valid_number(s):
    # Regular expression to match the pattern of a valid number
    pattern = r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$'
    return bool(re.match(pattern, s))

# Test cases
test_cases = ["0", "e", " ", ".", "%"]
results = [is_valid_number(s) for s in test_cases]

# Printing results
for i, tc in enumerate(test_cases):
    print(f"Input: s = \"{tc}\", Output: {results[i]}")
