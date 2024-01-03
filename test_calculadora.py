from calculadora import Calculadora

def test_que_calculadora_soma():
    calc = Calculadora()
    result = calc.soma(5, 2)
    assert result == 7

def test_que_calculadora_subtrai():
    calc = Calculadora()
    result = calc.subtrai(10, 5)
    assert result == 5

def test_que_calculadora_divisao():
    calc = Calculadora()
    result = calc.divisao(6, 2)
    assert result == 3
    result = calc.divisao(8, 4)
    assert result == 2

# def test_env_var():
#     calc = Calculadora()
#     result = calc.get_env_var()
#     assert result == "Minha ENV_VAR"
