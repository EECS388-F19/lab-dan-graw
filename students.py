students = ["Raul", "Sophie", "Joe"]
students.sort()
first_name = students[0]
for s in students:
    print(s)
first_name = first_name[0:len(first_name) - 1]
print(first_name)
longest = students[0]
for s in students:
    if len(longest) < len(s):
        longest = s
print(longest)