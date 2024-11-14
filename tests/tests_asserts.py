import pytest

def test_addition():
    result = 1 + 1
    assert result == 2 # Verifica que el resultado sea 2


def test_list():
    my_list = [1, 2, 3]
    assert 2 in my_list  # Verifica que 2 esté en la lista
    assert 4 not in my_list  # Verifica que 4 no esté en la lista


def test_string():
    my_string = "Hello, world!"
    assert "Hello" in my_string  # Verifica que 'Hello' esté en la cadena
    assert "hello" not in my_string  # Verifica que 'hello' no esté en la cadena


def test_dict():
    my_dict = {'player': 'Ronaldo'}
    assert my_dict.get('player') == 'Ronaldo'  # Verifica que el valor de la clave sea 'value'


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0  # Verifica que la excepción ZeroDivisionError se lance

def test_float_comparison():
    result = 0.1 + 0.2
    assert result == pytest.approx(0.3, rel=1e-9)  # Compara números flotantes con un margen de error


def test_string_error():
    my_string = "Error: Something went wrong"
    assert "Error" in my_string  # Verifica si "Error" está en la cadena
    with pytest.raises(ValueError, match="Something went wrong"):
        raise ValueError("Something went wrong")  # Verifica que el mensaje de la excepción coincida

def test_value_error():
    with pytest.raises(ValueError):
        int('o8r')