# Problem 1: Contact Manager
# Your name: Logan Ghast
# === Part A: Create and Populate ===
contacts = {
    "Mom": "555-1234",
    "Dad": "555-5678",
    "Best Friend": "555-8888",
    "Pizza Place": "555-9999",
    "Work": "555-0000"
}
# Add 5 contacts here
print("=== Initial Contacts ===")
print(contacts)


# === Part B: Access and Modify ===
print("\n=== Access and Modify ===")
# Print Mom's number
print("Mom's number:", contacts["Mom"])
# Update Dad's number
contacts["Dad"] = "555-4321"
# Add Dentist
contacts["Dentist"] = "555-2222"
# Look up Grandma safely
grandma_number = contacts.get("Grandma")
if grandma_number is None:
    print("Contact not found")

# Print updated contacts
print("Updated contacts:", contacts)
# === Part C: Delete and Analyze ===
print("\n=== Delete and Analyze ===")
# Remove Pizza Place
del contacts["Pizza Place"]
# Remove Work and save the number
old_work = contacts.pop("Work", None)
print(f"Removed work number: {old_work}")
print(f"Contacts remaining: {len(contacts)}")
print(f"Contact names: {list(contacts.keys())}")
print(f"Phone numbers: {list(contacts.values())}")






# Problem 2: Grade Book Analyzer
# Your name: Logan Ghast
grades = {
"Alice": 87,
"Bob": 65,
"Carol": 92,
"Dave": 78,
"Eve": 55,
"Frank": 88,
"Grace": 71,
"Henry": 95,
"Ivy": 60,
"Jack": 83
}
# === Part A: Basic Statistics ===
print("")
print("=== Basic Statistics ===")
print("")
print(f"Students: {list(grades.keys())}")
print(f"Grades: {list(grades.values())}")
print(f"Total students: {len(grades)}")
print(f"Sum of grades: {sum(grades.values())}")
average = sum(grades.values()) / len(grades)
print(f"Class average: {average:.2f}")
print(f"Highest grade: {max(grades.values())}")
print(f"Lowest grade: {min(grades.values())}")
# === Part B: Iteration and Analysis ===
print("\n=== Grade Report ===")
# Helper function for letter grade

def get_letter(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
# Print each student with letter grade
for name, grade in grades.items():
    letter = get_letter(grade)
    print(f"{name}: {grade} ({letter})")
# Count grades
print("\n=== Grade Distribution ===")
passed = 0
failed = 0
count_a = 0
count_b = 0
count_c = 0
count_d = 0
count_f = 0
for name, grade in grades.items():
# Count pass/fail
    if grade >= 60:
        passed += 1
    else:
        failed += 1
    # Count letter grades
    letter = get_letter(grade)
    if letter == "A":
        count_a += 1
    elif letter == "B":
        count_b += 1
    elif letter == "C":
        count_c += 1
    elif letter == "D":
        count_d += 1
    elif letter == "F":
        count_f += 1
print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"A grades: {count_a}")
print(f"B grades: {count_b}")
print(f"C grades: {count_c}")
print(f"D grades: {count_d}")
print(f"F grades: {count_f}")
# === Part C: Find Specific Students ===
print("\n=== Top and Bottom Performers ===")
# Find highest scorer
top_name = ""
top_grade = 0
for name, grade in grades.items():
    if grade > top_grade:
        top_grade = grade
        top_name = name
print(f"Highest scorer: {top_name} ({top_grade})")
# Find lowest scorer
bottom_name = ""
bottom_grade = 100
for name, grade in grades.items():
    if grade < bottom_grade:
        bottom_grade = grade
        bottom_name = name
print(f"Lowest scorer: {bottom_name} ({bottom_grade})")

print("\n=== Above Average Students ===")

for name, grade in grades.items():
    if grade > average and grade > 80:
        print(f"{name}: {grade}")