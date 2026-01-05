n = int(input())
students = []
for i in range(n):
    name = input(f"input name {i+1}: ")
    mark = float(input(f"mark {i+1}: "))
    students.append([name,mark])

score = sorted(set([x for _,x in students]))
y = sorted([name for name,mark in students if mark == score[1]])
for x in y:
    print(x)
    