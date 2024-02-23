from flask import Blueprint
from app.controller.animal_controller import (
    list_animal, 
    get_animal,
    update_animal,
    create_animal,
    search_animal,
    delete_animal
    )

animal_blueprint = Blueprint('animal_endpoint', __name__)

animal_blueprint.route("/", methods=['GET'])(list_animal)

animal_blueprint.route("/<int:animal_id>", methods=['GET'])(get_animal)

animal_blueprint.route("/<int:animal_id>", methods=['PUT'])(update_animal)

animal_blueprint.route("/", methods=['POST'])(create_animal)

animal_blueprint.route("/search", methods=['GET'])(search_animal)

animal_blueprint.route("/<int:animal_id>", methods=['DELETE'])(delete_animal)