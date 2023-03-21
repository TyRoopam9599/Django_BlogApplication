# Django Blog Application
This is a simple Django blog application that allows the owner to create and view blog posts. The latest blog post is displayed at the top of the homepage.

# Features
1. Create and view blog posts
2. Latest blog post displayed at the top of the homepage
3. Responsive design
4. Search functionality

# Getting Started
1. Clone the repository
2. Install the requirements: `pip install -r requirements.txt`
3. Run the migrations: `python manage.py migrate`
4. Create a superuser: `python manage.py createsuperuser`
5. Run the server: `python manage.py runserver`

# Usage
1. Visit http://localhost:8000/admin and login with your superuser credentials.
2. Create a new blog post by clicking the `Add` button next to `Blog posts`.
3. View your blog posts on the homepage (http://localhost:8000).

# Future Work
Here are some features that could be added to the application:

1. User authentication: Allow multiple users to create and manage their own blog posts.
2. Image uploads: Allow users to upload images to their blog posts.
3. Pagination: Add pagination to the homepage to display a limited number of blog posts at a time.
4. Categories: Allow users to categorize their blog posts.
5. Comments: Allow users to comment on blog posts.
