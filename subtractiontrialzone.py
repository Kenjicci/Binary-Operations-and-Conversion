def count_decimal_places(num):
    return len(num.split(".")[-1]) if "." in num else 0

def padding(a, b):
    max_len = max(len(a), len(b))
    a_padded = a.zfill(max_len)
    b_padded = b.zfill(max_len)
    return a_padded, b_padded

class Subtraction:
    @staticmethod
    def binary_subtraction(minuend, subtrahend):
        result = []
        borrow = 0
        for i in range(len(minuend) - 1, -1, -1):
            if minuend[i] == ".":
                result.insert(0, ".")
                continue

            minuend_bit = int(minuend[i])
            subtrahend_bit = int(subtrahend[i])

            # Apply borrowing if necessary
            minuend_bit -= borrow
            borrow = 0

            # Check if subtraction is possible
            if minuend_bit < subtrahend_bit:
                minuend_bit += 2  # Add 2 to handle borrowing
                borrow = 1

            result.insert(0, str(minuend_bit - subtrahend_bit))

        return ''.join(result).lstrip('0') or '0'

# Input
minuend = input("Minuend: ").replace(" ", "")
subtrahend = input("Subtrahend: ").replace(" ", "")

char = "."
deci_places1 = count_decimal_places(minuend)
deci_places2 = count_decimal_places(subtrahend)
max_deci_length = max(deci_places1, deci_places2)

if char not in minuend and char not in subtrahend:
    result = Subtraction.binary_subtraction(minuend, subtrahend)
    print(result)
elif char in minuend or char in subtrahend:
    minuend_padded, subtrahend_padded = padding(minuend, subtrahend)
    result = Subtraction.binary_subtraction(minuend_padded, subtrahend_padded)
    #final_answer = result[:-max_deci_length] + '.' + result[-max_deci_length:]
    print(f"{minuend_padded} - {subtrahend_padded} = {result}")
