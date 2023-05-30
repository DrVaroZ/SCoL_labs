import requests


def test_home_page():  # Get the home page
    url = 'http://127.0.0.1:8000/'
    response = requests.get(url)
    assert response.status_code == 200


def test_detail_page():  # Get the home page
    url = 'http://127.0.0.1:8000/2'
    response = requests.get(url)
    assert response.status_code == 200


def test_ford_page():  # Get the home page
    url = 'http://127.0.0.1:8000/Ford'
    response = requests.get(url)
    assert response.status_code == 200


def test_ferrari_page():  # Get the home page
    url = 'http://127.0.0.1:8000/Ferrari'
    response = requests.get(url)
    assert response.status_code == 200


def test_1():
    url = 'http://127.0.0.1:8000/?sort=ascending'
    response = requests.get(url)
    assert response.status_code == 200


def test_2():
    url = 'http://127.0.0.1:8000/?sort=descending'
    response = requests.get(url)
    assert response.status_code == 200


def test_3():
    url = 'http://127.0.0.1:8000/Ford/?sort=descending'
    response = requests.get(url)
    assert response.status_code == 200


def test_4():
    url = 'http://127.0.0.1:8000/Ford/?sort=ascending'
    response = requests.get(url)
    assert response.status_code == 200


def test_5():
    url = 'http://127.0.0.1:8000/Ferrari/?sort=descending'
    response = requests.get(url)
    assert response.status_code == 200


def test_6():
    url = 'http://127.0.0.1:8000/Ferrari/?sort=ascending'
    response = requests.get(url)
    assert response.status_code == 200


def test_7():
    url = 'http://127.0.0.1:8000/edit/3/'
    response = requests.get(url)
    assert response.status_code == 403
