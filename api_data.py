import requests
import pandas as pd

# API URL
url = "https://jsonplaceholder.typicode.com/users"

# Send GET request
response = requests.get(url)

# Check response
if response.status_code == 200:

    data = response.json()

    # Convert JSON into DataFrame
    df = pd.DataFrame(data)

    print("API DATA FETCHED SUCCESSFULLY")

    print(df[["id", "name", "email"]])

    # Save API data
    df.to_csv("api_data.csv", index=False)

    print("\nAPI Data Saved Successfully!")

else:
    print("API Request Failed")