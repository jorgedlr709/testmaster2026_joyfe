def test_registro_correcto(client):
    response = client.post("/registro", json={"username": "ana", "password": "secreto"})
    assert response.status_code == 201
    assert response.get_json()["mensaje"] == "Usuario creado correctamente"


def test_registro_duplicado(client):
    payload = {"username": "ana", "password": "secreto"}
    client.post("/registro", json=payload)
    assert client.post("/registro", json=payload).status_code == 409


def test_login_correcto_devuelve_token(client):
    client.post("/registro", json={"username": "ana", "password": "secreto"})
    response = client.post("/login", json={"username": "ana", "password": "secreto"})
    assert response.status_code == 200
    assert response.get_json()["token"]


def test_login_con_credenciales_incorrectas(client):
    client.post("/registro", json={"username": "ana", "password": "secreto"})
    assert client.post("/login", json={"username": "ana", "password": "incorrecta"}).status_code == 401


def test_ruta_protegida_rechaza_token_ausente_o_invalido(client):
    assert client.get("/productos").status_code == 401
    assert client.get("/productos", headers={"Authorization": "Bearer falso"}).status_code == 401
