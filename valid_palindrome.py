strings = input()

y = ""
for i in strings:
    if i.isalnum():
        y = i.lower()

if y == y[::-1]:
    print("True")
else:
    print("False")