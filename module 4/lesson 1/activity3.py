list = [4,5,6,3,1,2,10]

sum = 0
for item in list:
    sum = item + sum
print("Sum:", sum)

avg = sum / len(list)
avg = round(avg, 2)
print("Average:", avg)

list.sort()
print("Sorted list:", list)

print("Smallest Number: ", list[0])
print("Largest Number: ", list[-1])
