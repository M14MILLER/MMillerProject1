import requests
import secrets


def get_data(url:str):
    all_data = []
    api_url = f"{url}&api_key={secrets.api_key}"
    