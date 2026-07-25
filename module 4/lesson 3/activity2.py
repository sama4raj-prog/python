my_dict = {
    "Codingal":2,
    "is":2,
    "best":2,
    "for":2,
    "coding":1
}

k = 2
result = 0

for key in my_dict:
    if my_dict[key] == k:
        result += 1

print(result)