weight=int(input("enter the weight:"))

unit= input("(L)lb or (K)kg")
if unit.upper()=="L":
    converted= weight*0.45
    print(f"the weight in kilos is {converted}")
else:
    convertedw = weight//0.45
    print(f"the weight in punds is {convertedw}")

    
