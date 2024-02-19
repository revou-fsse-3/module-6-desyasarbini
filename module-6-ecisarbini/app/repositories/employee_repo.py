from app.models.employee import Employee
from app.utils.database import db

class Employee_repo:
    def get_list_employee(self):
        employee = Employee.query.all()
        return employee

    def search_employee(self, name):
        employee = Employee.query.filter(Employee.name.like(f'%{name}%')).all()
        return employee

    def update_employee(self, id, employee):
        employee_obj = Employee.query.get(id)
        employee_obj.name = employee.name
        employee_obj.age = employee.age

        db.session.commit()