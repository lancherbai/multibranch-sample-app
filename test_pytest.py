import requests


def test_response():
    resp = requests.get("http://127.0.0.1:80")
    assert resp.status_code == 200
