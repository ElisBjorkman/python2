class student:
    def __init__(self, f_name : str, l_name : str, age : int, gender : str):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"{self.f_name} {self.l_name}"

class teacher:
    def __init__(self, f_name : str, l_name : str, age : int, gender : str):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.gender = gender
    
    def __str__(self):
        return f"{self.f_name} {self.l_name}"


class group:
    def __init__(self, subject : str, teacher : teacher, students : list):
        self.subject = subject
        self.teacher = teacher
        self.students = students


elis = student("Elis", "Björkman", 18, "Man")
joel = student("Joel", "Swartling", 17, "Man")
elias_e = student("Elias", "englsperger", 19, "Man")
elias = teacher("Elias", "Sjöling Njord", 21, "Man")

programmering = group("Programmering", elias, [elis, joel, elias_e])

input("teacher")
print(programmering.teacher)


input("student")
for a in programmering.students:
    print(a)

input()