class Student:
    name: str
    age: int
    grades: list[int]

    def add_grade(self,grade:int)-> None:
        self.grades.append(grade)

    def __init__(self,name:str,age:int,grades:list[int])->None:
        self.name = name
        self.age = age
        self.grades = grades

    def avg_grade(self)->float:
        return sum(self.grades)/len(self.grades)

    def __gt__(self,other:"Student")-> bool:
        return self.avg_grade() > other.avg_grade()

    def __lt__(self,other:"Student")-> bool:
        return self.avg_grade() < other.avg_grade()

    def __eq__(self,other:"Student")-> bool:
        return self.avg_grade() == other.avg_grade()

    def __str__(self):
        return f"{self.name}, {self.age}, {self.grades}"

    def __repr__(self):
        return f"{self.name}, {self.age}, {self.grades}"
class Group:

    students: list[Student] = []
    def add_student(self,student: Student) -> None:
        self.students.append(student)

    def del_student(self,student: Student) -> None:
        self.students.remove(student)

    def __str__(self):
        return f"{self.students}"

def find_student_highest_avg(groups:list[Group])-> Student:
    gr = "1"
    best = 5.0
    for group in groups:
       for student in group.students:
           if student.avg_grade() < best:
               best = student.avg_grade()
               gr = group
    return gr

x = Student("Adam",15,[2,3,4])
y = Student("Jane",13,[5,3,4])
z = Student("Cha",13,[1,3,4])
g = Group()
g1 = Group()
g.add_student(x)
g.add_student(y)
g1.add_student(z)
print(g1)
print(find_student_highest_avg([g1,g]))


