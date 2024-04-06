import json


def test_get_current_weather(client):
    response = client.get("/weather/?city=beijing")
    data = json.loads(response.data)

    assert response.status_code == 200
    assert "message" not in data