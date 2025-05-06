# Project Setup Instructions

<b> 1. Clone the Project  </b> <br/>
      `clone https://github.com/apl-mhd/pyron-blog.git` <br>
       `cd pyron-blog`

<b> 2. Create a Virtual Environment and Activate It </b> <br>
      `python -m venv venv` <br>
      `source venv/bin/activate` (Linux/macOS) <br>
      `venv\Scripts\activate` (Windows) <br>

<b> 3. Install Dependencies </b> <br>
      `pip install -r requirements.txt` <br>

<b> 4. Set Up .env File  </b> <br>
      `cp .env.example .env` or `rename .env.example to .env` <br>

<b> 5. Apply Migrations </b> <br>
      `python manage.py makemigrations` <br>
      `python manage.py migrate` <br>

<b> 6. Create a Superuser (Optional – For Admin Access) </b> <br>
      `python manage.py createsuperuser` <br>

<b> 7. Run the Development Server </b> <br>
      `python manage.py runserver` <br>

<b> 8. Visit the App </b> <br>
      `http://127.0.0.1:8000/` <br>
