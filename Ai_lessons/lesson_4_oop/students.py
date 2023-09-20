
class Student:
    def __init__(self, name, age, stage, mark) -> None:
        self.name = name
        self.age = age
        self.stage = stage
        self.mark = mark
    
    def send_mark(self) -> None:
        # اطبع اسم الطالب ودرجته عن استدعاء هذه الدالة من الكائن
        ...
        ...
    
     
std1 = Student(name="Salem", age=16, stage="3rd high school", mark=7)
std2 = Student(name="Saeed", age=16, stage="3rd high school", mark=10)
std3 = Student(name="Faisal", age=17, stage="3rd high school", mark=4)

print(f"student name is {std1.name}, he is {std1.age} years old at {std1.stage} stage, got {std1.mark}/10")
print(f"student name is {std2.name}, he is {std2.age} years old at {std2.stage} stage, got {std2.mark}/10")
print(f"student name is {std3.name}, he is {std3.age} years old at {std3.stage} stage, got {std3.mark}/10")


# استدعاء داله send mark ?? واجب