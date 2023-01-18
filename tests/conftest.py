
import json

import pytest
from faker import Factory
from sqlalchemy import create_engine

from app import create_app


@pytest.fixture()
def app():
    app = create_app()
    return app


@pytest.fixture()
def conn(config):
    database = config['SQLALCHEMY_DATABASE_URI']
    conn = create_engine(f'{database}')
    print(database)

    return conn


@pytest.fixture()
def client_token(client):
    headers = {
        'Content-Type': "application/json",
        'Authorization': "NDRleHByZXNzYWRtaW46NDRleHByZXNzcGFzc3dvcmQ="
    }
    data = {
        "username": "clientuser@thinkidea.app",
        "password": "123456",
        "grant_type": "password"
    }
    url = "/auth/token"
    response = client.post(url, data=json.dumps(data), headers=headers)
    response_body = response.get_json()

    if response.status_code == 401:
        raise KeyError('Usuário ou senha inválida')

    return response_body['access_token']


@pytest.fixture()
def admin_token(client):
    headers = {
        'Content-Type': "application/json",
        'Authorization': "b2ZlcnRhcGxheXVzZXI6b2ZlcnRhcGxheXBhc3N3b3Jk"
    }
    data = {
        "username": "adminuser@thinkidea.app",
        "password": "123456",
        "grant_type": "password"
    }
    url = "/auth/token"
    response = client.post(url, data=json.dumps(data), headers=headers)
    response_body = response.get_json()

    if response.status_code == 401:
        raise KeyError('Usuário ou senha inválida')

    return response_body['access_token']


@pytest.fixture()
def client_header(client_token):
    headers = {
        'Content-Type': "application/json",
        'Authorization': f"Bearer {client_token}"
    }

    return headers


@pytest.fixture()
def admin_header(admin_token):
    headers = {
        'Content-Type': "application/json",
        'Authorization': f"Bearer {admin_token}"
    }

    return headers


@pytest.fixture()
def faker():
    return Factory.create('pt_BR')


@pytest.fixture()
def create_user(client, admin_header, faker):
    data = {
        "name": faker.name(),
        "cell_phone": faker.phone_number(),
        "email": faker.email(),
        "password": "123456",
        "group": {"id": 5}
    }

    create_request = client.post(
        "/v1/admin/users", headers=admin_header, data=json.dumps(data))
    return create_request.get_json()
