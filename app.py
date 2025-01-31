import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
NOTION_TOKEN = os.getenv("NOTION_API")


class NotionAPI:

    def __init__(self, token):
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {NOTION_TOKEN}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json",
        }

    def list_all_databases(self) -> list:

        url = "https://api.notion.com/v1/search"
        payload = {"filter": {"value": "database", "property": "object"}}
        response = requests.post(url, headers=self.headers, json=payload)
        ids = self.get_all_database_id(response.json()["results"])
        return ids

    def get_database_id(self, results: list) -> list:
        id = []
        for result in results:
            id.append(result["id"])
        return id

    def get_database_info(self, database_id: str) -> dict:
        url = f"https://api.notion.com/v1/databases/{database_id}"
        response = requests.get(url, headers=self.headers)
        return response.json()
