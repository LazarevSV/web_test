import pytest
import yaml
import requests

with open("config.yaml", "r") as f:
    data = yaml.safe_load(f)

@pytest.fixture()
def login():
    res1 = requests.post(data["address_1"], data={"username": data["username"], "password": data["password"]})
    return res1.json()["token"]

@pytest.fixture()
def find_id():
    return 99432

@pytest.fixture()
def title():
    return "Writer"

@pytest.fixture()
def description():
    return "Pushkin"

@pytest.fixture()
def content():
    return "A.S.Pushkin"

@pytest.fixture()
def find_description():
    return "Pushkin"