from app.service.animal_service import Animal_service
from app import db

def test_get_animal(test_app):
    response = test_app.get("/v1/animal/")
    print(response.json['data'])
    assert len(response.json['data'])  == 6

def test_put_animal(test_app):
    data = {
        "name" : "lion",
        "birthdate" : 2312
    }
    response = test_app.put("/v1/animal/2", json=data)
    print(response.json)
    assert response.status_code == 200

def test_put_animal_400(test_app):
    data = {}
    response = test_app.put("/v1/animal/2", json=data)
    print(response.json)
    assert response.status_code == 400 

def test_delete_animal_not_found(test_app, mocker):
    #Arrange
    expected_response = "Animal not found"
    mocker.patch.object(Animal_service, 'delete_animal', return_value = expected_response)

    with test_app.test_client() as client:
        #Act
        response = client.delete("/v1/animal/2")

    # Assert
    assert response.status_code == 404
    assert response.json['data'] == "no data"