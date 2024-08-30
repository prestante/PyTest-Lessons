import pytest

@pytest.fixture()
def set_up():
    print("\nIn")
    yield
    print("\nOut")

@pytest.fixture(scope="function")
def set_up_function():
    print("\nFunc in")
    yield
    print("\nFunc out")

@pytest.fixture(scope="module")
def set_up_file():
    print("\nFile in")
    yield
    print("\nFile out")

