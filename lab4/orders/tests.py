import requests


def test_8():
    url = 'http://127.0.0.1:8000/orders/create/'
    response = requests.get(url)
    assert response.status_code == 403
