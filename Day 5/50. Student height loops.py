student_heights = input("Input student heights: ").split()
total_height = 0
number_of_students = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

for height in student_heights:
    total_height += height

for student in student_heights:
    number_of_students += 1
print(total_height)
print(number_of_students)
average = round(total_height/number_of_students)
print(average)

