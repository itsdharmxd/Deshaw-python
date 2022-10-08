import pytest


# fixtures are  like setup and teardown method run before and  after

@pytest.fixture()
def setup():
    print("i will execute first in common ")

    yield  # divider between setup and teardown section

    print('i will be last to execute')


@pytest.fixture(scope='class')   # Now this will run before  and  after  class execution
def setup_classLevel():
    print("i will execute first in common ")

    yield  # divider between setup and teardown section

    print('i will be last to execute')

@pytest.fixture()
def dataload():
    return ['dharmesh','upadhyay']


@pytest.fixture(params=['dharmesh','upadhyay','lalit'])
def multiparam(request):
    return request.param
