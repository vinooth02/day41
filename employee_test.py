import unittest
from employee import Employee, Manager

class TestEmployee(unittest.TestCase):

    def test_employee_initialization(self):
        employee = Employee("John", 50000)
        self.assertEqual(employee.name, "John")
        

    def test_manager_initialization(self):
         employee = Employee("John", 50000)
         self.assertEqual(employee.salary, 50000)

    def test_manager_department(self):
        manager= Manager("John", 50000, "HR")
        self.assertEqual(manager.department, "HR")

    def test_manager_inheritance(self):
         manager = Manager("Riya", 50000, "IT")
         self.assertIsInstance(manager, Employee)

if __name__=="__main__":
    unittest.main()
                
        