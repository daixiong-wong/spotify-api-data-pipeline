# Batch Data Processing Using Spotify API

## Overview
This project demonstrates batch data processing by interacting with the Spotify API to extract and save information about new album releases. It includes functionality for API authentication, paginated data retrieval, and data storage in AWS S3 buckets.

## Scripts
1. **authentication.py**: Contains the `get_token` function to authenticate with the Spotify API and retrieve an access token.
2. **endpoint.py**: Contains the `get_paginated_new_releases` function to fetch details of new album releases in a paginated format.
3. **main.py**: The main script orchestrates the API call, extracts album details, and stores the processed data in an S3 bucket.

## Features
- Authentication with Spotify's API.
- Programmatic handling of paginated API responses for large datasets.
- Automated creation of an S3 bucket and storage of album details in CSV format.

## Getting Started
1. **Prerequisites**:
   - Python 3.x
   - Spotify Developer Account (API Key required)
   - AWS Account with access to S3
2. **Installation**:
   - Install required libraries using:
     ```
     pip install -r requirements.txt
     ```
3. **Run the Scripts**:
   - Execute `main.py` after ensuring `authentication.py` and `endpoint.py` are correctly configured.

## Output
- A CSV file containing details of new album releases.
- The processed file is stored in a programmatically created AWS S3 bucket.

## Future Improvements
- Extend functionality to retrieve additional data like track details or artist information.
- Add data validation steps to ensure robustness.
