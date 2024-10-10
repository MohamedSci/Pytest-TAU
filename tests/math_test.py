import pytest

def test_one_plus_one():
    assert 1+1 == 2

# Handlinig Exception
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num= 1/0
        assert "division by zero" in str(e.value)    



#  Parameterization and Data test driven DDT
inputData = [
(-1,-1,1),
(1,1,1),
(-1,1,-1),
(-1,0,0),
(0,1,0)
]     
@pytest.mark.parametrize("a,b,c",inputData)
def test_mutliplication(a,b,c):
    a*b==c