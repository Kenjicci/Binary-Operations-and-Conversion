def count_decimal_places(num):
  return len(num.split(".")[-1]) if "." in num else 0

def add_sign_extension(binary_number):
    sign_extension = "1" if binary_number[0] == "1" else "0"
    binary_number = binary_number.replace(" ", "")
    parts = binary_number.split('.')
    whole_number = parts[0]
    decimal_part = parts[1] if len(parts) > 1 else ""
    groups = []
    current_group = ""
    for bit in whole_number[::-1]:
        current_group = bit + current_group
        if len(current_group) == 4:
            groups.insert(0, current_group)
            current_group = ""
    if current_group:
        if len(current_group) < 4:
            current_group = sign_extension * (4 - len(current_group)) + current_group
        groups.insert(0, current_group)
    if len(groups[0]) == 4:
        groups.insert(0, sign_extension * 4)
    whole_number_with_groups = ' '.join(groups)
    result = f"{whole_number_with_groups}"
    if decimal_part:
        result += f".{decimal_part}"
    return result

def modify_input(dividend, divisor):
    def count_decimal_places(num):
        if "." in num:
            return len(num.split(".")[1])
        return 0

    def pad_decimal_places(num, target_deci_places):
        if "." in num:
            int_part, dec_part = num.split(".")
            return int_part + dec_part.ljust(target_deci_places, "0")
        else:
            return num + "0" * target_deci_places

    deci_places = max(count_decimal_places(dividend), count_decimal_places(divisor))
    dividend = pad_decimal_places(dividend, deci_places)
    divisor = pad_decimal_places(divisor, deci_places)

    return dividend, divisor


def perform_binary_division():
    dividend = input("Dividend: ").replace(" ", "")
    divisor = input("Divisor: ").replace(" ", "")
    deci_places = max(count_decimal_places(dividend), count_decimal_places(divisor))
    modified_dividend, modified_divisor = modify_input(dividend, divisor)

    if dividend[0] == '1' and divisor[0] == '1':
        twos_dividend = Two_complement(modified_dividend).switch()
        twos_divisor = Two_complement(modified_divisor).switch()
        quotient = Division(twos_dividend, twos_divisor).divide_binary()
        positive_quotient = "0" + quotient.rstrip("0")
        print(add_sign_extension(positive_quotient))

    elif dividend[0] == '1' and divisor[0] == '0':
        twos_dividend = Two_complement(modified_dividend).switch()
        quotient = Division(twos_dividend, modified_divisor).divide_binary()
        twos_quotient = Two_complement(quotient).switch()
        negative_quotient = "1" + twos_quotient.rstrip("0")
        print(add_sign_extension(negative_quotient))

    elif dividend[0] == '0' and divisor[0] == '1':
        twos_divisor = Two_complement(modified_divisor).switch()
        quotient = Division(modified_dividend, twos_divisor).divide_binary()
        twos_quotient = Two_complement(quotient).switch()
        negative_quotient = "1" + twos_quotient.rstrip("0")
        print(add_sign_extension(negative_quotient))
    else:
        quotient = Division(modified_dividend, modified_divisor).divide_binary()
        positive_quotient = "0" + quotient.rstrip("0")
        print(add_sign_extension(positive_quotient))


def perform_binary_multiplication():
    multiplicand = input("Multiplicand: ").replace(" ", '')
    multiplier = input("Multiplier: ").replace(" ", '')

    removed_dec_multiplicand = multiplicand.replace(".", "")
    removed_dec_multiplier = multiplier.replace(".", "")

    deci_places = count_decimal_places(multiplicand) + count_decimal_places(multiplier)
    char = "."

    if char in multiplicand and char in multiplier:
        if multiplicand[0] == "0" and multiplier[0] == "1":
           new_multiplier = Two_complement(removed_dec_multiplier).switch()
           x = Multiplication(removed_dec_multiplicand, new_multiplier).multiply_binary()
           y = Two_complement(x).switch()
           z = y[:-deci_places] + "." + y[-deci_places:]
           print(add_sign_extension(z))

        elif multiplicand[0] == "1" and multiplier[0] == "0":
           new_multiplicand = Two_complement(removed_dec_multiplicand).switch()
           x = Multiplication(new_multiplicand, removed_dec_multiplier).multiply_binary()
           y = Two_complement(x).switch()
           z = y[:-deci_places] + "." + y[-deci_places:]
           print(add_sign_extension(z))

        elif multiplicand[0] == "1" and multiplier[0] == "1":
            x = Multiplication(removed_dec_multiplicand, removed_dec_multiplier).multiply_binary()
            z = x[:-deci_places] + "." + x[-deci_places:]
            print(add_sign_extension(z))
        else:
            x = Multiplication(removed_dec_multiplicand, removed_dec_multiplier).multiply_binary()
            z = x[:-deci_places] + "." + x[-deci_places:]
            print(add_sign_extension(z))

    elif char in multiplicand and char not in multiplier:
        if multiplicand[0] == "0" and multiplier[0] == "1":
           new_multiplier = Two_complement(multiplier).switch()
           x = Multiplication(removed_dec_multiplicand, new_multiplier).multiply_binary()
           y = Two_complement(x).switch()
           z = y[:-deci_places] + "." + y[-deci_places:]
           print(add_sign_extension(z))

        elif multiplicand[0] == "1" and multiplier[0] == "0":
           new_multiplicand = Two_complement(removed_dec_multiplicand).switch()
           x = Multiplication(new_multiplicand, multiplier).multiply_binary()
           y = Two_complement(x).switch()
           z = y[:-deci_places] + "." + y[-deci_places:]
           print(add_sign_extension(z))

        elif multiplicand[0] == "1" and multiplier[0] == "1":
            twos_multiplicand = Two_complement(removed_dec_multiplicand).switch()
            twos_multiplier = Two_complement(multiplier).switch()
            x = Multiplication(twos_multiplicand, twos_multiplier).multiply_binary()
            z = x[:-deci_places] + "." + x[-deci_places:]
            print(add_sign_extension(z))

        else:
            x = Multiplication(removed_dec_multiplicand, multiplier).multiply_binary()
            z = x[:-deci_places] + "." + x[-deci_places:]
            print(add_sign_extension(z))


    elif char not in multiplicand and char in multiplier:
        if multiplicand[0] == "0" and multiplier[0] == "1":
           new_multiplier = Two_complement(removed_dec_multiplier).switch()
           x = Multiplication(multiplicand, new_multiplier).multiply_binary()
           y = Two_complement(x).switch()
           z = y[:-deci_places] + "." + y[-deci_places:]
           print(add_sign_extension(z))

        elif multiplicand[0] == "1" and multiplier[0] == "0":
           new_multiplicand = Two_complement(multiplicand).switch()
           x = Multiplication(new_multiplicand, removed_dec_multiplier).multiply_binary()
           y = Two_complement(x).switch()
           z = y[:-deci_places] + "." + y[-deci_places:]
           print(add_sign_extension(z))

        elif multiplicand[0] == "1" and multiplier[0] == "1":
           new_multiplicand = Two_complement(multiplicand).switch()
           new_multiplier = Two_complement(removed_dec_multiplier).switch()
           x = Multiplication(new_multiplicand, new_multiplier).multiply_binary()
           z = x[:-deci_places] + "." + x[-deci_places:]
           print(add_sign_extension(z))

        else:
            x = Multiplication(multiplicand, removed_dec_multiplier).multiply_binary()
            z = x[:-deci_places] + "." + x[-deci_places:]
            print(add_sign_extension(z))

    else:
        if multiplicand[0] == "0" and multiplier[0] == "1":
           new_multiplier = Two_complement(multiplier).switch()
           x = Multiplication(multiplicand, new_multiplier).multiply_binary()
           y = Two_complement(x).switch()
           print(add_sign_extension(y))

        elif multiplicand[0] == "1" and multiplier[0] == "0":
           new_multiplicand = Two_complement(multiplicand).switch()
           x = Multiplication(new_multiplicand, multiplier).multiply_binary()
           y = Two_complement(x).switch()
           print(add_sign_extension(y))

        elif multiplicand[0] == "1" and multiplier[0] == "1":
           new_multiplicand = Two_complement(multiplicand).switch()
           new_multiplier = Two_complement(multiplier).switch()
           x = Multiplication(new_multiplicand, new_multiplier).multiply_binary()
           print(add_sign_extension(x))

        else:
            x = Multiplication(multiplicand, multiplier).multiply_binary()
            print(add_sign_extension(x))

def perform_binary_subtraction():
    minuend = input("Minuend: ").replace(" ", "")
    subtrahend = input("Subtrahend: ").replace(" ", "")
    char = "."

    deci_places1 = count_decimal_places(minuend)
    deci_places2 = count_decimal_places(subtrahend)
    max_deci_length = max(deci_places1, deci_places2)

    minuend_padded = minuend + "0" * (max_deci_length - deci_places1)
    subtrahend_padded = subtrahend + "0" * (max_deci_length - deci_places2)

    minuend_rpadded_bin = minuend_padded.replace(char, "")
    subtrahend_rpadded_bin = subtrahend_padded.replace(char, "")

    max_len = max(len(minuend_rpadded_bin), len(subtrahend_rpadded_bin))
    minuend_lpadded_bin = minuend_rpadded_bin.zfill(max_len)
    subtrahend_lpadded_bin = subtrahend_rpadded_bin.zfill(max_len)

    if minuend == subtrahend:
        dif = "0"
        print(add_sign_extension(dif))

    if char not in minuend and char not in subtrahend:
        if minuend[0] == '0' and subtrahend[0] == '0':
            result = Subtraction.binary_subtraction(minuend, subtrahend)
            new_difference = result.zfill(len(result) + 1)
            print(add_sign_extension(new_difference))

        elif minuend[0] == '1' and subtrahend[0] == '1':
            twos_subtra = Two_complement(subtrahend).switch()
            new_dif = Addition.binary_addition(minuend, twos_subtra)
            print(add_sign_extension(new_dif))

        elif minuend[0] == '1' and subtrahend[0] == "0":
            twos_subtra = Two_complement(subtrahend).switch()
            dif = Addition.binary_addition(minuend, twos_subtra)
            print(add_sign_extension(dif))
        else:
            dif = Subtraction.binary_subtraction(minuend, subtrahend)
            print(add_sign_extension(dif))

    elif char in minuend or char in subtrahend:
        if minuend[0] == "0" and subtrahend[0] == "0":
            result = Subtraction.binary_subtraction(minuend_lpadded_bin, subtrahend_lpadded_bin)
            final_answer = result[:-max_deci_length] + "." + result[-max_deci_length:]
            new_final = final_answer.zfill(len(final_answer) + 1)
            print(add_sign_extension(new_final))

        elif minuend[0] == '1' and subtrahend[0] == '1':
            twos_subtra = Two_complement(subtrahend_lpadded_bin).switch()
            result = Addition.binary_addition(minuend_lpadded_bin, twos_subtra)
            final_answer = result[:-max_deci_length] + "." + result[-max_deci_length:]
            print(add_sign_extension(final_answer))

        elif minuend[0] == '1' and subtrahend[0] == "0":
            twos_subtra = Two_complement(subtrahend_lpadded_bin).switch()
            dif = Addition.binary_addition(minuend_lpadded_bin, twos_subtra)
            final_answer = dif[:-max_deci_length] + "." + dif[-max_deci_length:]
            print(add_sign_extension(final_answer))

        else:
            dif = Addition.binary_addition(minuend_lpadded_bin, subtrahend_lpadded_bin)
            final_answer = dif[:-max_deci_length] + "." + dif[-max_deci_length:]
            y = final_answer.replace("1", "0", 1)
            new_y = y.zfill(len(y) + 1)
            print(add_sign_extension(new_y))    

def perform_binary_addition():
  a = input("Addend 1: ").replace(" ", "")
  b = input("Addend 2: ").replace(" ", "")
  char = "."

  deci_places1 = count_decimal_places(a)
  deci_places2 = count_decimal_places(b)
  max_deci_length = max(deci_places1, deci_places2)

  a_padded = a + "0" * (max_deci_length - deci_places1)
  b_padded = b + "0" * (max_deci_length - deci_places2)

  a_rpadded_bin = a_padded.replace(char, "")
  b_rpadded_bin = b_padded.replace(char, "")

  max_len = max(len(a_rpadded_bin), len(b_rpadded_bin))
  a_lpadded_bin = a_rpadded_bin.zfill(max_len)
  b_lpadded_bin = b_rpadded_bin.zfill(max_len)

  if char not in a and char not in b:
    x = Addition.binary_addition(a, b)
    if a[0] == '1' and b[0] == '1':
      print(add_sign_extension(x))
    elif a[0] == '0' and b[0] == '0':
      new_x = x.zfill(len(x) + 1)
      print(add_sign_extension(new_x))
    elif a[0] == '1' and b[0] == '0':
      if int(a, 2) > int(b, 2):
        print(add_sign_extension(x))
      else:
        new_x = x.zfill(len(x) + 1)
        print(add_sign_extension(new_x))
    elif a[0] == '0' and b[0] == '1':
      if int(a, 2) > int(b, 2):
        new_x = x.zfill(len(x) + 1)
        print(add_sign_extension(new_x))
      else:
        print(add_sign_extension(x))
  elif char in a or char in b:
    y = Addition.binary_addition(a_lpadded_bin, b_lpadded_bin)
    final_answer = y[:-max_deci_length] + '.' + y[-max_deci_length:]
    if a[0] == '1' and b[0] == '1':
      print(add_sign_extension(final_answer))
    elif a[0] == '0' and b[0] == '0':
      new_final = final_answer.zfill(len(final_answer) + 1)
      print(add_sign_extension(new_final))
    elif a[0] == '1' and b[0] == '0':
      new_a = BintoX(a)
      new_b = BintoX(b)
      if new_a.convert_dec() > new_b.convert_dec():
        print(add_sign_extension(final_answer))
      else:
        y = final_answer.replace("1", "0", 1)
        new_y = y.zfill(len(y) + 1)
        print(add_sign_extension(new_y))
    elif a[0] == '0' and b[0] == '1':
      new_a = BintoX(a)
      new_b = BintoX(b)
      if new_a.convert_dec() > new_b.convert_dec():
        y = final_answer.replace("1", "0", 1)
        new_y = y.zfill(len(y) + 1)
        print(add_sign_extension(new_y))
      else:
        print(add_sign_extension(final_answer))

#CLASSES
class One_complement:
  def __init__(self, given_bin):
    self.given_bin = given_bin

  def switch(self):
    binlst = str(self.given_bin)
    rev_lst = [str(1 - int(i)) for i in binlst]
    return "".join(rev_lst)
    binlst,_, binflt = str(self.given_bin).partition(".")
    rev_bin = [str(1 - int(i)) for i in binlst]
    rev_frac = [str(1 - int(i)) for i in binflt]
    binint=("".join(rev_bin))
    binflt=("".join(rev_frac))
    return f'{binint}.{binflt}'

class Two_complement:
  def __init__(self, given_bin2):
    self.given_bin2 = given_bin2

  def switch(self):
    binlst = self.given_bin2
    if '.' not in binlst:
      inverted_bin = One_complement(binlst).switch()
      a = len(inverted_bin)
      padded_one = '0' * (a - 1) + '1'      
      result = Addition.binary_addition(inverted_bin, padded_one)
      return result
    elif "." in binlst:  
      deci_places = count_decimal_places(binlst)
      whole_bin = binlst.replace(".", "")
      inverted_bin = One_complement(whole_bin).switch()
      a = len(whole_bin)
      padded_one = '0' * (a - 1) + '1'    
      result = Addition.binary_addition(inverted_bin, padded_one)
      result_with_dec = result[:-deci_places] + "." + result[-deci_places:]
      return result_with_dec

class Addition:
  @staticmethod
  def binary_addition(a_lpadded_bin, b_lpadded_bin):
    max_len = max(len(a_lpadded_bin), len(b_lpadded_bin))
    result = ''
    carry = 0

    for i in range(max_len - 1, -1, -1):
      r = carry
      r += int(a_lpadded_bin[i]) if i < len(a_lpadded_bin) else 0
      r += int(b_lpadded_bin[i]) if i < len(b_lpadded_bin) else 0
      result = ('1' if r % 2 == 1 else '0') + result
      carry = 0 if r < 2 else 1
    if carry != 0:
      result = '1' + result

    return result.zfill(max_len)

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

            # Para sa borrow
            minuend_bit -= borrow
            borrow = 0

            # Check if subtraction is possible
            if minuend_bit < subtrahend_bit:
                minuend_bit += 2  # Add 2 to for borrowing
                borrow = 1

            result.insert(0, str(minuend_bit - subtrahend_bit))

        return ''.join(result).lstrip('0') or '0'

class Multiplication:
    def __init__(self, multiplicand, multiplier):
        self.multiplicand = multiplicand
        self.multiplier = multiplier

    def multiply_binary(self):
        num1 = int(self.multiplicand, 2)
        num2 = int(self.multiplier, 2)
        result = 0
        leading_zeroes = self.count_leading_zeroes(self.multiplicand) + self.count_leading_zeroes(self.multiplier)
        while num2 > 0:
            if num2 & 1:
                result += num1
            num1 <<= 1
            num2 >>= 1
        result_str = bin(result)[2:]
        return '0' * leading_zeroes + result_str

    def count_leading_zeroes(self, binary_num):
        count = 0
        for bit in binary_num:
            if bit == '0':
                count += 1
            else:
                break
        return count
    

class Division:
    def __init__(self, dividend, divisor):
        self.dividend = dividend
        self.divisor = divisor

    def count_leading_zeroes(self, binary_str):
        return len(binary_str) - len(binary_str.lstrip('0'))

    def divide_binary(self):
        num1 = int(self.dividend.replace(".", ""), 2)
        num2 = int(self.divisor.replace(".", ""), 2)
        quotient = 0
        remainder = 0
        leading_zeroes = self.count_leading_zeroes(self.dividend) - self.count_leading_zeroes(self.divisor)
        

        while num1 >= num2:
            temp = num2
            multiple = 1
            while temp <= num1:
                temp <<= 1
                multiple <<= 1
            temp >>= 1
            multiple >>= 1
            num1 -= temp
            quotient += multiple
        
        remainder = num1
        quotient_str = bin(quotient)[2:]
        

        decimal_str = ""
        for _ in range(8): 
            num1 <<= 1
            if num1 >= num2:
                num1 -= num2
                decimal_str += "1"
            else:
                decimal_str += "0"
        
        return '0' * leading_zeroes + quotient_str + "." + decimal_str
  
class BintoX:
  def __init__(self,giv_bin):
    self.giv_bin = giv_bin

  def convert_dec(self):

    integer_part, _, fractional_part = str(self.giv_bin).partition('.')
    
    # Convert integer part to decimal
    integer_dec = int(integer_part, 2)
    
    # Convert fractional part to decimal
    fractional_dec = 0
    if fractional_part:
        fraction = float('0.' + fractional_part)
        for i, digit in enumerate(fractional_part, 1):
            fractional_dec += int(digit) * (2 ** (-i))
    
    # Return the sum of integer and fractional parts
    return integer_dec + fractional_dec

  def convert_octal(self, precision=6):
    integer_part, _, fractional_part = str(self.giv_bin).partition('.')
    
    # Convert integer part to decimal
    integer_decimal = int(integer_part, 2)
    integer_octal = oct(integer_decimal)[2:]
    
    # Convert fractional part to decimal
    fractional_octal = ''
    if fractional_part:
        fractional_octal += '.'  # Start fractional part
        fraction = sum(int(digit) / (2 ** i) for i, digit in enumerate(fractional_part, start=1))
        for _ in range(precision):
            fraction *= 8
            integer_part = int(fraction)
            fractional_octal += str(integer_part)
            fraction -= integer_part

    return integer_octal + fractional_octal



  def convert_hexa(self):

    bth_lst = '0' * (4 - (len(str(self.giv_bin)))% 4) + str(self.giv_bin)
#initializing hex value
    hex_sum = ""

    for i in range(len(bth_lst), 0, -4):

      grp_lst = bth_lst[max(0, i-4):i]
      # hex_val = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
      hex_lst = sum(int(num) * ( 2**(i%4)) for i, num in enumerate(grp_lst[::-1]))
      # hexa conditions
      if hex_lst == 10:
        hex_lst = 'A'
      elif hex_lst ==11:
        hex_lst = 'B'
      elif hex_lst ==12:
        hex_lst = 'C'
      elif hex_lst ==13:
        hex_lst = 'D'
      elif hex_lst ==14:
        hex_lst = 'E'
      elif hex_lst ==15:
        hex_lst = 'F'

      hex_sum = str(hex_lst) + hex_sum
    #return value
    return hex_sum
    """    
    test = input("Enter Binary number:  ")
    # test = 10100
    x = BintoX(test)
    print(x.convert_dec())
    print(x.convert_octal())
    print(x.convert_hexa())
    """

  def convert_hexa(self, precision=6):
    integer_part, _, fractional_part = str(self.giv_bin).partition('.')
    
    # Convert integer part to hexadecimal
    integer_hex = hex(int(integer_part, 2))[2:]
    integer_decimal = int(integer_part, 2)
    
    # Convert fractional part to hexadecimal
    fractional_hex = ''
    if fractional_part:
        fractional_hex += '.'  # Start fractional part
        fraction = sum(int(digit) / (2 ** i) for i, digit in enumerate(fractional_part, start=1))
        for _ in range(precision):
            fraction *= 16
            integer_part = int(fraction)
            fractional_hex += hex(integer_part)[2:]
            fraction -= integer_part

    return integer_hex + fractional_hex
  

# def bin_to_x():
# test = input("Enter Binary number:  ")
# x = BintoX(test)
# print(f'Decimal: {x.convert_dec()}')3
# print(f'Octal: {x.convert_octal()}')
# print(f'Hexadecimal: {x.convert_hexa()}')
  
class XtoBin:
  def __init__(self, given_bin):
    self.given_bin = given_bin

  def convert_hexa(self, precision=6):
    integer_part, _, fractional_part = str(self.giv_bin).partition('.')
    
    # Convert integer part to hexadecimal
    integer_hex = hex(int(integer_part, 2))[2:]
    
    # Convert fractional part to hexadecimal
    fractional_hex = ''
    if fractional_part:
        fractional_hex += '.'  # Start fractional part
        fraction = float('0.' + fractional_part)
        for _ in range(precision):
            fraction *= 16
            integer_part = int(fraction)
            fractional_hex += hex(integer_part)[2:]
            fraction -= integer_part

    return integer_hex + fractional_hex

# def bin_to_x():
#test = input("Enter Binary number:  ")
# x = BintoX(test)
# print(f'Decimal: {x.convert_dec()}')
# print(f'Octal: {x.convert_octal()}')
# print(f'Hexadecimal: {x.convert_hexa()}')


# bin_to_x()

class XtoBin:
  def __init__(self, given_bin):
    self.given_bin = given_bin

  def dec_bin(self):
    dtb_int, _, dtb_flt = str(self.given_bin).partition(".")

    # Convert the integer part to binary
    dtb_conv = bin(int(dtb_int))[2:]

    # Convert the fractional part
    fractional_lst = []
    if dtb_flt:
        dtb_frac = float('0.' + dtb_flt)
        while dtb_frac != 0:
            dtb_frac = dtb_frac * 2
            if dtb_frac >= 1:
                fractional_lst.append('1')
                dtb_frac = dtb_frac - 1
            else:
                fractional_lst.append('0')
            if len(fractional_lst) > 20:
                break
        
    frac_final = ("".join(fractional_lst))
    # Combine decimal and fractional result
    final_result = dtb_conv + '.' + frac_final

    # Return final result
    return final_result
      
  def oct_bin(self):
    otb_int, _, otb_frac = str(self.given_bin).partition(".")    
    otb_lst = []
    otb_fracfin = []
#octal map
    otb_map = {
        '0': "000",
        '1': "001",
        '2': "010",
        '3': "011",
        '4': "100",
        '5': "101",
        '6': "110",
        '7': "111"
    }
#iterate and covert the integer value
    for i in otb_int:
      otb_lst.append(otb_map[i])
#iterate and covert the fractional value
    for i in otb_frac:
      otb_fracfin.append(otb_map[i])

#initializing octal value

    oct_final =  ("".join(otb_lst)) + '.' + (''.join(otb_fracfin))
    
#return octal value
    return oct_final


  def hex_bin(self):
    htb_int, _, htb_frac = str(self.given_bin).upper().partition(".") 
    htb_lst = []
    htb_fracfin = []
#hex map
    htb_map = {
        '0': "0000",
        '1': "0001",
        '2': "0010",
        '3': "0011",
        '4': "0100",
        '5': "0101",
        '6': "0110",
        '7': "0111",
        '8': "1000",
        '9': "1001",
        'A': "1010",
        'B': "1011",
        'C': "1100",
        'D': "1101",
        'E': "1110",
        'F': "1111",
    }
#iterate and covert the integer value
    for i in htb_int:
      htb_lst.append(htb_map[i])
#iterate and covert the fractional value
    for i in htb_frac:
      htb_fracfin.append(htb_map[i])

#initializing hex value

    hex_final =  ("".join(htb_lst)) + '.' + (''.join(htb_fracfin))
    
#return hex value
    return hex_final

#menu 3 processes
def bin_to_x():
  test = input("Enter Binary number:  ")
  x = BintoX(test)
  print(f'Decimal: {x.convert_dec()}')
  print(f'Octal: {x.convert_octal()}')
  print(f'Hexadecimal: {x.convert_hexa()}')

def deci_to_x():
  test = input("Enter Decimal number:  ")
  x = XtoBin(test)
  decbin = x.dec_bin()
  y = BintoX(decbin)
  print(f'Binary : {x.dec_bin()}')
  print(f'Octal: {y.convert_octal()}')
  print(f'Hexadecimal: {y.convert_hexa()}')

def oct_to_x():
  test = input("Enter Octal number:  ")
  x = XtoBin(test)
  octbin = x.oct_bin()
  y = BintoX(octbin)
  print(f'Binary: {x.oct_bin()}')
  print(f'Decimal: {y.convert_dec()}')
  print(f'Hexadecimal: {y.convert_hexa()}')

def hex_to_x():
  test = input("Enter Hexadecimal number:  ")
  x = XtoBin(test)
  octbin = x.hex_bin()
  y = BintoX(octbin)
  print(f'Binary: {x.hex_bin()}')
  print(f'Decimal: {y.convert_dec()}')
  print(f'Octal: {y.convert_octal()}')


def menu1():
  print("Menu - (Main Menu)")
  menu_choice = input(f"\n[1] Binary Operations \n[2] Number System Conversion \n[3] Exit \n")

  if menu_choice == "1":
    menu2()
  elif menu_choice == "2":
    menu3()
  else:
    exit()



def menu2():
  print("Menu - 1 (Binary Operations)")
  menu2_choice = input(f"\n[1] Division \n[2] Multiplication \n[3] Subtraction \n[4] Addition \n[5] Negative (2's Complement) \n")
  if menu2_choice == "1":
    perform_binary_division()
  elif menu2_choice == "2":
    perform_binary_multiplication()
  elif menu2_choice == "3":
    perform_binary_subtraction()
  elif menu2_choice == "4":
    perform_binary_addition()
  elif menu2_choice == "5":
    binlst = input("Binary to Two's Complement: ").replace(" ", "")
    twoscomp = Two_complement(binlst).switch()
    print(twoscomp)
  else:
    print("Invalid Option")


def menu3():
  print("Menu - 2 (Conversion)")
  menu3_choice = input(f"\n[1] Binary to X \n[2] Decimal to X \n[3] Octal to X\n[4] Hexa to X \n")

  if menu3_choice == '1':
    print("this is the binary conversion to x")
    bin_to_x()
  elif menu3_choice == '2':
    print('this is the decimal conversion to x')
    deci_to_x()
  elif menu3_choice == '3':
    print('this is the octal conversion to x')
    oct_to_x()
  elif menu3_choice == '4':
    print('this is the hexa conversion to x')
    hex_to_x()


#CALLING
menu1()

