#programme to calculate amount of sweets divided between students wih teacher keeping the remainder

Teacher = int(40)
students = int(14)

teacher_keeps = Teacher % students
students_keep = Teacher - teacher_keeps

print("the teacher keeps " + str(teacher_keeps) + ", the students keep " + str(students_keep))




