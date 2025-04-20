import requests
import os
import pandas as pd
import boto3

from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
from endpoint import get_paginated_new_releases

load_dotenv("./env", override=True)

CLIENT_ID = os.getenv("CLIENT_ID", "")
CLIENT_SECRET = os.getenv("CLIENT_SECRET", "")
AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME", "")

URL_TOKEN = "https://accounts.spotify.com/api/token"
URL_NEW_RELEASES = "https://api.spotify.com/v1/browse/new-releases"

def main():

    response = requests.post(URL_TOKEN, auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET), data={"grant_type": "client_credentials"})
    token = response.json().get("access_token")

    new_releases = get_paginated_new_releases(
            base_url=URL_NEW_RELEASES,
            access_token=token
    )

    print("New album releases have been extracted.")

    flattened_album_details = [
        {
            "album_id": album["id"],
            "album_name": album["name"],
            "release_date": album["release_date"],
            "album_spotify_url": album["external_urls"]["spotify"],
            "artist_id": artist["id"],
            "artist_name": artist["name"],
            "artist_spotify_url": artist["external_urls"]["spotify"],
        }
        for album in new_releases
        for artist in album.get("artists", [])
    ]

    csv_buffer = io.StringIO()
    df = pd.DataFrame(flattened_album_details)
    df.to_csv(csv_buffer, index=False, encoding="utf-8")
    print("Data successfully saved")

    s3 = boto3.client('s3')
    s3.put_object(Bucket=AWS_BUCKET_NAME, Key="album_details.csv", Body=csv_buffer.getvalue(), ContentType="text/csv")
    print("File successfully uploaded to S3 bucket as 'album_details_v1.csv'")

if __name__ == "__main__":
    main()
