from app.models.employee import Employee
from app.utils.database import db
from app.utils.api_response import api_response
from flask import jsonify, request
from pydantic import ValidationError
from app.service.employee_service import Employee_service
from app.controller.schema.validation_employee_request import Update_employee_request
from http.client import CREATED, INTERNAL_SERVER_ERROR, NOT_FOUND, OK

def list_employee():
    try:
        employee_service = Employee_service()
        employees = employee_service.get_employee()

        return api_response(
            status_code = OK,
            message = 'getting employee list worked',
            data = employees
        )
    except Exception as e:
        return str(e), INTERNAL_SERVER_ERROR
    
def get_employee(employee_id):
    try:
        employee = Employee.query.get(employee_id)

        if Employee:
            return jsonify({
                "id" : employee.id,
                "name": employee.name,
                "age": employee.age
            }), OK
        return jsonify({'error': 'Employee not Found'}), NOT_FOUND
    except Exception as e:
        return str(e), INTERNAL_SERVER_ERROR

    
def update_employee(employee_id):
    try:
        data = request.json
        update_employee_request = Update_employee_request(**data)
        print(update_employee_request)

        employee = Employee()
        employee.name = update_employee_request.name
        employee.age = update_employee_request.age

        employee_service = Employee_service()
        employees = employee_service.update_employee(employee_id, employee)

        return api_response(
            status_code = OK,
            message = 'Employee update successful',
            data = employees
        )
    except ValidationError as e:
        return api_response(
            status_code = 400,
            message = e.errors(),
            data = {}
        )
    except Exception as e:
            return str(e), INTERNAL_SERVER_ERROR
    
def create_employee():
    try:
        data = request.json
        
        employee = Employee()
        employee.id = data ['id']
        employee.name = data['name']
        employee.age = data['age']
        db.session.add(employee)
        db.session.commit()

        return 'Employee created successful', CREATED
    except Exception as e:
        return str(e), INTERNAL_SERVER_ERROR
    
def search_employee():
    try:
        request_data = request.args
        employee_service = Employee_service()
        employees = employee_service.search_employee(request_data["name"])

        return api_response(
            status_code = OK,
            message = 'search employee worked',
            data = employees
        )
    except Exception as e:
        return str(e), INTERNAL_SERVER_ERROR
    
def delete_employee(employee_id):
    try:
        employee = Employee.query.get(employee_id)

        if not employee:
            return 'Employee not found', NOT_FOUND
        db.session.delete(employee)
        db.session.commit()

        return 'Employee deleted successful', 202
    except Exception as e:
        return str(e), 500