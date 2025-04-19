import requests

def get_paginated_new_releases(base_url: str, access_token: str) -> list:

    headers = {"Authorization": f"Bearer {access_token}"}
    request_url = base_url
    new_releases_data = []

    while request_url:
        response = requests.get(url=request_url, headers=headers)

        # Check for request success
        if response.status_code != 200:
            print(f"Error: Status code {response.status_code}")
            break

        response_json = response.json()
        new_releases_data.extend(response_json.get("albums", {}).get("items", []))
        request_url = response_json.get("albums", {}).get("next")  # Move to next page

    return new_releases_data
