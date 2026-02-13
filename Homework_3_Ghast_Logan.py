#Problem 1: Array creation and basic operations
import numpy as np
a = np.array([2, 4, 6, 8, 10])
b = np.array([1, 2, 3, 4, 5])


zeros_arr = np.zeros(8)
ones_matrix = np.ones((3, 4))
range_arr = np.arange(10, 51, 5)
linear_arr = np.linspace(0, 2, 9)

print("zeros_arr =", zeros_arr)
print("ones_matrix =", ones_matrix)
print("range_arr =", range_arr)
print("linear_arr =", linear_arr)

print("="*50)

print("a + b =", a + b)
print("a * b =", a * b)
print("a ** 2 =", a ** 2)
print("a / b =", a / b)
print("Sum of all elements in a =", np.sum(a))
print("Mean of all elements in b =", np.mean(b))

print("="*50)

#Problem 2: Array attributes and statistics


matrix = np.arange(1, 21).reshape(4, 5)
print("Matrix:\n", matrix)
print("Shape:", matrix.shape)
print("Number of dimensions:", matrix.ndim)
print("Total number of elements:", matrix.size)
print("Data type:", matrix.dtype)
print("Total bytes used:", matrix.nbytes)

print("="*50)

print("Overall mean:", np.mean(matrix))
print("Overall standard deviation:", np.std(matrix))
print("Minimum value:", np.min(matrix))
print("Maximum value:", np.max(matrix))
print("Sum of each row:", np.sum(matrix, axis=1))
print("Mean of each column:", np.mean(matrix, axis=0))
print("Index of the maximum value in the flattened array:", np.argmax(matrix))

print("="*50)

#Problem 3: indexing and boolean selection
# Student scores: 6 students, 4 exams
scores = np.array([
[85, 90, 78, 92], # Alice
[70, 65, 72, 68], # Bob
[95, 98, 94, 97], # Carol
[60, 55, 58, 62], # Dave
[88, 85, 90, 87], # Eve
[75, 80, 77, 82] # Frank
])
students = ['Alice', 'Bob', 'Carol', 'Dave', 'Eve', 'Frank']
exams = ['Exam1', 'Exam2', 'Exam3', 'Exam4']


alice_scores = scores[0, :]
exam3_scores = scores[:, 2]
bob_carol_submatrix = scores[1:3, 0:2]

print("Alice's scores:", alice_scores)
print("Exam 3 scores:", exam3_scores)
print("Bob and Carol's scores on Exam1 and Exam2:\n", bob_carol_submatrix)



high_scores_mask = scores >= 90
high_scores = scores[high_scores_mask]
num_high_scores = np.sum(high_scores_mask)
average_scores = np.mean(scores, axis=1)
students_with_high_avg = [students[i] for i in range(len(students)) if average_scores[i] >= 85]
scores[scores < 60] = 60
print("Scores >= 90:", high_scores)
print("Number of scores >= 90:", num_high_scores)
print("Students with average score >= 85:", students_with_high_avg)
print("Modified scores array:\n", scores)

print("="*50)

#Problem 4: Reshaping and Broadcasting



arr_1d = np.arange(1, 25)
matrix_4x6 = arr_1d.reshape(4, 6)
matrix_2x3x4 = arr_1d.reshape(2, 3, 4)
flattened_arr = matrix_2x3x4.flatten()
print("1D array:", arr_1d)
print("4x6 matrix:\n", matrix_4x6)
print("2x3x4 matrix:\n", matrix_2x3x4)
print("Flattened array:", flattened_arr)

print("="*50)

# Rows: products (Apple, Banana, Orange)
# Columns: stores (Store1, Store2, Store3, Store4)
prices = np.array([
[1.20, 1.50, 1.30, 1.40], # Apple
[0.50, 0.60, 0.55, 0.45], # Banana
[0.80, 0.90, 0.85, 0.75] # Orange
])


discounted_prices = prices * 0.9
prices_with_delivery = discounted_prices + 0.10
tax_rates = np.array([0.08, 0.06, 0.07, 0.05])
final_prices_with_tax = prices_with_delivery * (1 + tax_rates)
mean_prices = np.mean(prices, axis=1, keepdims=True)
normalized_prices = prices - mean_prices
print("Discounted prices:\n", discounted_prices)
print("Prices with delivery fee:\n", prices_with_delivery)
print("Final prices with tax:\n", final_prices_with_tax)
print("Normalized prices:\n", normalized_prices)
