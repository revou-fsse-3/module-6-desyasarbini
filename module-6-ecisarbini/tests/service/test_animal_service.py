from app.models.animal import Animal
from app.service.animal_service import Animal_service
from app.repositories.animal_repo import Animal_repo

def test_get_list_animal_success(test_app, mocker):
    """service get animal success"""
    
    # Arrange
    mock_animal_data = [
        Animal(id=1, name='Bear', birthdate= 1213),
        Animal(id=2, name='Dolphin', birthdate= 1213),
    ]
    mocker.patch.object(Animal_repo, 'get_list_animal', return_value = mock_animal_data)

    # Act
    with test_app.test_request_context():
        animal_service = Animal_service().get_animals()

    print(animal_service)

    # Assert 
    assert len(animal_service) == 2
    assert animal_service[0]["name"] == 'Bear'
    assert animal_service[1]["birthdate"] == 1213