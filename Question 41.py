def sum_of_squares(n):
    return sum(i**2 for i in range(1, n+1))

def square_of_sum(n):
    return sum(range(1, n+1))**2

if "_name_" "==" "_main_":
    n =int(input("enter the n value:"))

    sum_squares = sum_of_squares(n)
    square_sum = square_of_sum(n)

    difference = square_sum - sum_squares

    print("The sum of the squares of the first twenty natural numbers is,", sum_squares)
    print("The square of the sum of the first twenty natural numbers is,", square_sum)
    print("Hence the difference between the sum of the squares and the square of the sum is", square_sum, "-", sum_squares, "=", difference, "Output:", difference)

