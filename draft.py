class One_complement:
  def __init__(self, given_bin):
    self.given_bin = given_bin

  def switch(self):
    binlst,_, binflt = str(self.given_bin).partition(".")
    rev_bin = [str(1 - int(i)) for i in binlst]
    rev_frac = [str(1 - int(i)) for i in binflt]
    binint=("".join(rev_bin))
    binflt=("".join(rev_frac))
    return f'{binint}.{binflt}'
  
class two_complement:
  def __init__ (self, given_bin):
    self.given_bin = given_bin

  def switch(self):
    whole,_, frac = str(self.given_bin).partition(".")

    twos_lst = []

    while len(frac) != 0:
      twos_lst = []
      for j in frac[::-1]:
        twos_lst.append(j)
        if j ==1:
          rev_frac = [str(1 - int(i)) for i in frac]
          rev_bin = [str(1 - int(i)) for i in whole[::-1]]
          break
          

      
    return twos_lst


# Test the conversion
test_decimal = 10110101.011
converter = two_complement(test_decimal)
binary_result = converter.switch()
print(binary_result)  # Output: 01001010.101
      

# test = input("Enter Binary number: ")
# # test = 11001011
# x = One_complement(test)
# print(x.switch())

# class BintoX:
#   def __init__(self,giv_bin):
#     self.giv_bin = giv_bin

#   def convert_dec(self):
#     btd_lst,_, btd_flt = str(self.giv_bin).partition(".")
# #multiplying the bits by 2 raise to index
#     deci_lst = [(2**index)* int(btd_lst[index]) for index in range(len(btd_lst[::-1]))]
#     decimal = sum(deci_lst)
# #converting the fractional part
#     deci_frac = [((2**(-(index+1)))) * int(btd_flt[index]) for index in range(len(btd_flt))]
#     frac = sum(deci_frac)
#     result = decimal+frac
#     return f'{result}'
  
# test = input("Enter Binary number:  ")
# # test = 10100
# x = BintoX(test)
# print(x.convert_dec())

# class XtoBin:
#   def __init__(self, given_bin):
#     self.given_bin = given_bin

#   def dec_bin(self):
#       dtb_int,_, dtb_flt = str(self.given_bin).partition(".")

#     #convert the int to bin
      
#       # dtb_conv = sum(int(digit)* (2**(i + 1)) for i, digit in enumerate(dtb_int)[2:])
#       dtb_conv = bin(int(dtb_int))[2:]
#     #convert the fractional part
#       fractional_lst = []
#       if dtb_flt:
#         dtb_frac = float(f'0.{dtb_flt}')
#         fractional_lst = []
#         while dtb_frac !=0:
#           dtb_frac = dtb_frac*2
#           if dtb_frac >= 1:
#             fractional_lst.append('1')
#             dtb_frac = dtb_frac - 1
#           else:
#             fractional_lst.append('0')
#           if len(fractional_lst)>20:
#             break
        
#         frac_final = ("".join(fractional_lst))
# #combine decimal and fractional result
#         final_result = str(dtb_conv) + '.' + frac_final
# #return final result
#         return final_result
#   def oct_bin(self):
#     otb_int, _, otb_frac = str(self.given_bin).partition(".")    
#     otb_lst = []
#     otb_fracfin = []
# #octal map
#     otb_map = {
#         '0': "000",
#         '1': "001",
#         '2': "010",
#         '3': "011",
#         '4': "100",
#         '5': "101",
#         '6': "110",
#         '7': "111"
#     }
# #iterate and covert the integer value
#     for i in otb_int:
#       otb_lst.append(otb_map[i])
# #iterate and covert the fractional value
#     for i in otb_frac:
#       otb_fracfin.append(otb_map[i])

# #initializing octal value

#     oct_final =  ("".join(otb_lst)) + '.' + (''.join(otb_fracfin))
    
# #return octal value
#     return oct_final


#   def hex_bin(self):
#     htb_int, _, htb_frac = str(self.given_bin).partition(".")    
#     htb_lst = []
#     htb_fracfin = []
# #hex map
#     htb_map = {
#         '0': "0000",
#         '1': "0001",
#         '2': "0010",
#         '3': "0011",
#         '4': "0100",
#         '5': "0101",
#         '6': "0110",
#         '7': "0111",
#         '8': "1000",
#         '9': "1001",
#         'A': "1010",
#         'B': "1011",
#         'C': "1100",
#         'D': "1101",
#         'E': "1110",
#         'F': "1111",
#     }
# #iterate and covert the integer value
#     for i in htb_int:
#       htb_lst.append(htb_map[i])
# #iterate and covert the fractional value
#     for i in htb_frac:
#       htb_fracfin.append(htb_map[i])

# #initializing hex value

#     hex_final =  ("".join(htb_lst)) + '.' + (''.join(htb_fracfin))
    
# #return hex value
#     return hex_final


# # test = input("enter: ")
# test = 25.5
# x = XtoBin(test)
# print(x.hex_bin())  # Output: 010101.101