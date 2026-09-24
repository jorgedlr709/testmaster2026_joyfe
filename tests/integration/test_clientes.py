def test_crud_completo_de_clientes(client, auth_headers):
    created = client.post("/clientes", headers=auth_headers, json={"nombre": "Ana", "email": "ana@example.com"})
    assert created.status_code == 201
    client_id = created.get_json()["id"]
    assert created.get_json()["telefono"] == ""
    assert client.get("/clientes", headers=auth_headers).get_json()[0]["email"] == "ana@example.com"
    updated = client.put(f"/clientes/{client_id}", headers=auth_headers, json={"nombre": "Ana Perez", "email": "ana.perez@example.com", "telefono": "600000000"})
    assert updated.status_code == 200
    assert updated.get_json()["nombre"] == "Ana Perez"
    assert client.delete(f"/clientes/{client_id}", headers=auth_headers).status_code == 204
    assert client.get(f"/clientes/{client_id}", headers=auth_headers).status_code == 404


def test_cliente_con_email_invalido(client, auth_headers):
    response = client.post("/clientes", headers=auth_headers, json={"nombre": "Ana", "email": "sin-arroba"})
    assert response.status_code == 400
