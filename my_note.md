- pip install django
- pip install python-decouple
- pip install djangorestframework
- pip install django-heroku
- pip install django-cors-headers
- pip install django-rest-auth
- pip install django-allauth


## Deploy on Heroko
Ann's path for Heroku
- `./node_modules/heroku/bin/run`
- run `pip freeze` and coppy everything
- create `reauirements.txt` and paste 
- `git init` create gitignore 
- 

- `herohu addons` check if we have heroku database
- `heroku run python manage.py migrate` migrate to posgres
- `heroku run bash`
- `python manage.py createsuperuser` 
- `python manage.py shell` do the magic
