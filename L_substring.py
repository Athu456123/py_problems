str1 = input()
max_length = 0
for i in range(len(str1)):
    seen = []
    current_length = 0
    for j in range(i, len(str1)):
        if str1[j] not in seen:
            seen.append(str1[j])
            current_length += 1
        else:
            break
    if current_length > max_length:
        max_length = current_length 

print(max_length)