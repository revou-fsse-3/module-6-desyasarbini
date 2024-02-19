from app.repositories.employee_repo import Employee_repo

class Employee_service:

    def __init__(self):
        self.employee_repo = Employee_repo()

    def get_employee(self):
        employees = self.employee_repo.get_list_employee()
        return [employee.as_dict() for employee in employees]

    def update_employee(self, id, employee_data):
        updated_employee = self.employee_repo.update_employee(id, employee_data)
        return updated_employee
    
    def search_employee(self, name):
        employees = self.employee_repo.search_employee(name)
        return [employee.as_dict() for employee in employees]
    
    