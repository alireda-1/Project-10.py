import random
user_pin=(input("Enter a 4-digit PIN code :\n"))
C_pin1=str(random.randint(0,9999)).zfill(4)
if len(user_pin)==4:
  if user_pin==C_pin1:
    print("match!")
  else:
    print("Failure! PIN code didn't match .")
    print(f"The computer generated this PIN : {C_pin1}")
else:
  print("Please enter 4 digits . ")
