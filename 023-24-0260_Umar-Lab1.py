import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



#===================================== PRACTICE TASKS =========================================


# =============================
# DAY 1
# ==============================

# Task 1
num1 = int(input("enter first no: "))
num2 = int(input("enetr 2nd no : "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 / num2)
print("Floor Division:", num1 // num2) 
print("Modulus:", num1 % num2)


# Task 2
fahrenheit = float(input("enter  temperature :"))
fahrenheit = float(fahrenheit)
celsius = (fahrenheit - 32) * 5 / 9

print(f"{fahrenheit} Fahrenheit = {celsius:.2f} Celsius")


# Task 3
print("Prime numbers from 1 to 100:")

for number in range(2, 101):
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
            break

    if prime:
        print(number, end=" ")

print()


# Task 4
number = 17
if number & 1:
    print(number, "is Odd")
else:
    print(number, "is Even")


# ===================================
# DAY 2
# ==================================

# Task 1
def stats(*nums):

    minimum = min(nums)
    maximum = max(nums)
    average = sum(nums) / len(nums)

    return minimum, maximum, average


print("Statistics:", stats(10, 20, 30, 40, 50))


# Task 2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [x ** 2 for x in numbers if x % 2 == 0]
print("Even number squares:", even_squares)


# Task 3
course1 = {"Ali", "Bilal", "Umar", "Fahad"}
course2 = {"Fahad", "Umar", "Ayesha", "Bilal"}

both_courses = course1 & course2
only_one = course1 ^ course2

print("Students in both courses:", both_courses)
print("Students in only one course:", only_one)


# Task 4
def remove_duplicates(numbers):

    result = []

    for x in numbers:
        if x not in result:
            result.append(x)

    return result


numbers = [1, 2, 3, 2, 4, 1, 5, 3]

print("Original list:", numbers)
print("New list:", remove_duplicates(numbers))


# Task 5
cubes = {x: x ** 3 for x in range(1, 11)}
print("Cubes:", cubes)


# ============================================================
# DAY 3                       NumPy Fundamentals
# ============================================================

# Task 1
arr = np.arange(1, 16)

print("Array:", arr)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data type:", arr.dtype)


# Task 2
random_array = np.random.randint(10, 51, (5, 5))

print(random_array)
print("Maximum:", np.max(random_array))
print("Minimum:", np.min(random_array))
print("Mean:", np.mean(random_array))


# Task 3
arr = np.arange(1, 21)
matrix = arr.reshape(4, 5)

print("Matrix:")
print(matrix)

print("2nd and 3rd columns:")
print(matrix[:, 1:3])


# Task 4
scores = np.array([
    55, 67, 72, 81, 90,
    45, 76, 88, 63, 95,
    70, 58, 84, 79, 92
])

mean_score = np.mean(scores)
above_mean = scores[scores > mean_score]

print("Scores:", scores)
print("Mean:", mean_score)
print("Scores above mean:", above_mean)


# Task 5
numbers = np.array([-5, 3, -2, 7, -1, 8, 4, -6 ])
result = np.where(numbers < 0, 0, 1)

print("Original:", numbers)
print("New array:", result)


# ============================================================
# DAY 4                                Pandas 1
# ============================================================

# Task 1
students = pd.DataFrame({
    "name": ["Ali", "Umair", "Umar", "Ayesha", "Hamza", "Fahad"],
    "subject": ["Python", "Python", "Java", "Database", "Database", "Java"],
    "marks": [78, 92, 65, 85, 74, 88]
})

print(students)

print("\nDataFrame information:")
students.info()

print("\nDataFrame description:")
print(students.describe())


# Task 2
# Using the actual CSV file downlaoded form google
csv_path = r"C:\Users\umarc\Desktop\ML-Lab Practice\student_marks.csv"

data = pd.read_csv(csv_path)

print("\nCSV Shape:")
print(data.shape)

print("\nCSV Columns:")
print(data.columns.tolist())

print("\nFirst 5 rows:")
print(data.head())      #.haed fundtion gives the first 5 row


# Task 3
top_students = students[
    students["marks"] > 80
]

print("\nStudents who scored above 80:")
print(top_students)


# Task 4
row_loc = students.loc[2]
row_iloc = students.iloc[2]

print("\nUsing loc:")
print(row_loc)

print("\nUsing iloc:")
print(row_iloc)

print("\nBoth are same:", row_loc.equals(row_iloc))


# ============================================================
# DAY 5                                  Pandas 2
# ============================================================

# Task 1
marks_data = pd.DataFrame({
    "name": ["Ali", "Fahad", "Umar", "Ayesha", "Hammmad" ],
    "marks": [ 80, np.nan, 75, np.nan, 90 ]
})

print("\nMissing values:")
print(marks_data.isna().sum())

marks_data["marks"] = marks_data["marks"].fillna(
    marks_data["marks"].mean()
)

print("\nAfter filling missing values:")
print(marks_data)


# Task 2
marks_data["pass_fail"] = marks_data["marks"].apply(
    lambda x: "Pass" if x >= 50 else "Fail"
)

print("\nPass/Fail:")
print(marks_data)


# Task 3
subject_data = pd.DataFrame({
    "name": [ "Ali", "Fahad", "Umar", "Ayesha", "Hammmad", "Zainab"],
    "subject": ["Python", "Python","PF", "PF","C++", "C#"],
    "marks": [78, 92, 65,88, 74, 90]
})

subject_result = subject_data.groupby("subject")["marks"].agg(
    ["mean", "min", "max"]
)

print("\nSubject result:")
print(subject_result)


# Task 4
student_info = pd.DataFrame({
    "student_id": [1, 2, 3, 4],
    "name": ["Ali", "Fahad", "Umar", "Uzair" ]
})

attendance = pd.DataFrame({
    "student_id": [1, 2, 3, 4],
    "attendance": [90, 82, 70, 95]
})

merged_data = pd.merge( student_info, attendance, on="student_id" )

print("\nMerged data:")
print(merged_data)


# ============================================================
# DAY 6                                    Matplotlib
# ============================================================

# Task 1
days = range(1, 11)

temperature = [
    31, 32, 34, 33, 35,
    36, 34, 37, 38, 36
]

plt.figure(figsize=(7, 4))

plt.plot(days, temperature, marker="o" )

plt.xlabel("Day")
plt.ylabel("Temperature (C)")
plt.title("Temperature for 10 Days")

plt.show()


# Task 2
categories = ["A", "B", "C", "D"]

counts = [10, 15, 8, 12]

marks_for_hist = [
    45, 55, 60, 62, 65,
    68, 70, 72, 75, 78,
    80, 82, 85, 88, 90
]

fig, ax = plt.subplots( 1, 2, figsize=(10, 4))

ax[0].bar( categories, counts )
ax[0].set_xlabel("Category")
ax[0].set_ylabel("Count")
ax[0].set_title("Category Counts")


ax[1].hist( marks_for_hist, bins=5, edgecolor="black" )
ax[1].set_xlabel("Marks")
ax[1].set_ylabel("Frequency")
ax[1].set_title("Marks Distribution")

plt.tight_layout()
plt.show()


# Task 3
box_data = pd.DataFrame({
    "marks": [45, 55, 60, 65, 70, 72, 75, 78, 80, 85, 90, 95 ]
})

box_data["marks"].plot(
    kind="box"
)

plt.title("Marks Boxplot")
plt.ylabel("Marks")

plt.show()
print("The boxplot shows the spread of marks and possible outliers.")

#task4
# Load the CSV
mini_data = pd.read_csv(csv_path)

print("Original data:")
print(mini_data.head())

# Checking missing values
print("\nMissing values:")
print(mini_data.isna().sum())

# Fill missing if any
numeric_columns = mini_data.select_dtypes(include="number").columns

for column in numeric_columns:

    mini_data[column] = mini_data[column].fillna(
        mini_data[column].mean()
    )


print("\nData after cleaning:")
print(mini_data.head())


# Convert subject columns into rows
subject_columns = [ "Maths","Physics", "Chemistry", "English", "Biology", "Economics", "History", "Civics"]

long_data = mini_data.melt(
    id_vars=["Gender"],
    value_vars=subject_columns,
    var_name="subject",
    value_name="marks"
)


# Calculating average marks and top marks
summary = long_data.groupby("subject")["marks"].agg(["mean", "std", "max"])

print("\nSubject summary:")
print(summary)


# Bar chart of average marks
plt.figure(figsize=(9, 5))
plt.bar(summary.index, summary["mean"])

plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.title("Average Marks by Subject")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


# Histogram of all marks
plt.figure(figsize=(7, 4))
plt.hist( long_data["marks"], bins=8, edgecolor="black" )

plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Overall Marks Distribution")

plt.show()

print("The bar chart compares the average marks of different subjects.")
print("The histogram shows how the marks are distributed.")











# =======================================================================================================
#                                          WEEKLY LAB EXERCISE
# =======================================================================================================


# ======================
# Q1
# ======================

a = 15
b = 25

print("\nQ1")
print("Before:", a, b)

a, b = b, a

print("After:", a, b)


# ===========================
# Q2
# ===========================

def is_prime(n):

    if n < 2:
        return False

    for i in range(2, n):

        if n % i == 0:
            return False

    return True


print("\nQ2")
print("7:", is_prime(7))
print("10:", is_prime(10))


# ==============================
# Q3
# =============================

n = 10

a = 0
b = 1

print("\nQ3")
print("Fibonacci sequence:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

print()


# ================================
# Q4
# ================================

def remove_duplicates(numbers):

    result = []

    for x in numbers:
        if x not in result:
            result.append(x)

    return result


numbers = [2, 4, 2, 6, 4, 8, 6, 10]

print("\nQ4")
print("Original list :", numbers)
print("New list:", remove_duplicates(numbers))


# ==================================
# Q5
# ===================================

def multiply(*args):

    result = 1

    for x in args:
        result = result * x

    return result


print("\nQ5")
print("Product:", multiply(2, 3, 4, 5))


# ================================
# Q6
# ====================================

text = "programming"

frequency = {
    char: text.count(char)
    for char in set(text)
}

print("\nQ6")
print("Text:", text)
print("Frequency:", frequency)


# =====================================
# Q7
# ======================================

employees = [
    {
        "name": "Ali",
        "department": "IT",
        "salary": 70000
    },
    {
        "name": "Farukh",
        "department": "HR",
        "salary": 65000
    },
    {
        "name": "Umar",
        "department": "Developer",
        "salary": 85000
    },
    {
        "name": "Jalil",
        "department": "IT",
        "salary": 78000
    }
]

highest = employees[0]

for employee in employees:

    if employee["salary"] > highest["salary"]:
        highest = employee


print("\nQ7")
print("Employee with highest salary:")
print(highest)


# ====================================
# Q8
# =====================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = list( filter(lambda x: x % 2 != 0, numbers ))

print("\nQ8")
print("Odd numbers:", odd_numbers)


# =====================================
# Q9
# ====================================

arr = np.arange(1, 31)
matrix = arr.reshape(5, 6)

print("\nQ9")
print(matrix)


# =======================
# Q10
# ======================

matrix = np.eye(6, dtype=int)
np.fill_diagonal(matrix,[1, 2, 3, 4, 5, 6])

print("\nQ10")
print(matrix)


# ==============================
# Q11
# ================================

numbers = np.random.randint(1, 101,25)

print("\nQ11")
print("Array:", numbers)
print("Sum:", np.sum(numbers))
print("Mean:", np.mean(numbers))
print("Standard deviation:",np.std(numbers))


# ============================================================
# Q12
# ============================================================

matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

diagonal = np.diag(matrix)

print("\nQ12")
print("Diagonal:", diagonal)
print("Sum:", np.sum(diagonal))


# ===================================
# Q13
# ====================================

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

B = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

print("\nQ13")

print("Element-wise multiplication:")
print(A * B)

print("\nMatrix multiplication:")
print(A @ B)


# ============================
# Q14
# =============================

temperatures = np.array([
    32, 34, 36, 38, 31,
    37, 39, 33, 35, 40,
    36, 34, 30, 37, 41,
    32, 35, 38, 36, 33,
    31, 39, 40, 34, 37,
    36, 32, 35, 38, 42
])

above_35 = temperatures[
    temperatures > 35
]

print("\nQ14")
print("Temperatures above 35:")
print(above_35)

print("Number of days:", len(above_35))


# =================================
# Q15
# ================================

numbers = np.array([10, 20, 30, 40, 50])

normalized = (
    (numbers - np.min(numbers)) / (np.max(numbers) - np.min(numbers))
)

print("\nQ15")
print("Original:", numbers)
print("Normalized:", normalized)


# ===================================
# Q16
# ===================================

marks = np.array([
    [80, 75, 90],
    [65, 70, 72],
    [88, 92, 85],
    [55, 60, 58],
    [95, 89, 93]
])

total = np.sum(marks, axis=1)
average = np.mean( marks, axis=1 )

print("\nQ16")
print("Total marks:", total)
print("Average marks:", average)


# ===============================
# Q17
# ==============================

numbers = np.array([
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10
])

result = np.where(numbers % 2 == 0, -1, numbers )

print("\nQ17")
print("Original:", numbers)
print("Result:", result)


# =====================================
# Q18
# ====================================

students = pd.DataFrame({
    "name": ["Ali", "Umair", "Umar", "Ayesha", "Hamza", "Fahad", "Bilal", "Zainab"],
    "section": ["A", "A", "B", "B","A", "B", "A", "B"],
    "marks": [ 85, 92, 45, 78, 74, 88, 38, 96 ]
})

print("\nQ18")
print(students)

print("\nDescription:")
print(students.describe())


# ===================================
# Q19
# ===================================

# Load the student_marks.csv
df = pd.read_csv(csv_path)

print("\nQ19")
print("First 5 rows:")
print(df.head())

print("\nMissing values before:")
print(df.isna().sum())

df.loc[2, "Maths"] = np.nan
df.loc[5, "Physics"] = np.nan

print("\nMissing values after adding practice values:")
print(df.isna().sum())

numeric_columns = df.select_dtypes(include="number").columns

for column in numeric_columns:

    df[column] = df[column].fillna(
        df[column].mean()
    )


print("\nMissing values after filling:")
print(df.isna().sum())

print("\nData after filling:")
print(df)


# ==============================================
# Q20
# ===============================================
print("\nQ20")

below_50 = df.loc[
    df["Maths"] < 50,
    ["Gender", "Maths"]
]

print(below_50)


# =================
# Q21
# ================
print("\nQ21")
section_marks = students.groupby("section")["marks"].agg(["mean", "max"])
print(section_marks)


# ================================
# Q22
# =================================

student_data = pd.DataFrame({
    "student_id": [1, 2, 3, 4, 5],
    "name": ["Ali", "Fahad", "Umar", "Ayesha", "Hammmad"]
})

attendance_data = pd.DataFrame({
    "student_id": [1, 2, 3, 4, 5],
    "attendance": [85, 92, 68, 74, 88 ]
})

merged = pd.merge(student_data, attendance_data, on="student_id" )

print("\nMerged data:")
print(merged)

print("\nAttendance below 75%:")
print( merged[ merged["attendance"] < 75 ] )


# ==================================
# Q23
# =====================================

average_marks = students.groupby("section")["marks"].mean()
print("\nQ23")
plt.figure(figsize=(7, 4))
plt.bar(average_marks.index, average_marks.values )

plt.xlabel("Section")
plt.ylabel("Average Marks")
plt.title("Average Marks per Section")

plt.show()


# ================================
# Q24
# ==================================

print("\nQ24")

plt.figure(figsize=(7, 4))

plt.hist( students["marks"], bins=5,edgecolor="black")

plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Distribution of Student Marks")

plt.show()
print( "The histogram shows the distribution of the students' marks." )


# ============================================================
# Q25
# ============================================================

days = [1, 2, 3, 4,5, 6, 7, 8]
temperature = [ 30, 32, 31, 35, 36, 34, 37, 39]
study_hours = [2, 3, 1, 4, 5, 3, 6, 7]
student_marks = [60, 65, 58, 72, 78, 70, 85, 90]

fig, ax = plt.subplots(1, 2, figsize=(10, 4))


# Line plot
ax[0].plot(days, temperature, marker="o")
ax[0].set_xlabel("Day")
ax[0].set_ylabel("Temperature")
ax[0].set_title("Daily Temperature")


# Scatter plot
ax[1].scatter(study_hours,student_marks)
ax[1].set_xlabel("Study Hours")
ax[1].set_ylabel("Marks")
ax[1].set_title("Study Hours vs Marks")


plt.tight_layout()

plt.show()

# =============================================== end ====================================