import requests
import pandas as pd

# Set up login details
username = "Noobenyy101"
password = "#YAHYA-labiba01"

# Read website URL from Excel file
#excel_file = "websites.xlsx"
#df = pd.read_excel(excel_file)
#website_url = df["Website"][0]
website_url = "pages10.com"  # Assuming the URL is in the first column of the Excel file

# Login to the blog creation website
login_url = f"https://{website_url}/login"
login_data = {
    "username": username,
    "password": password
}
session = requests.Session()
session.post(login_url, data=login_data)

# Create a post with backlinks
post_url = f"https://{website_url}/new"
post_data = {
    "title": "My Awesome Blog Post",
    "body": "Check out these amazing websites: [Link 1](https://website1.com), [Link 2](https://website2.com), [Link 3](https://website3.com)"
}
session.post(post_url, data=post_data)

print("Post created successfully!")