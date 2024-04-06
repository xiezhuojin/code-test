def test_route_not_found(client):
    response = client.get("/apidocs")

    assert response.status_code != 200