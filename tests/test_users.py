import pytest
from utils.api_client import APIClient

def test_get_users():
    """Test fetching users"""
    response = APIClient.get_users()
    assert response.status_code == 200
    assert "data" in response.json()

@pytest.mark.parametrize("name, job", [("John Doe", "QA Engineer"), ("Jane Doe", "Developer")])
def test_create_user(name, job):
    """Test creating a user"""
    response = APIClient.create_user(name, job)
    assert response.status_code == 201
    assert response.json()["name"] == name
    assert response.json()["job"] == job

def test_update_user():
    """Test updating user information"""
    user_id = 2
    response = APIClient.update_user(user_id, "John Updated", "Lead QA")
    assert response.status_code == 200
    assert response.json()["name"] == "John Updated"
    assert response.json()["job"] == "Lead QA"

def test_delete_user():
    """Test deleting a user"""
    user_id = 2
    response = APIClient.delete_user(user_id)
    assert response.status_code == 204
