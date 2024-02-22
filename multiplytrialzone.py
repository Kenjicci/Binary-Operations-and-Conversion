#count the number of decimal
#check is the multiplier is negative
#Use two's complement if negative
#every bits of multipier be multiplied to the bits of multiplicand
def count_decimal_places(num):
    return len(num.split(".")[-1]) if "." in num else 0
def multiply_binary(bin1, bin2):
    # Convert binary strings to lists for easier manipulation
    multiplicand = list(bin1)
    multiplier = list(bin2)

    # Reverse both lists for easier handling of rightmost digits
    multiplicand.reverse()
    multiplier.reverse()

    # Initialize the result list with zeros
    result = [0] * (len(multiplicand) + len(multiplier))

    # Multiply each digit of the multiplicand by the multiplier
    for i in range(len(multiplicand)):
        for j in range(len(multiplier)):
            result[i + j] += int(multiplicand[i]) * int(multiplier[j])
            result[i + j + 1] += result[i + j] // 2
            result[i + j] %= 2

    # Convert the result list back to a string
    result.reverse()
    return ''.join(str(x) for x in result).lstrip('0') or '0'

# Example usage
binary1 = input("Multiplicand: ").replace(" ", '')
binary2 = input("Multiplier: ").replace(" ", '')
result = multiply_binary(binary1, binary2)
print(f'{binary1} x {binary2} = {result}')

