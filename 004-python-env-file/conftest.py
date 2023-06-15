import os

import pytest
from dotenv import load_dotenv, find_dotenv


@pytest.fixture()
def get_env_data():
    # find the path of the .env.bate file
    dotenv_path = find_dotenv('.env.beta')
    # load the .env file
    load_dotenv(dotenv_path=dotenv_path)

    user_name = os.getenv('USER_NAME')
    user_password = os.getenv('USER_PASSWORD')

    print('\nconftest.py:', user_name, user_password)

    return user_name, user_password


if __name__ == "__main__":
    name, password = get_env_data()
    print(name, password)
