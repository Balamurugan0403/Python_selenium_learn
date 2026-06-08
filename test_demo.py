import sys
import pytest
@pytest.mark.smoke
def test_sample_one():
    print("hai")
@pytest.mark.bala
def test_sample_two():
    print("hai2")
def test_sample_three():
    print("hai3")
def test_simple_assertion():
    assert (1+2) == 4
def test_equal_assertion():
    x=5
    y=5
    assert x!=y
def test_in_assertion():
    numbers=[2,4,5,7,9]
    assert 5 in numbers
def test_in_assertion():
    numbers=["apple","orange","grapes",7,9]
    assert "orange" not in numbers
@pytest.mark.skip(reason="no need of this method now")
def test_sample():
    a="bala"
    b="bala"
    assert a.__eq__(b)
    
@pytest.mark.skipif(sys.version_info<(3,8),reason="requires python 3.8")
def test_add():
    a=6
    b=7
    print(a+b)
    
@pytest.mark.xfail(reason="expexted to fail until we fix the bug")
def test_example_xfail():
    assert 2*3==7
def test_example2_xfail():
    assert 2*3==6
@pytest.mark.parametrize("test_input,expected",[(1,3),(3,6),(5,7)])
def test_addition(test_input,expected):
    assert test_input+2==expected
    
