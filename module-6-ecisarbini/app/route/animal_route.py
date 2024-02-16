from flask import Blueprint, jsonify
from app.utils.database import db
from app.models.animal import Animal

animal_blueprint = Blueprint('animal_endpoint', __name__)

@animal_blueprint.route("/", methods=['GET'])
def get_animal():
    return jsonify()

@animal_blueprint.route("/", methods=['POST'])
def create_animal():
    animal = Animal()
    animal.name = 'gajah'
    animal.birthday = 12-12-1997
    db.session.add(animal)
    db.session.commit()
    return
