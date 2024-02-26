def addBinary(a: str, b: str) -> str:
    result = []
    carry = 0
    i, j = len(a) - 1, len(b) - 1

    while i >= 0 or j >= 0 or carry:

        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0

        sum_bits = digit_a + digit_b + carry

        carry = sum_bits // 2
        result.append(str(sum_bits % 2))

        i -= 1
        j -= 1

    return ''.join(result[::-1])

a = input("enter the value of a:")
b = input("enter the value of b:")
print(addBinary(a, b))
