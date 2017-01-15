## Setup server instructions -

\# Run the following in shell

git clone https://github.com/balajivenkatesh/resumebackend.git

cd resumebackend

\# Edit resumebackend/settings.py DATABASES to point to MySql db, user, etc.

python manage.py makemigrations currentresume

python manage.py migrate

python manage.py runserver 0.0.0.0:8000

\# 0.0.0.0 to access via local network, next see app readme

## Endpoints

Example http://192.168.1.73:8000/currentresume

GET - Get the most recent resume or error when none exists

Expect -

[200 OK] returns most recent resume, {'resume_body':'Body of the resume'}

[400 BAD REQUEST] when no resume uploaded yet, {'error':'No resume uploaded yet.'}
	
POST - Add a new resume

request body like {'resume_body':'Body of the resume'} with max length of body = 500

Expect -

[201 CREATED] when successfully saved, {'success':'Resume uploaded.'}

[400 BAD REQUEST] when some error, {'error': errMsg}
	