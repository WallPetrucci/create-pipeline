from calculadora import Calculadora

def test_que_calculadora_soma():
    calc = Calculadora()
    result = calc.soma(5, 5)
    assert result == 10
