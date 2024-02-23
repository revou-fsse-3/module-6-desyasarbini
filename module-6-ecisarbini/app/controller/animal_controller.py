from app.models.animal import Animal
from app.utils.database import db
from app.utils.api_response import api_response
from flask import jsonify, request
from pydantic import ValidationError
from app.service.animal_service import Animal_service
from app.controller.schema.validation_animal_request import Update_animal_request
from http.client import CREATED, INTERNAL_SERVER_ERROR, NOT_FOUND, OK

def list_animal():
    try:
        animal_service = Animal_service()
        animals = animal_service.get_animals()

        return api_response(
            status_code = OK,
            message = 'getting animal list worked',
            data = animals
        )
    except Exception as e:
        return str(e), INTERNAL_SERVER_ERROR
    
def get_animal(animal_id):
    try:
        animal = Animal.query.get(animal_id)

        if Animal:
            return jsonify({
                "id" : animal.id,
                "name": animal.name,
                "birthdate": animal.birthdate
            }), OK
        return jsonify({'error': 'Animal not Found'}), NOT_FOUND
    except Exception as e:
        return str(e), INTERNAL_SERVER_ERROR

    
def update_animal(animal_id):
    try:
        data = request.json
        update_animal_request = Update_animal_request(**data)
        print(update_animal_request)

        animal = Animal()
        animal.name = update_animal_request.name
        animal.birthdate = update_animal_request.birthdate

        animal_service = Animal_service()
        animals = animal_service.update_animal(animal_id, animal)

        return api_response(
            status_code = OK,
            message = 'Animal update successful',
            data = animals
        )
    except ValidationError as e:
        return api_response(
            status_code = 400,
            message = e.errors(),
            data = {}
        )
    except Exception as e:
            return str(e), INTERNAL_SERVER_ERROR
    
def create_animal():
    try:
        data = request.json
        
        animal = Animal()
        animal.id = data ['id']
        animal.name = data['name']
        animal.birthdate = data['birthdate']
        db.session.add(animal)
        db.session.commit()

        return 'Animal created successful', CREATED
    except Exception as e:
        return str(e), INTERNAL_SERVER_ERROR
    
def search_animal():
    try:
        request_data = request.args
        animal_service = Animal_service()
        animals = animal_service.search_animal(request_data["name"])

        return api_response(
            status_code = OK,
            message = 'search animal worked',
            data = animals
        )
    except Exception as e:
        return str(e), INTERNAL_SERVER_ERROR
    
def delete_animal(animal_id):
    try:
        animal_service = Animal_service() 
        animal = animal_service.delete_animal(animal_id)

        if animal == "Animal not found":
            return api_response (
                status_code = 404,
                message = animal,
                data = "no data"
            )
        return api_response (
            status_code = 200,
            message = "deleted",
            data = animal
        )
    
    except Exception as e:
        return api_response (
            status_code = 500,
            message = str(e),
            data = {}
        )