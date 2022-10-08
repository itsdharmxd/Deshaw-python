import pytest

@pytest.mark.usefixtures("setup_classLevel")   # before and  after class
# @pytest.mark.usefixtures("setup") # method level before and  after method
# pytest  will search for this method in conftest if  not found
class Test_ClassLevelFixtures:

    def test_demo1(self):
        print("Test is executing")

    def test_demo2(self):
        print("Test is executing")

    def test_demo3(self):
        print("Test is executing")

    def test_demo4(self):
        print("Test is executing")


