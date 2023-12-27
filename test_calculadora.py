from calculadora import Calculadora

def test_que_calculadora_soma():
    calc = Calculadora()
    result = calc.soma(5, 5)
    assert result == 10

def test_que_calculadora_subtrai():
    calc = Calculadora()
    result = calc.subtrai(10, 5)
    assert result == 5

def test_que_calculadora_divisao():
    calc = Calculadora()
    result = calc.divisao(10, 2)
    assert result == 5

def test_env_var():
    calc = Calculadora()
    result = calc.get_env_var()
    assert result == "Minha ENV_VAR"
