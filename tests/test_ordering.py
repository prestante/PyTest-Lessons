import pytest

@pytest.mark.run(order=40)
def test_fun_1():
    print("Function1")

@pytest.mark.run(order=5)
def test_fun_2():
    print("Function2")

@pytest.mark.run(order=2)
def test_fun_3():
    print("Function3")