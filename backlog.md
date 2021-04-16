#

## Walkthrough

* Create database:
  * in python shell import db from app
  * $ db.create_all()
* Heroku
  * $ heroku login
  * $ pip install gunicorn
  * $ pip freeze > requirements.txt
  * $ heroku create todoappnameflask
  * $ git push master
  * Procfile
    * web: gunicorn app:app
