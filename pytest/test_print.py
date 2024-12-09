import pytest

def test_helloworld():
    print("\nHELLO,WORLD")
    assert 1 == 1
    pytest.assume(1 + 1 == 2)
    print("HELLO,WORLD")

def test_failure():
    return False     #不会因为返回值是False就判断case为failed，依然为passed
    
def test_failure1():
    assert False 

def test_failure2():
    pytest.assume(False) 

def test_failure3():
    raise ValueError("Something went wrong")  #抛异常

def test_explicit_fail():
    pytest.fail("This test failed explicitly")
    #pytest.fail(reason="test fail", pytrace=True)

if __name__ == "__main__":
    pytest.main(["-vs", "test_print.py"]) 
    print("hello,world!!!")     
