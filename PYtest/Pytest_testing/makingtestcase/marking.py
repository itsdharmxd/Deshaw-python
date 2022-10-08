# any pytest file start with test_  or end  with _test
import pytest


# any function start with test_

@pytest.mark.sanity
def test_firstProgram():
    assert 1==2

@pytest.mark.regression
def test_secondProgram():
    assert 1==2
@pytest.mark.dharmesh
def test_thirdProgram():
    assert 1 == 2

@pytest.mark.upadhyay
def test_fourthProgram():
    assert 1 == 2



