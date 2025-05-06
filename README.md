# Project Setup Instructions

 1. <b> Clone the Project  </b> <br/>
`git clone https://github.com/apl-mhd/pyron-blog.git` <br>
`cd pyron-blog`

 2. <b> Create a Virtual Environment and Activate It </b> <br>
`python -m venv venv` <br>
`source venv/bin/activate` (Linux/macOS) <br>
`venv\Scripts\activate` (Windows) <br>

 3. <b> Install Dependencies </b> <br>
`pip install -r requirements.txt` <br>

 4. <b> Set Up .env File  </b> <br>
`cp .env.example .env` or `rename .env.example to .env` <br>

 5. <b> Apply Migrations </b> <br>
`python manage.py makemigrations` <br>
`python manage.py migrate` <br>

 6. <b> Create a Superuser (Optional – For Admin Access) </b> <br>
`python manage.py createsuperuser` <br>

 7. <b> Run the Development Server </b> <br>
`python manage.py runserver` <br>

8. <b> Visit the App </b> <br>
http://127.0.0.1:8000/ <br>

9. <b> Test project </b> <br>
 `python manage.py test` `python manage.py test accounts` `python manage.py test post`

# API Endpoint Description 
1. <b> User Registration — POST /api/register </b> <br>
Registers a new user with a username, email,first_name, last_name and password. Requires password confirmation. Returns user info on success.

2. <b> POST /api/token/ </b> <br/>
Authenticates a user and returns access and refresh tokens.

3. <b> GET /api/posts/ </b> <br/>
Returns a list of all published blog posts.

4. <b> POST /api/posts/ (Authenticated) </b> <br/>
Creates a new blog post. Requires authentication (e.g., JWT token).

5. <b> GET /api/posts/id/ </b> <br/>
Fetches the details of a specific blog post by its ID.

6. <b> PUT /api/posts/id/ (Only by post author) </b> <br/>
Updates the details of an existing blog post. Only the author of the post can make updates.

7. <b> DELETE /api/posts/id/ (Only by post author) </b> <br/>
Deletes a specific blog post. Only the author of the post can delete it.
