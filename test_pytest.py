import requests


def test_response():
    resp = requests.get("https://www.baidu.com")
    assert resp.status_code == 200
