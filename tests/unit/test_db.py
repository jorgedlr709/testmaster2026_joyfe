import sqlite3

import pytest

from app import init_db


def test_init_db_crea_todas_las_tablas(db_path):
    init_db(db_path)
    with sqlite3.connect(db_path) as connection:
        tables = {row[0] for row in connection.execute("SELECT name FROM sqlite_master WHERE type = 'table'")}
    assert {"usuarios", "tokens", "productos", "clientes"}.issubset(tables)


def test_init_db_se_puede_ejecutar_varias_veces(db_path):
    init_db(db_path)
    init_db(db_path)
    with sqlite3.connect(db_path) as connection:
        connection.execute("INSERT INTO usuarios (username, password_hash) VALUES (?, ?)", ("ana", "hash"))
        with pytest.raises(sqlite3.IntegrityError):
            connection.execute("INSERT INTO usuarios (username, password_hash) VALUES (?, ?)", ("ana", "otro-hash"))
