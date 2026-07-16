# Student Score Analyzer
# Assignment 1

import numpy as np

# Store marks in a list
marks = [72, 85, 90, 45, 63, 78, 91, 56, 88, 67]

# Function to return grade based on score
def grade(score):
    if score >= 85:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "F"


print("===== Student Grades =====")
for i, mark in enumerate(marks, start=1):
    print(f"Student {i}: {mark} -> {grade(mark)}")
  
print("\nNumpy starts here")

# Convert list to NumPy array
arr = np.array(marks)

print("\n===== Statistics =====")
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Standard Deviation:", np.std(arr))

# Students scoring above average
average = np.mean(arr)
count = np.sum(arr > average)

print("\nAverage Score:", average)
print("Students above average:", count)

# Print only A grade scores (>=85)
print("\nA Grade Scores:")
print(arr[arr >= 85])

# ---------------- BONUS ----------------

print("\n===== Bonus Part =====")

# Add 5 more students
marks.extend([95, 81, 49, 73, 66])

# Convert again
arr = np.array(marks)

print("\nUpdated Statistics")
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Standard Deviation:", np.std(arr))

# Count grades
grade_count = {"A": 0, "B": 0, "C": 0, "F": 0}

for mark in marks:
    g = grade(mark)
    grade_count[g] += 1

print("\nGrade Counts")
for g, c in grade_count.items():
    print(f"{g}: {c}")

# Find grade category with most students
most_grade = max(grade_count, key=grade_count.get)

print("\nGrade category with most students:", most_grade)