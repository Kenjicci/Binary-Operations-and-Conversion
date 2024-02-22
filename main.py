class One_complement:
  def __init__(self, given_bin):
    self.given_bin = given_bin

  def switch(self):
    binlst = str(self.given_bin)
    rev_lst = [str(1 - int(i)) for i in binlst]
    return "".join(rev_lst)
  """
  test = input("Enter Binary number: ")
  # test = 11001011
  x = One_complement(test)
  x.switch()
  """

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
      print(result)
    elif "." in binlst:
      deci_places = count_decimal_places(binlst)
      whole_bin = binlst.replace(".", "")
      inverted_bin = One_complement(whole_bin).switch()
      a = len(whole_bin)  
      padded_one = '0' * (a - 1) + '1'  
      result = Addition.binary_addition(inverted_bin, padded_one)
      result_with_dec = result[:-deci_places] + "." + result[-deci_places:]
      print(result_with_dec)


def count_decimal_places(num):
  return len(num.split(".")[-1]) if "." in num else 0

class Addition:
  @staticmethod
  def binary_addition(a_lpadded_bin, b_lpadded_bin):
    max_len = max(len(a_lpadded_bin), len(b_lpadded_bin))
    result = ''
    carry = 0

    for i in range(max_len - 1, -1, -1):
      r = carry
      r += 1 if a_lpadded_bin[i] == '1' else 0
      r += 1 if b_lpadded_bin[i] == '1' else 0
      result = ('1' if r % 2 == 1 else '0') + result
      carry = 0 if r < 2 else 1

    if carry != 0:
      result = '1' + result

    return result.zfill(max_len)

class Subtract:
  def __init__(self, minuend, subtrahend):
    self.minuend = minuend
    self.subtrahend = subtrahend

  def display_difference(self):
    pass

class Multiplication:
  def __init__(self, multiplicand, multiplier):
    self.multiplicand = multiplicand
    self.multplier = multiplier

  def product(self):
    pass

class Division:
  def __init__(self, dividend, divisor):
    self.dividend = dividend
    self.divisor = divisor

  def quotient(self):
    pass
  
class BintoX:
  def __init__(self,giv_bin):
    self.giv_bin = giv_bin

  def convert_dec(self):
    btd_lst = str(self.giv_bin)[::-1]
#multiplying the bits by 2 raise to index
    deci_lst = [(2**index)* int(btd_lst[index]) for index in range(len(btd_lst))]
    decimal = sum(deci_lst)

    return decimal

  def convert_octal(self):

    # octal = oct(self.giv_bin)

    bto_lst = '0' * (3 - (len(str(self.giv_bin)))% 3) + str(self.giv_bin)
#initializing octal value
    oct_sum = ''

    for i in range(len(bto_lst), 0, -3):
#slicing the list
      grp_lst = bto_lst[max(0, i-3):i]
#enumeration of bits by 3's
      octal = sum(int(bit) * (2 ** (i % 3)) for i, bit in enumerate(grp_lst[::-1]))

      oct_sum =  str(octal) + oct_sum
    
#return octal value
    return oct_sum

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


def menu1():
  print("Menu - 1 (Main Menu)")
  menu_choice = input(f"\n[1] Binary Operations \n[2] Number System Conversion \n[3] Exit \n")

  if menu_choice == "1":
    menu2()
  elif menu_choice == "2":
    menu3()
  else:
    exit()




def menu2():
  print("Menu - 2 (Binary Operations)")
  menu2_choice = input(f"\n[1] Division \n[2] Multiplication \n[3] Subtraction \n[4] Addition \n[5] Negative (2's Complement) \n")
  if menu2_choice == "1":
    pass
  elif menu2_choice == "2":
    pass
  elif menu2_choice == "3":
    pass
  elif menu2_choice == "4":

    a = input("Addendx: ").replace(" ", "")
    b = input("Addendy: ").replace(" ", "")

    char = "."

    # bilang ng number of decimals
    deci_places1 = count_decimal_places(a)
    deci_places2 = count_decimal_places(b)
    max_deci_length = max(deci_places1, deci_places2)

    # Pad numbers with trailing zeroes
    a_padded = a + "0" * (max_deci_length - deci_places1)
    b_padded = b + "0" * (max_deci_length - deci_places2)

    #removing decimal points
    a_rpadded_bin = a_padded.replace(char, "")
    b_rpadded_bin = b_padded.replace(char, "")

    #padding left side 
    max_len = max(len(a_rpadded_bin), len(b_rpadded_bin))
    a_lpadded_bin = a_rpadded_bin.zfill(max_len)
    b_lpadded_bin = b_rpadded_bin.zfill(max_len)

    #add the decimal point
    if char not in a and char not in b:
        x = Addition.binary_addition(a,b)
        print(x)
    elif char in a or char in b:
        y = Addition.binary_addition(a_lpadded_bin, b_lpadded_bin)
        final_answer= y[:-max_deci_length]+'.'+ y[-max_deci_length:]
        print(final_answer)

  elif menu2_choice == "5":
    binlst = input("Binary to Two's Complement: ").replace(" ", "")
    twoscomp = Two_complement(binlst).switch()
    print(twoscomp)
  else:
    print("Invalid Option")



def menu3():
  print("Menu - 3 (Conversion)")
  menu3_choice = input(f"\n[1] Binary to X \n[2] Decimal to X \n[3] Octal to X\n[4] Hexa to X \n")

  if menu3_choice == '1':
    print("this is the binary conversion to x")
  elif menu3_choice == '2':
    print('this is the decimal conversion to x')
  elif menu3_choice == '3':
    print('this is the octal conversion to x')
  elif menu3_choice == '4':
    print('this is the hexa conversion to x')


#CALLING
menu1()
