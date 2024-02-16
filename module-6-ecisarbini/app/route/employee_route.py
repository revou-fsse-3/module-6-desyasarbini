from flask import Blueprint, jsonify

employee_blueprint = Blueprint('employee_endpoint', __name__)

employee = [
    {
        'name'  : 'Alif',
        'age'   : '25'
    },
    {
        'name'  : 'Budi',
        'age'   : '25'
    },
    {
        'name'  : 'Dinda',
        'age'   : '28'
    }
]

@employee_blueprint.route("/", methods=['GET'])
def get_employee():
    return jsonify(employee)

# @employee_blueprint.route("/<int:employee_id>", methods=['GET'])
# def detail_employee(employee_id):
#     return jsonify(employee_id(employee_id))

@employee_blueprint.route("/", methods=['POST'])
def create_employee():
    return 'Create Employee'

@employee_blueprint.route("/<int:employee_id>", methods=['PUT'])
def update_employee(employee_id):
    return str(employee_id) # employee_id diubah dulu ke string

@employee_blueprint.route("/<int:employee_id>", methods=['DELETE'])
def delete_employee(employee_id):
    return str(employee_id)

