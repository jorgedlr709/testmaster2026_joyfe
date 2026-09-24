import pytest

from app import validar_cliente, validar_producto, validar_registro


@pytest.mark.parametrize(
    ("data", "expected"),
    [
        ({"username": "ana", "password": "1234"}, None),
        (None, "Cuerpo de la peticion invalido"),
        ({"password": "1234"}, "El campo username es obligatorio"),
        ({"username": "ana", "password": "123"}, "El campo password debe tener al menos 4 caracteres"),
    ],
)
def test_validar_registro(data, expected):
    assert validar_registro(data) == expected


@pytest.mark.parametrize(
    ("data", "expected"),
    [
        ({"nombre": "Teclado", "precio": 19.99, "stock": 3}, None),
        ({"precio": 1, "stock": 1}, "El campo nombre es obligatorio"),
        ({"nombre": "Teclado", "precio": -1, "stock": 1}, "El campo precio debe ser un numero >= 0"),
        ({"nombre": "Teclado", "precio": True, "stock": 1}, "El campo precio debe ser un numero >= 0"),
        ({"nombre": "Teclado", "precio": 1, "stock": 1.5}, "El campo stock debe ser un entero >= 0"),
    ],
)
def test_validar_producto(data, expected):
    assert validar_producto(data) == expected


@pytest.mark.parametrize(
    ("data", "expected"),
    [
        ({"nombre": "Ana", "email": "ana@example.com"}, None),
        ({"email": "ana@example.com"}, "El campo nombre es obligatorio"),
        ({"nombre": "Ana", "email": "incorrecto"}, "El campo email no es valido"),
    ],
)
def test_validar_cliente(data, expected):
    assert validar_cliente(data) == expected
