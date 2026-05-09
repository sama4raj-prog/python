units = int(input("Enter the units consumed: "))

if units<50:
    total = units*2.6+25

elif units<100:
    total = units*3.25+35

elif units<200:
    total = units*5.26+45

else:
    total = units*8.45+75

print("The total electricity bill is: ", total)