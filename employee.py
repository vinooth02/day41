class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_details(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_details(self):
        super().display_details()
        print("Department:", self.department)


if __name__ == "__main__":
    manager = Manager("Riya", 50000, "IT")
    manager.display_details()

