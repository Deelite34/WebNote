# WebNote
Django rest api site providing api for simple operations on short texts, such as GET, POST, PUT, DELETE  

## Installation
create virtual environment `python -m venv venv_zakop_app`  
launch virtual environment `.\venv_zakop_app\scripts\activate` (powershell command)  
Install required modules `pip install -r requirements.txt`  
Create database `python manage.py migrate`  
Create super user `python manage.py createsuperuser`
Run server `python manage.py runserver`  
Log in as super user in /admin/ and generate token to be used for requests requiring authorisation  
Add TOKEN to request headers containing key - "Authorization" and value - "token TOKEN" (replace TOKEN with your token)  

# Tests
Tests cover all request method views, as well as redirection from base directory to /api/
To run tests, enter `python manage.py test api.test`

## Open Endpoints


Open endpoints require no Authentication.

* API : `GET /api/` - Get all available notes
* API : `GET /api/:pk/` - Get specific Note

## Endpoints that require Authentication

Closed endpoints require a valid Token to be included in the header of the
request. A Token can be acquired by generating it in admin panel.
### Operations on unspecified note
*  AUTH : `GET /auth/`
*  AUTH : `POST /auth/`

### Operations on specific Notes
*  AUTH : `GET /auth/:pk/`
*  AUTH : `PUT /auth/:pk/`
*  AUTH : `DELETE /auth/:pk/`