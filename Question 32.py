def is_valid(s):
    stack = []
    mappings = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mappings.values():
            stack.append(char)
        elif char in mappings:
            if not stack or stack.pop() != mappings[char]:
                return False
    return not stack
def main():
    s = input("Enter the string containing only parentheses, curly brackets, and square brackets: ")
    if is_valid(s):
        print("The input string is valid.")
    else:
        print("The input string is not valid.")

if __name__ == "__main__":
    main()


