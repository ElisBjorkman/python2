f = open("text.txt", "r", encoding="utf-8")
lines = f.readlines()

name = input()

new_list = []

for line in lines:
    if line.split()[0] != name + ":":
        new_list.append(line)

print(new_list)

f= open('newtext.txt', 'w')
f.writelines(new_list)