# class One_complement:
#   def __init__(self, given_bin):
#     self.given_bin = given_bin

#   def switch(self):
#     binlst,_, binflt = str(self.given_bin).partition(".")
#     rev_bin = [str(1 - int(i)) for i in binlst]
#     rev_frac = [str(1 - int(i)) for i in binflt]
#     binint=("".join(rev_bin))
#     binflt=("".join(rev_frac))
#     return f'{binint}.{binflt}'

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

class XtoBin:
  def __init__(self, given_bin):
    self.given_bin = given_bin

  def dec_bin(self):
      dtb_int,_, dtb_flt = str(self.given_bin).partition(".")

    #convert the int to bin
      
      # dtb_conv = sum(int(digit)* (2**(i + 1)) for i, digit in enumerate(dtb_int)[2:])
      dtb_conv = bin(int(dtb_int))[2:]
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
        
        final_result = str(dtb_conv) + '.' + frac_final

        return final_result
  def oct_bin(self):
    pass

  def hex_bin(self):
    pass

test = input("enter: ")
x = XtoBin(test)
print(x.dec_bin())  # Output: 1010.1001