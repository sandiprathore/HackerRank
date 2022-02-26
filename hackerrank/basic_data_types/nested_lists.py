all_students_with_score = []
list__of_score = []
list_of_second_last = []
for i in range(int(input())):
    name = input()
    score = float(input())
    all_students_with_score = [[name,score]] +all_students_with_score
    list__of_score = [score ] + list__of_score
second_last = sorted(list(set(list__of_score)))[1]
for i in all_students_with_score:
    if i[1] == second_last:
        list_of_second_last.append(i[0])
list_of_second_last.sort()
for name_of_student in list_of_second_last:
    print(name_of_student)