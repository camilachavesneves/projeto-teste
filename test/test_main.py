import pytest
from unittest.mock import patch
from src.main import root, funcaoteste, create_estudante, update_estudante, delete_estudante, Estudante

@pytest.mark.asyncio
async def test_root():
    result = await root()
    # CORREÇÃO 1: Removido 'yield result' (generators quebram asserções em testes simples)
    assert result == {"message": "Hello World"}


@pytest.mark.asyncio
async def test_funcaoteste():
    with patch('random.randint', return_value=12345):
        result = await funcaoteste()

    # CORREÇÃO 2: 'result' já é um dicionário, não uma função (removido parênteses de result())
    assert result == {"teste": True, "num_aleatorio": 12345}


@pytest.mark.asyncio
async def test_create_estudante():
    # CORREÇÃO 3: O parâmetro correto na Pydantic do main.py é 'nome', e não 'name'
    estudante_teste = Estudante(nome="Fulano", curso="Curso 1", ativo=False)
    result = await create_estudante(estudante_teste)
    assert estudante_teste == result


@pytest.mark.asyncio
async def test_update_estudante_negativo():
    result = await update_estudante(-5)
    assert not result


@pytest.mark.asyncio
async def test_update_estudante_positivo():
    result = await update_estudante(10)
    assert result


@pytest.mark.asyncio
async def test_delete_estudante_negativo():
    result = await delete_estudante(-5)
    assert not result


@pytest.mark.asyncio
async def test_delete_estudante_positivo():
    result = await delete_estudante(5)
    assert result