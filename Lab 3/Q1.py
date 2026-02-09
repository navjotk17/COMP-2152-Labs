grades = [85, 92, 78, 95, 88]
grades.append(90)
grades.sort()
print(f"Sorted grades: {grades}") # Sorted grades: [78, 85, 88, 90, 92, 95]
print(f"Highest grade: {grades[-1]}")
print(f"Lowest grade: {grades[0]}")
print(f"Total number of grades: {len(grades)}")