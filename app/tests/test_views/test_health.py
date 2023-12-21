def test_healthcheck(client):
    response = client.get("/health")

    assert "It's working!" in response.text
    assert "/static/css/tailwind-output.css" in response.text
    assert "/static/js/htmx.min.js" in response.text
    assert response.status_code == 200
