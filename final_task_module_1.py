grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

for a in range(0, 5):
    result = sum(grades[a]) / len(grades[a])
    grades[a] = result
#print(grades)

sorted_students = sorted(students)
modified_students = tuple(sorted_students)

Journal = {}
for i in range(len(grades)):
    Journal = dict(zip(modified_students, grades))
print(Journal)
