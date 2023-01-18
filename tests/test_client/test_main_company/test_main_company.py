import json


def test_list_main_company(client, admin_header):
    req = client.get('/v1/admin/main', headers=admin_header)
    res = req.get_json()

    assert req.status_code == 200

    assert 'id' in res['data']
    assert 'name' in res['data']
    assert 'email' in res['data']
    assert 'cell_phone' in res['data']
    assert 'landline' in res['data']
    assert 'status' in res['data']
    assert 'ein' in res['data']
    assert 'facebook' in res['data']
    assert 'instagram' in res['data']
    assert 'app_android' in res['data']
    assert 'app_ios' in res['data']
    assert 'address' in res['data']

    assert type(res['data']['id']) == int
    assert type(res['data']['name']) in (str, type(None))
    assert type(res['data']['email']) in (str, type(None))
    assert type(res['data']['cell_phone']) in (str, type(None))
    assert type(res['data']['landline']) in (str, type(None))
    assert type(res['data']['status']) in (bool, type(None))
    assert type(res['data']['ein']) in (str, type(None))
    assert type(res['data']['facebook']) in (str, type(None))
    assert type(res['data']['instagram']) in (str, type(None))
    assert type(res['data']['app_android']) in (str, type(None))
    assert type(res['data']['app_ios']) in (str, type(None))
    assert type(res['data']['address']) in (object, type(None))


def test_put_main_company(client, admin_header):
    payload = {
        "name": "Test Company",
        "email": "maincompany@email.com",
        "cell_phone": "62999999999",
        "landline": "teste",
        "status": True,
        "ein": "teste",
        "company_name": "Main Company",
        "facebook": "@maincompany",
        "instagram": "@maincompany",
        "app_android": "@maincompany",
        "app_ios": "@maincompany"
    }
    req = client.put('/v1/admin/main', headers=admin_header,
                     data=json.dumps(payload), content_type='application/json')
    res = req.get_json()

    assert req.status_code == 200

    assert 'id' in res['data']
    assert 'name' in res['data']
    assert 'email' in res['data']
    assert 'cell_phone' in res['data']
    assert 'landline' in res['data']
    assert 'status' in res['data']
    assert 'ein' in res['data']
    assert 'facebook' in res['data']
    assert 'instagram' in res['data']
    assert 'app_android' in res['data']
    assert 'app_ios' in res['data']
    assert 'address' in res['data']

    assert type(res['data']['id']) == int
    assert type(res['data']['name']) in (str, type(None))
    assert type(res['data']['email']) in (str, type(None))
    assert type(res['data']['cell_phone']) in (str, type(None))
    assert type(res['data']['landline']) in (str, type(None))
    assert type(res['data']['status']) in (bool, type(None))
    assert type(res['data']['ein']) in (str, type(None))
    assert type(res['data']['facebook']) in (str, type(None))
    assert type(res['data']['instagram']) in (str, type(None))
    assert type(res['data']['app_android']) in (str, type(None))
    assert type(res['data']['app_ios']) in (str, type(None))
    assert type(res['data']['address']) in (object, type(None))
