def convert_dec(self):
    btd_lst = str(self.giv_bin)[::-1]
#multiplying the bits by 2 raise to index
    deci_lst = [(2**index)* int(btd_lst[index]) for index in range(len(btd_lst))]
    decimal = sum(deci_lst)

    return decimal

convert_dec("1001")