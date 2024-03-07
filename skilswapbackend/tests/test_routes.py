"""testing routes."""


from skilswapbackend.main import app


def test_index_route() -> None:
    """Test the index route to ensure it returns a 200 status code."""
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
