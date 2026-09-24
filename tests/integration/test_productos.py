def test_crud_completo_de_productos(client, auth_headers):
    created = client.post("/productos", headers=auth_headers, json={"nombre": "Teclado", "precio": 19.99, "stock": 5})
    assert created.status_code == 201
    product_id = created.get_json()["id"]
    assert client.get("/productos", headers=auth_headers).get_json()[0]["nombre"] == "Teclado"
    updated = client.put(f"/productos/{product_id}", headers=auth_headers, json={"nombre": "Teclado mecanico", "precio": 29.99, "stock": 2})
    assert updated.status_code == 200
    assert updated.get_json()["stock"] == 2
    assert client.delete(f"/productos/{product_id}", headers=auth_headers).status_code == 204
    assert client.get(f"/productos/{product_id}", headers=auth_headers).status_code == 404


def test_producto_con_datos_invalidos(client, auth_headers):
    response = client.post("/productos", headers=auth_headers, json={"nombre": "Teclado", "precio": -1, "stock": 1})
    assert response.status_code == 400
