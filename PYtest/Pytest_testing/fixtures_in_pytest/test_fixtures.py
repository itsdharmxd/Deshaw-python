import pytest


# fixtures are  like setup and teardown method run before and  after

@pytest.fixture()
def setup():
    print("i will execute first")

    yield  # divider between setup and teardown section

    print('i will be executed last')


def test_demo(setup):  # passing setup method to tell there is a fixtures
    print("Test is executing")
    assert 1==1