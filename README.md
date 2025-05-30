# Batch Data Processing Using Spotify API
In this project, I will use Python, AWS, and Spotify's API to build a scalable batch data processing pipeline that extracts, transforms, and stores detailed information about newly released albums and artists. This serves as a practical exercise in data engineering, showcasing skills in API integration, programmatic handling of paginated responses, cloud workflows, and structured data processing. The pipeline enables scalable storage in AWS S3 buckets for further analysis, serving as a foundation for performing trend analyses and creating interactive dashboards to visualize music release patterns.

<div align="center">
    <img src="img/spotify-api-data-pipeline.png" alt="Spotify Data Pipeline" width="500">
</div>

## Scripts
1. **endpoint.py**: Contains the `get_paginated_new_releases` function, which handles paginated API calls to fetch comprehensive details about new album releases.
2. **main.py**: The main script:
   - Authenticates with the Spotify API to obtain an access token.
   - Extracts album and artist data from the `Get New Releases` endpoint.
   - Processes the data into a flattened format suitable for storage.
   - Saves the structured data as a CSV file and uploads it to an AWS S3 bucket.

## Tools and Software Used
- **Python**: Primary programming language for developing the pipeline.
- **Requests**: For making HTTP requests to the Spotify API and handling responses.
- **Pandas**: For transforming extracted JSON data and organizing it into a CSV format.
- **Boto3**: For interacting with AWS S3 services, including file uploads.
- **Dotenv**: For securely managing environment variables.
- **Spotify API**: Source of the data for album and artist information.
- **AWS S3**: Cloud storage for scalability and accessibility of processed data.
  
## Future Improvements
- **Data Modeling**: Enhance the pipeline by structuring the extracted data into dimensional models, organizing it into measures (e.g., popularity scores, track counts) and dimensions (e.g., artist details, release dates) for efficient analysis and reporting.
- **Use of QuickSight Visualization**: Integrate Amazon QuickSight to create interactive dashboards that visualize trends in album releases, artist activity, and genre distributions, enabling deeper insights into the music industry.
- **Use Schedulers like AWS Lambda or Airflow**: Automate the batch processing pipeline by leveraging tools like AWS Lambda or Apache Airflow to schedule periodic data extraction, transformation, and storage tasks seamlessly.
