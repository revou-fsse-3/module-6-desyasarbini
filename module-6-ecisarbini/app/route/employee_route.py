from flask import Blueprint
from app.controller.employee_controller import (
    list_employee, 
    get_employee,
    update_employee,
    create_employee,
    search_employee,
    delete_employee
    )

employee_blueprint = Blueprint('employee_endpoint', __name__)

employee_blueprint.route("/", methods=['GET'])(list_employee)

employee_blueprint.route("/<int:employee_id>", methods=['GET'])(get_employee)

employee_blueprint.route("/<int:employee_id>", methods=['PUT'])(update_employee)

employee_blueprint.route("/", methods=['POST'])(create_employee)

employee_blueprint.route("/search", methods=['GET'])(search_employee)

employee_blueprint.route("/<int:employee_id>", methods=['DELETE'])(delete_employee)