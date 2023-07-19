student_marks = {'Krishna': [67.0, 68.0, 69.0], 'Arjun': [70.0, 98.0, 63.0], 'Malika': [52.0, 56.0, 60.0]}
query_name = 'Malika'
value = []
equal = 0

for i in student_marks.keys():
        if student_marks[i] == student_marks[query_name]:   #mencari key name yang sesuai dengan query
            value = student_marks[i]    #assignment values pada variable value
for i in range(len(value)):
      equal += value[i] / len(value)
      print(equal)

      