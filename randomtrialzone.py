def add_sign_extension(binary_number):
    # Determine the sign extension based on the most significant bit
    sign_extension = "1" if binary_number[0] == "1" else "0"
    
    # Remove spaces from the binary number
    binary_number = binary_number.replace(" ", "")

    # Separate the whole number part and the decimal part
    parts = binary_number.split('.')
    whole_number = parts[0]
    decimal_part = parts[1] if len(parts) > 1 else ""

    # Group the whole number part into sets of four bits from right to left
    groups = []
    current_group = ""
    for bit in whole_number[::-1]:
        current_group = bit + current_group
        if len(current_group) == 4:
            groups.insert(0, current_group)
            current_group = ""
    
    # Add the last group
    if current_group:
        if len(current_group) < 4:
            current_group = sign_extension * (4 - len(current_group)) + current_group
        groups.insert(0, current_group)
    
    # Add an additional 4 bits of sign extension if the first group is 4 bits
    if len(groups[0]) == 4:
        groups.insert(0, sign_extension * 4)

    # Reconstruct the whole number with the groups
    whole_number_with_groups = ' '.join(groups)

    # Reconstruct the binary number with the sign extension and the whole number with groups
    result = f"{whole_number_with_groups}"

    # Add the decimal part back if it exists
    if decimal_part:
        result += f".{decimal_part}"

    return result

# Example usage
binary_number = "1 1011 0000.01"  # Example binary number
result = add_sign_extension(binary_number)
print(result)
