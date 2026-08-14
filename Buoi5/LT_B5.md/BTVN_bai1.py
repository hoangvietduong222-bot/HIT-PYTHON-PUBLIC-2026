class Employee:

    def __init__(self, name, salary, department):
        self.name = name
        self.__salary = salary
        self._department = department

    def get_salary(self):
        return self.__salary

    def increase_salary(self, amount):
        if amount > 0:
            self.__salary += amount

    def calculate_bonus(self):
        return self.__salary * 0.05

    def show_info(self):
        print(f"Tên: {self.name}")
        print(f"Lương: {self.__salary}")
        print(f"Phòng ban: {self._department}")


class Developer(Employee):
    def __init__(self, name, salary, department, programming_language, overtime_hours):
        super().__init__(name, salary, department)
        self.programming_language = programming_language
        self.overtime_hours = overtime_hours

    def calculate_bonus(self):
        return self.get_salary() * 0.10 + self.overtime_hours * 100000

    def show_info(self):
        super().show_info()
        print(f"Ngôn ngữ: {self.programming_language}")
        print(f"Giờ làm thêm: {self.overtime_hours}")
        print(f"Tiền thưởng: {self.calculate_bonus()}")


class Manager(Employee):
    def __init__(self, name, salary, department, number_of_employees):
        super().__init__(name, salary, department)
        self.number_of_employees = number_of_employees

    def calculate_bonus(self):
        return self.get_salary() * 0.15 + self.number_of_employees * 200000

    def show_info(self):
        super().show_info()
        print(f"Số nhân viên: {self.number_of_employees}")
        print(f"Tiền thưởng: {self.calculate_bonus()}")


employees = [
    Employee("A", 8000000, "Hành chính"),
    Developer("B", 12000000, "IT", "Python", 10),
    Developer("C", 15000000, "IT", "Java", 5),
    Manager("D", 20000000, "Web", 8)
]


for employee in employees:
    employee.show_info()
    print( )


max_employee = employees[0]

for employee in employees:
    if employee.get_salary() > max_employee.get_salary():
        max_employee = employee

print("Nhân viên có lương cao nhất:")
print(max_employee.name)
print(max_employee.get_salary())


total_bonus = 0

for employee in employees:
    total_bonus += employee.calculate_bonus()

print("Tổng tiền thưởng:", total_bonus)


developer_count = 0
manager_count = 0

for employee in employees:
    if isinstance(employee, Developer):
        developer_count += 1

    if isinstance(employee, Manager):
        manager_count += 1

print("Số Developer:", developer_count)
print("Số Manager:", manager_count)