#

## Walkthrough

* Get started
  * $ pip install flask flask-sqlalchemy
  * Write basic `app.py`
  ```
  from flask import Flask
  app = Flask(__name__)

  @app.route('/')
  def index():
    return "Hello World!!"
  if __name__ == "__main__":
    app.run(debug=True)
  ```
  * $ python3 app.py
  * `return "<h2>Hello World</h2>"`
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
