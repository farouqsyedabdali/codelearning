while True:
  ques = float(input("Enter a number: "))
  
  while True:
    funcn = input("A/S/M/D: ").lower()
    ques2 = float(input("Enter another number: "))
    
    if funcn == "a":
      print(ques+ques2)
      ques = ques+ques2
    elif funcn == "s":
      print(ques-ques2)
      ques = ques-ques2
    elif funcn == "m":
      print(ques*ques2)
      ques = ques*ques2
    elif funcn == "d":
      print(ques/ques2)
      ques = ques/ques2
    else:
      print("Exiting...")
      break
  break

