class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Xin chào tôi tên là {self.name}, năm nay tôi {self.age} tuổi")


class Student(Person):

    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        print(f"Tôi tên là {self.name}, {self.age} tuổi, MSV {self.student_id}")


class Teacher(Person):

    def __init__(self, name, age, subject):
        super().__init__(name, age) 
        self.subject = subject

    def introduce(self):
        print(f"Tôi là giáo viên {self.name}, {self.age} tuổi, giảng dạy môn {self.subject}.")

student1 = Student("Thành Đạt", 100, "SV1")
student1.introduce()

teacher1 = Teacher("Dương", 24, "Quản lí hệ thống")
teacher1.introduce()
