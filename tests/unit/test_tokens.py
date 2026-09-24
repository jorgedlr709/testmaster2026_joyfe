import re

from app import generar_token


def test_generar_token_devuelve_32_caracteres_hexadecimales():
    assert re.fullmatch(r"[0-9a-f]{32}", generar_token())


def test_generar_token_es_distinto_en_dos_llamadas():
    assert generar_token() != generar_token()
