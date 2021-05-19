# WebNote
Django rest api site providing api for simple operations on short texts, such as GET, POST, PUT, DELETE  

# Website
Project is deployed and accepts requests on webpage https://web-note-project.herokuapp.com/api/ 
Use `a92e242f925461a50d852dee5ba83371ce721c19` token for authenticated operations.

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
* [GET](examples/API%20endpoints.md) : `GET /api/` - Get all available notes
* [GET](examples/API%20endpoints.md) : `GET /api/:pk/` - Get specific Note

## Endpoints that require Authentication

Closed endpoints require a valid Token to be included in the header of the
request. A Token can be acquired by generating it in admin panel.
### Operations on unspecified note
*  [GET](examples/AUTH%20endpoints.md) : `GET /auth/`
*  [POST](examples/AUTH%20endpoints.md) : `POST /auth/`

### Operations on specific Notes
*  [GET](examples/AUTH%20endpoints.md) : `GET /auth/:pk/`
*  [PUT](examples/AUTH%20endpoints.md) : `PUT /auth/:pk/`
*  [DELETE](examples/AUTH%20endpoints.md) : `DELETE /auth/:pk/`
