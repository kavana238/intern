import pandas as pd

marks = pd.Series([78, 85, 92, 88],
                    index=['A', 'B', 'C', 'D'])
print(marks)

# apply condition 
mask = marks >= 80
print(mask)

#filter using mask
filtered_marks = marks[mask]
print(filtered_marks)

#only values where condition is true are kept
filtered_marks = marks[marks >= 80]
print(filtered_marks)

print(marks[(marks >= 80) & (marks < 90)])

marks[marks <70] = 70
print(marks)
