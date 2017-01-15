# Setup server instructions-

git clone https://github.com/balajivenkatesh/resumebackend.git

cd resumebackend

# Edit resumebackend/settings.py DATABASES to point to MySql db, user, etc.

python manage.py makemigrations currentresume

python manage.py migrate

python manage.py runserver 0.0.0.0:8000

# 0.0.0.0 to access via local network, next see app readme