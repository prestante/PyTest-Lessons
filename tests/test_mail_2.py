import pytest
import time

@pytest.fixture
def set_up():
    print("\nNo login required")

def test_sending_mail_1(set_up, set_up_file, set_up_function):
    time.sleep(2)
    print("The mail 1 has been sent")

def test_sending_mail_2(set_up, set_up_file, set_up_function):
    raise Exception("This is an intentional error!")
    print("The mail 2 has been sent")