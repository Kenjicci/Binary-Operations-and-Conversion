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
    
    # Convert integer part to octal
    integer_octal = oct(int(integer_part, 2))[2:]
    
    # Convert fractional part to octal
    fractional_octal = ''
    if fractional_part:
        fractional_octal += '.'  # Start fractional part
        fraction = float('0.' + fractional_part)
        for _ in range(precision):
            fraction *= 8
            integer_part = int(fraction)
            fractional_octal += str(integer_part)
            fraction -= integer_part

    return integer_octal + fractional_octal

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
test = input("Enter Binary number:  ")
x = BintoX(test)
print(f'Decimal: {x.convert_dec()}')
print(f'Octal: {x.convert_octal()}')
print(f'Hexadecimal: {x.convert_hexa()}')


# bin_to_x()

class XtoBin:
  def __init__(self, given_bin):
    self.given_bin = given_bin

  def dec_bin(self):
      dtb_int,_, dtb_flt = str(self.given_bin).partition(".")

    #convert the int to bin
      
      # dtb_conv = sum(int(digit)* (2**(i + 1)) for i, digit in enumerate(dtb_int)[2:])
      dtb_conv = bin(int(dtb_int))
    #convert the fractional part
      fractional_lst = []
      if dtb_flt:
        dtb_frac = float(f'0.{dtb_flt}')
        fractional_lst = []
        while dtb_frac !=0:
          dtb_frac = dtb_frac*2
          if dtb_frac >= 1:
            fractional_lst.append('1')
            dtb_frac = dtb_frac - 1
          else:
            fractional_lst.append('0')
          if len(fractional_lst)>20:
            break
        
        frac_final = ("".join(fractional_lst))
#combine decimal and fractional result
        final_result = str(dtb_conv) + '.' + frac_final
#return final result
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
    htb_int, _, htb_frac = str(self.given_bin).partition(".")    
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
      
def deci_to_x():
  test = input("Enter Decimal number:  ")
  x = XtoBin(test)
  decbin = x.dec_bin()
  y = BintoX(decbin)
  print(f'Decimal: {x.dec_bin()}')
  print(f'{y.convert_octal()}')
  print(f'{y.convert_hexa()}')

deci_to_x()