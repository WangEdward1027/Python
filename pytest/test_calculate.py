import pytest

#def test_divide():
def divide():
    assert 4 % 2 == 3

def test_multiply():
    print("run test_multiply()")
    assert 1 * 3 == 3
    
def test_exit():
    #assert 1 + 1 == 3
    pytest.assume(1 + 1 == 2)     #pytest.assume() :断言，但继续执行完该测试函数
    print(111)
    print(222)
    pytest.exit("exit reason")   #pytest.exit() :退出，不执行后续测试用例。且不计算本次测试用例
    print(333)

@pytest.mark.parametrize("x, y, result", [(1,2,3),(10,20,30),(100,200,300)])
def test_addition(x, y, result):
    assert x + y == result

#@pytest.mark.parametrize("a,b,c",[(10,6,4),(100,90,10)])
@pytest.mark.parametrize("a, b, c", [pytest.param(10, 6, 4, id="test_case_4"), pytest.param(100, 90, 10, id="test_case_5")])
def test_subtraction(a, b, c):
    assert 3 - 2 == 1
    assert a - b == c
