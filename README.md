# Portepel

Portepel is a simple Django (web) application built to provide simple image gallery as a personal portfolio web site. This web app is built based on awesome tutorial: [Building a Personal Portfolio with Django](https://www.lynda.com/Django-tutorials/Building-Personal-Portfolio-Django/761962-2.html), and using PostgreSQL as its RDBMS.

## Getting Started

1. Make sure Python 3.x, `venv` module, and PostgreSQL server are already installed and running/setup correctly.

2. Create Python virtual environment and then activate it as shown in [Installing packages using pip and virtual environments](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) tutorial.

3. Let's suppose your working directory right now is your user home directory, so clone the repository:

        $ cd
        $ git clone https://github.com/andisugandi/portepel.git

4. Change working directory to `portepel`:

        $ cd portepel

5. Change DATABASE configuration in 

	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.postgresql',
		'NAME': 'portfoliodb',
		'USER':'julia',
		'PASSWORD':'bismillah90=-',
		'HOST':'127.0.0.1',
		'PORT':'5432',
	    }
	}

6. Install Python modules required, and run the server:

        $ pip install -r requirements.txt
        $ python manage.py runserver

7. Using web browser, go to `http://127.0.0.1:8000` and you'll see the application running

8. Login to Django Admin: `http://127.0.0.1:8000/admin` to start uploading portfolio content and image.

## Demo
[![Web Apps of Galeri Data SQM](https://img.youtube.com/vi/tvdV1UAr564/0.jpg)](https://www.youtube.com/watch?v=tvdV1UAr564)
