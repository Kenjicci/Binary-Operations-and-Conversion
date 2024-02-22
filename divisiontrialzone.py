def divide_binary(dividend, divisor):
    # Convert binary strings to integers
    dividend_int = int(dividend, 2)
    divisor_int = int(divisor, 2)

    # Initialize quotient and remainder as integers
    quotient_int = 0
    remainder_int = 0

    # Perform binary division
    for i in range(len(dividend)):
        # Left shift remainder and add next bit from dividend
        remainder_int = (remainder_int << 1) + int(dividend[i])

        # If the remainder is greater than or equal to the divisor, subtract the divisor
        if remainder_int >= divisor_int:
            remainder_int -= divisor_int
            # Set the current bit in the quotient to 1
            quotient_int = (quotient_int << 1) | 1
        else:
            # Set the current bit in the quotient to 0
            quotient_int <<= 1

    # Convert the quotient and remainder back to binary strings
    quotient = bin(quotient_int)[2:]
    remainder = bin(remainder_int)[2:]

    return quotient, remainder

# Example usage
dividend = "101101"
divisor = "11"
quotient, remainder = divide_binary(dividend, divisor)
print("Quotient:", quotient)
print("Remainder:", remainder)
