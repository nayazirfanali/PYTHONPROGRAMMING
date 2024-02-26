def find_mth_max_and_nth_min(arr, m, n):
    sorted_arr = sorted(arr)
    mth_max = sorted_arr[-m]
    nth_min = sorted_arr[n - 1]
    return mth_max, nth_min

def main():
    arr = [int(x) for x in input("Enter the array elements separated by space: ").split()]
    m = int(input("Enter the value of M: "))
    n = int(input("Enter the value of N: "))

    mth_max, nth_min = find_mth_max_and_nth_min(arr, m, n)
    sum_of_numbers = mth_max + nth_min
    difference_of_numbers = mth_max - nth_min

    print(f"Mth maximum number: {mth_max}")
    print(f"Nth minimum number: {nth_min}")
    print(f"Sum of the numbers: {sum_of_numbers}")
    print(f"Difference of the numbers: {difference_of_numbers}")

if __name__ == "__main__":
    main()


