import pytest


@pytest.mark.usefixtures('dataload')
def test_multiarg(dataload):
    print(dataload)