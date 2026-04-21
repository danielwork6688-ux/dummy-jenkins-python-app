from app import create_app


def test_health_endpoint_returns_ok():
    client = create_app().test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_greet_endpoint_uses_name():
    client = create_app().test_client()

    response = client.get("/api/greet?name=Jenkins")

    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, Jenkins!"}


def test_greet_endpoint_uses_default_for_blank_name():
    client = create_app().test_client()

    response = client.get("/api/greet?name=   ")

    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, DevOps learner!"}
