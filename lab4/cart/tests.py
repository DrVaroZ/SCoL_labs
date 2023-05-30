import requests


def test_7():
    url = 'http://127.0.0.1:8000/cart/'
    response = requests.get(url)
    assert response.status_code == 403
