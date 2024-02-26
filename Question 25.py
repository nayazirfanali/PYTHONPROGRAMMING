def create_tuple_list(lower, upper):
    tuple_list = [(num, num ** 2) for num in range(lower, upper + 1)]
    return tuple_list
def main():
    lower_range = int(input("Enter the lower range: "))
    upper_range = int(input("Enter the upper range: "))
    if lower_range > upper_range:
        print("Lower range cannot be greater than upper range.")
        return
    result = create_tuple_list(lower_range, upper_range)
    print("List of tuples with the first element as the number and the second element as the square:")
    print(result)
if __name__ == "__main__":
    main()


