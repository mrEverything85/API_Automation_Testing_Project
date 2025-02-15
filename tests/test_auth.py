import pytest
from utils.api_client import APIClient

# ✅ Test successful login
def test_successful_login():
    """Test login with valid credentials."""
    response = APIClient.login("eve.holt@reqres.in", "cityslicka")
    assert response.status_code == 200, "Login failed!"
    assert "token" in response.json(), "Token not received!"

# ✅ Test failed login with missing password
def test_failed_login():
    """Test login with missing password."""
    response = APIClient.login("eve.holt@reqres.in", "")
    assert response.status_code == 400, "Expected failure but got success!"
    assert response.json()["error"] == "Missing password"

# ✅ Test successful registration
def test_successful_register():
    """Test user registration with valid credentials."""
    response = APIClient.register("eve.holt@reqres.in", "pistol")
    assert response.status_code == 200, "Registration failed!"
    assert "token" in response.json(), "Token not received!"

# ✅ Test failed registration with missing password
def test_failed_register():
    """Test registration failure due to missing password."""
    response = APIClient.register("eve.holt@reqres.in", "")
    assert response.status_code == 400, "Expected failure but got success!"
    assert response.json()["error"] == "Missing password"
