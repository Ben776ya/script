import requests
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Define your OAuth 2.0 credentials
credentials = service_account.Credentials.from_service_account_file(
    'credentials.json',
    scopes=['https://www.googleapis.com/auth/blogger']
)

def create_blog_post(title, content):
    # Initialize the Blogger service
    blogger_service = build('blogger', 'v3', credentials=credentials)

    # Define the blog post body
    body = {
        'kind': 'blogger#post',
        'title': title,
        'content': content,
    }

    try:
        # Create the blog post
        post = blogger_service.posts().insert(blogId='YOUR_BLOG_ID', body=body).execute()
        print(f"Blog post created successfully with ID: {post['id']}")
        return post['id']
    except Exception as e:
        print(f"Failed to create blog post: {str(e)}")
        return None

# Example Usage:
blog_title = "My Blog Post"
blog_content = "This is the content of my blog post."

create_blog_post(blog_title, blog_content)
