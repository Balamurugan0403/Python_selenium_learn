import pytest
def test_sample_one():
    print("hai")
    
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
def test_sample():
    a="bala"
    b="balamurugan"
    assert a.__eq__(b)