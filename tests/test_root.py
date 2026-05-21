def test_root_redirect(client):
    # Arrange
    # (No special setup needed)

    # Act
    response = client.get("/")

    # Assert
    assert response.status_code in (307, 302)  # FastAPI may use 307 or 302
    assert "/static/index.html" in response.headers["location"]
