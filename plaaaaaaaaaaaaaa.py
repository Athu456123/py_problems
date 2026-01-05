# Read input
N = int(input())
strs = input().split()

# Normal dictionary to group anagrams
anagram_groups = {}

for word in strs:
    key = ''.join(sorted(word))
    
    if key in anagram_groups:
        anagram_groups[key].append(word)
    else:
        anagram_groups[key] = [word]

# Print each group
for group in anagram_groups.values():
    print(' '.join(group))
 