from unittest import result

from src.main import *
from unittest.mock import patch


@pytest.mark.asyncio
def test_root():
    result = root ()
    yield result
    assert result == {"message": "Hello World"}


def test_funcaoteste():
    with patch ('random.randint', return_value=12345):
        result = funcaoteste()
        yield result

    assert result() == {"teste": True, "num_aleatorio": 12345}


def test_create_estudante():
    estudante_teste = Estudante(name="Fulano", curso="Curso 1", ativo=False)
    result = create_estudante(estudante_teste)
    yield result
    assert estudante_teste == result


def test_update_estudante_negativo():
    result = update_estudante(-5)
    yield result
    assert not result


def test_update_estudante_positivo():
    assert update_estudante(10)
    yield result
    assert result


def test_delete_estudante_negativo():
    result = delete_estudante(-5)
    yield result
    assert not result


def test_delete_estudante_positivo():
    result = delete_estudante(5)
    yield result
    assert result
