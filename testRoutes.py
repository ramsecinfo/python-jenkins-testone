from app import *

def test_Home():
    response = app.test_client().get('/')
    assert b"Welcome to Jenkins CI/CD Pipeline for Python Application" in response.data
    assert response.status_code == 200