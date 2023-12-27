from calculadora import Calculadora

def test_que_calculadora_soma():
    calc = Calculadora()
    result = calc.soma(5, 5)
    assert result == 10

def test_que_calculadora_subtrai():
    calc = Calculadora()
    result = calc.subtrai(10, 5)
    assert result == 5
