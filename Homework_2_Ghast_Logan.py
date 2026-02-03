ratings = {
 "Alice": {"Inception": 5, "Titanic": 3, "Avatar": 4, "Jaws": 2},
 "Bob": {"Inception": 4, "The Matrix": 5, "Avatar": 5, "Jaws": 3},
 "Carol": {"Titanic": 5, "The Matrix": 4, "Avatar": 3, "Interstellar": 5},
 "Dave": {"Inception": 3, "Titanic": 4, "The Matrix": 5, "Jaws": 4},
 "Eve": {"Inception": 5, "Avatar": 4, "Interstellar": 4, "Jaws": 1}
}
#Problem 1: Movie Rating Analysis
#Part A:

print("=== User Statistics ===")
for user, movies in ratings.items():
    num_movies = len(movies)
    avg_rating = sum(movies.values()) / num_movies
    favorite_movie = max(movies, key=movies.get)
    favorite_rating = movies[favorite_movie]
    print(f"{user}: {num_movies} movies, avg rating: {avg_rating:.2f}, favorite: {favorite_movie} ({favorite_rating})")

#Part B:


print("\n=== Movie Statistics ===")
movie_totals = {}
movie_counts = {}
for user, movies in ratings.items():
    for movie, rating in movies.items():
        if movie not in movie_totals:
            movie_totals[movie] = 0
            movie_counts[movie] = 0
        movie_totals[movie] += rating
        movie_counts[movie] += 1
for movie in movie_totals:
    avg_rating = movie_totals[movie] / movie_counts[movie]
    print(f"{movie}: {avg_rating:.2f} avg ({movie_counts[movie]} reviews)")

#Part C: 
highly_rated_movies = [movie for movie, total in movie_totals.items() if (total / movie_counts[movie]) >= 4.0]
print("\nMovies with average rating of 4.0 or higher:")
for movie in highly_rated_movies:
    print(f"- {movie}")




print("")
print("="*40)

#Problem 2: Sales Data Transformer
#Given Data:
sales_records = [
 {"product": "Laptop", "category": "Electronics", "price": 999, "quantity": 5,
"region": "North"},
 {"product": "Mouse", "category": "Electronics", "price": 25, "quantity": 50,
"region": "North"},
 {"product": "Desk", "category": "Furniture", "price": 350, "quantity": 8,
"region": "South"},
 {"product": "Chair", "category": "Furniture", "price": 150, "quantity": 20,
"region": "South"},
 {"product": "Laptop", "category": "Electronics", "price": 999, "quantity": 3,
"region": "South"},
 {"product": "Keyboard", "category": "Electronics", "price": 75, "quantity":
    30, "region": "North"},
    {"product": "Chair", "category": "Furniture", "price": 150, "quantity": 15,
     "region": "North"},
 {"product": "Desk", "category": "Furniture", "price": 350, "quantity": 5,
"region": "North"},
 {"product": "Monitor", "category": "Electronics", "price": 300, "quantity":
12, "region": "South"},
]
print("")
#Part A: Dicionary Comprehensions
#1. product_prices: Maps each unique product to its price:
product_prices = {record["product"]: record["price"] for record in sales_records}
print("Product Prices:")

for product, price in product_prices.items():
    print(f"- {product}: ${price}")

#2. expensive_products: Only products with price > 100
expensive_products = {record["product"]: record["price"] for record in sales_records if record["price"] > 100}
print("\nExpensive Products (price > $100):")
for product, price in expensive_products.items():
    print(f"- {product}: ${price}")
    
#3. price_category: Maps each product to "Premium" if price 300, else "Standard"
price_category = {record["product"]: ("Premium" if record["price"] >= 300 else "Standard") for record in sales_records}
print("\nPrice Category:")
for product, category in price_category.items():
    print(f"- {product}: {category}")
    
#Part B: Aggregation Pattern
# 1. total_by_category: Total revenue (price × quantity) per category
total_by_category = {}
for record in sales_records:
    category = record["category"]
    revenue = record["price"] * record["quantity"]
    if category not in total_by_category:
        total_by_category[category] = 0
    total_by_category[category] += revenue
    
print("\nTotal Revenue by Category:")
for category, total in total_by_category.items():
    print(f"- {category}: ${total}")

#2. total_by_region: Total revenue per region
total_by_region = {}
for record in sales_records:
    region = record["region"]
    revenue = record["price"] * record["quantity"]
    if region not in total_by_region:
        total_by_region[region] = 0
    total_by_region[region] += revenue
print("\nTotal Revenue by Region:")
for region, total in total_by_region.items():
    print(f"- {region}: ${total}")
    
#3. quantity_by_product: Total quantity sold per product (across all records)
quantity_by_product = {}
for record in sales_records:
    product = record["product"]
    quantity = record["quantity"]
    if product not in quantity_by_product:
        quantity_by_product[product] = 0
    quantity_by_product[product] += quantity
print("\nTotal Quantity Sold by Product:")
for product, total_quantity in quantity_by_product.items():
    print(f"- {product}: {total_quantity} units")
 
 
print("")
print("="*40)
print("")


#Problem 3: Course Registration System
# Given Data:
# Students and their registered courses
registrations = {
 "Alice": {"CS101", "CS201", "MATH101"},
 "Bob": {"CS101", "MATH101", "PHYS101"},
 "Carol": {"CS201", "CS301", "MATH201"},
 "Dave": {"CS101", "CS201", "MATH101", "PHYS101"},
 "Eve": {"CS301", "MATH201", "MATH301"}
}
# Course prerequisites (must have taken these BEFORE registering)
prerequisites = {
 "CS101": set(), # No prerequisites
 "CS201": {"CS101"}, # Must have CS101
 "CS301": {"CS201"}, # Must have CS201
 "MATH101": set(), # No prerequisites
 "MATH201": {"MATH101"}, # Must have MATH101
 "MATH301": {"MATH201"}, # Must have MATH201
 "PHYS101": {"MATH101"} # Must have MATH101
}
# Course capacities and current enrollment
capacity = {"CS101": 30, "CS201": 25, "CS301": 20, "MATH101": 35, "MATH201": 25,
"MATH301": 20, "PHYS101": 30}

#Part A: Set Operations

print("=== Part A: Set Operations ===")
all_courses = set()
for courses in registrations.values():
    all_courses.update(courses)
print(f"All courses with enrollment: {all_courses}")
common_courses = set.intersection(*registrations.values())
print(f"Courses ALL students share: {common_courses}")
alice_courses = registrations["Alice"]
other_students_courses = set()
for student, courses in registrations.items():
    if student != "Alice":
        other_students_courses.update(courses)
only_alice_courses = alice_courses - other_students_courses
print(f"Courses ONLY Alice takes: {only_alice_courses}")
cs_students = {student for student, courses in registrations.items() if any(course.startswith("CS") for course in courses)}
print(f"Students in CS courses: {cs_students}")
print("")

#Part B: Prerequisite Check

print("=== Part B: Prerequisite Check ===")
for student, courses in registrations.items():
    invalid_courses = []
    for course in courses:
        prereqs = prerequisites.get(course, set())
        if not prereqs.issubset(courses):
            missing = prereqs - courses
            invalid_courses.append((course, missing))
    if not invalid_courses:
        print(f"{student}: VALID")
    else:
        print(f"{student}: INVALID - Missing prerequisites:")
        for course, missing in invalid_courses:
            print(f"{course} requires {prerequisites[course]} but missing: {missing}")
print("")



#Part C: Enrollment Analysis


print("=== Part C: Enrollment Analysis ===")
print("")
overloaded_students = {student for student, courses in registrations.items() if len(courses) >= 4}
print(f"Overloaded students (4+ courses): {overloaded_students}")
all_math_courses = {course for course in registrations.values() for course in courses if course.startswith("MATH")}
print(f"All MATH courses enrolled: {all_math_courses}")
schedule_map = {}
for student, courses in registrations.items():
    course_tuple = tuple(sorted(courses))
    if course_tuple not in schedule_map:
        schedule_map[course_tuple] = []
    schedule_map[course_tuple].append(student)
identical_schedules = {tuple_: students for tuple_, students in schedule_map.items() if len(students) > 1}
if identical_schedules:
    print("Students with identical schedules:")
    for course_tuple, students in identical_schedules.items():
        print(f" Courses: {course_tuple} - Students: {students}")
else:
    print("Students with identical schedules: None found")
enrollment_per_course = {}
for student, courses in registrations.items():
    for course in courses:
        if course not in enrollment_per_course:
            enrollment_per_course[course] = 0
        enrollment_per_course[course] += 1
print("Enrollment per course:")
for course, count in enrollment_per_course.items():
    print(f" {course}: {count} students")
under_enrolled_courses = {course for course, count in enrollment_per_course.items() if count < 3}
print(f"Under-enrolled courses (<3 students): {under_enrolled_courses}")
print("")
