if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    total_scores = student_marks[query_name]
    print("{0:.2f}".format(sum(total_scores)/(len(total_scores))))
