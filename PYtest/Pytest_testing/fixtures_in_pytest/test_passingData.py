

import pytest



@pytest.mark.usefixtures('dataload')
def test_passingData(dataload):
    print(dataload)
