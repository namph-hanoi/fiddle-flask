
from app.models import UserModel

# def test_home(client):
#     response = client.get("/")
#     assert b"<title>Home</title>" in response.data

_json_data = {
    "email": "test@test.com", "password": "testpassword", "username": "test"}

def _register_user(client):
    return client.post("/user/register", json=_json_data, content_type='application/json')


def test_registration(client, app):
    _register_user(client)

    with app.app_context():
        assert UserModel.query.count() == 1
        assert UserModel.query.first().email == _json_data['email']

def test_invalid_login(client, app):
    _register_user(client)

    with app.app_context():
        response = client.post("/user/login", json={
            "username": _json_data['username'], "password": _json_data['password']})
        assert UserModel.query.count() == 1
        assert response.status_code == 200


def test_invalid_login(client):
    response = client.post("/login", data={"email": "test2@test.com", "password": "asdfsadf"})
    assert response.status_code == 404