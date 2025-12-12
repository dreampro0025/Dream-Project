import requests

BASE_URL = "https://colleges-api.onrender.com/colleges"

def get_states():
    response = requests.get(f"{BASE_URL}/states")
    return response.json()

def get_districts(state):
    response = requests.get(f"{BASE_URL}/{state}/districts")
    return response.json()

def get_colleges_by_state(state):
    response = requests.get(f"{BASE_URL}/{state}")
    return response.json()

def get_colleges_by_state_district(state, district):
    response = requests.get(f"{BASE_URL}/{state}/{district}")
    return response.json()