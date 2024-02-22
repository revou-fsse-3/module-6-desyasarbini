from app.service.animal_service import Animal_service
from app import db

# def test_get_animal(test_app, mocker):
#     # Arrange
#     mock_animal_data = [
#         {
#             "id" : 1,
#             "name" : 'lion',
#             "birthdate" : 2312
#         },
#     ]
#     mocker.patch.object(Animal_service, "get_animals", return_value = mock_animal_data)

#     # Act
#     with test_app.test_client() as client:
#         response = client.get('/v1/animal')

#     # Assert
#     assert response.status_code == 200
#     assert len(response.json["data"]) == len(mock_animal_data)
#     assert response.json['data'] == mock_animal_data

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