import os
import pytest
from dotenv import load_dotenv


def example_1():
    # load the .env file
    load_dotenv()
    # get api_key
    api_key = os.getenv("API_KEY")
    print("API_KEY:", api_key)


@pytest.mark.usefixtures('get_env_data')
def test_example_2():
    print('\n hello, world!')
    assert False


def test_example_3(get_env_data):
    name, password = get_env_data
    print('name:', name)
    print('password:', password)
    assert name == 'jackson'
    assert password == '123456'
