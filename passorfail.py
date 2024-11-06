medical_cause=(input("do u have a medical reason yes or no   "))
atten = int(input("enter the student's atendance  "))
if medical_cause=="yes": 
    print("you are allowed ")
else:
    if atten<75:
     print("youre not allowed ")
    else:
      print("you are allowed ")         