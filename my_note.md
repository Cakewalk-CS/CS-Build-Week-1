- pip install django
- pip install python-decouple
- pip install djangorestframework
- pip install django-heroku
- pip install django-cors-headers
- pip install django-rest-auth
- pip install django-allauth


## Deploy on Heroku
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



player token

curl -X POST -H 'Authorization: Token uJvFvtUztYBzefdPmSVjIJKFEYoVM6h5R4SVQ83Ftb15HR6OWIlNgldTGP43yj78
' -H "Content-Type: application/json" -d '{"direction":"n"}' text-adv-game.herokuapp.com/api/adv/move/
