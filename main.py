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