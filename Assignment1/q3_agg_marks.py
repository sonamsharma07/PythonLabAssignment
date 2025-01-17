print("Enter the marks obtained in 5 subjects (out of 100):")

marks = []
for i in range(1, 6):
    mark = float(input(f"Subject {i}: "))
    marks.append(mark)

agg_marks = 0
for mark in marks:
    agg_marks += mark

total_marks = 500  
per_marks = (agg_marks / total_marks) * 100

print(f"Aggregate Marks: {agg_marks:.2f}")
print(f"Percentage Marks: {per_marks:.2f}%")
