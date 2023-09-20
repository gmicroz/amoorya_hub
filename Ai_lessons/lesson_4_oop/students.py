
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
    
     


std1 = Student(name="Salem", age=16, stage="3rd high school", mark=9)

print(std1.name, std1.mark, std1.stage)


# استدعاء داله send mark ?? واجب