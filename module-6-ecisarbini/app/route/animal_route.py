from flask import Blueprint, request
from app.utils.database import db
from app.models.animal import Animal

animal_blueprint = Blueprint('animal_endpoint', __name__)

@animal_blueprint.route("/", methods=['GET'])
def get_list_animal():
    try:
        animal = Animal.query.all()

        return [animal.as_dict() for animal in animal], 200
    except Exception as e:
        return e, 500

@animal_blueprint.route("/", methods=['POST'])
def create_animal():
    try:
        data = request.json
        print(data)

        animal = Animal()
        animal.name = data['name']
        animal.birthdate = data['birthdate']
        db.session.add(animal)
        db.session.commit()

        return 'berhasil', 200
    except Exception as e:
        return e, 500
    
@animal_blueprint.route("/<int:animal_id>", methods=['PUT'])
def update_animal(animal_id):
        return str(animal_id), 200

@animal_blueprint.route("/<int:animal_id>", methods=['DELETE'])
def delete_employee(animal_id):
    return str(animal_id)