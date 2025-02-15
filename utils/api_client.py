import requests

BASE_URL = "https://reqres.in/api"

class APIClient:
    @staticmethod
    def get_users(page=1):
        """Fetches a list of users from ReqRes API."""
        response = requests.get(f"{BASE_URL}/users", params={"page": page})
        return response

    @staticmethod
    def create_user(name, job):
        """Creates a new user."""
        payload = {"name": name, "job": job}
        response = requests.post(f"{BASE_URL}/users", json=payload)
        return response

    @staticmethod
    def update_user(user_id, name, job):
        """Updates user information."""
        payload = {"name": name, "job": job}
        response = requests.put(f"{BASE_URL}/users/{user_id}", json=payload)
        return response

    @staticmethod
    def delete_user(user_id):
        """Deletes a user."""
        response = requests.delete(f"{BASE_URL}/users/{user_id}")
        return response

    @staticmethod
    def login(email, password):
        """Logs in a user with the given credentials."""
        payload = {"email": email, "password": password}
        response = requests.post(f"{BASE_URL}/login", json=payload)
        return response

    @staticmethod
    def register(email, password):
        """Registers a new user."""
        payload = {"email": email, "password": password}
        response = requests.post(f"{BASE_URL}/register", json=payload)
        return response