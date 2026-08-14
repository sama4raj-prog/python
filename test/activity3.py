grade_book = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 90,
    "Eve": 88
}

# Calculating the class average
total_score = 0
for score in grade_book.values():
    total_score += score
class_average = total_score / len(grade_book)
print(f"Class Average: {class_average:.2f}")

# Finding the highest and lowest scores of the class

top_student = max(grade_book, key=grade_book.get)
lowest_student = min(grade_book, key=grade_book.get)

print(f"Highest Score: {top_student} with {grade_book[top_student]}")
print(f"Lowest Score: {lowest_student} with {grade_book[lowest_student]}")

#User lookup using input and recieve a friendly message if missing
search_name = input("Enter a student's name to look up their grade: ")

score = grade_book.get(search_name, "Not found")
if score != "Not found":
    print(f"{search_name}'s score is: {score}")
else:
    print("Student not found.")