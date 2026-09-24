import sqlite3


def test_producto_se_guarda_en_sqlite(client, auth_headers, db_path):
    response = client.post("/productos", headers=auth_headers, json={"nombre": "Raton", "precio": 12.5, "stock": 8})
    assert response.status_code == 201
    with sqlite3.connect(db_path) as connection:
        row = connection.execute("SELECT nombre, precio, stock FROM productos WHERE id = ?", (response.get_json()["id"],)).fetchone()
    assert row == ("Raton", 12.5, 8)
