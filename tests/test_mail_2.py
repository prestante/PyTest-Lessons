import pytest
import time

@pytest.fixture
def set_up():
    print("\nNo login required")

def test_sending_mail_1(set_up):
    raise Exception("This is an intentional error!")
    print("The mail 1 has been sent")

def test_sending_mail_2(set_up):
    time.sleep(2)
    print("The mail 2 has been sent")