import json


def test_route_not_found(client):
    response = client.get("/route-not-exist")
    data = json.loads(response.data)

    assert response.status_code != 200
    assert "error" in data