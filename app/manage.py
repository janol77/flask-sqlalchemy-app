# manage.py
from db import db
from server import create_app
from models.uno import *
from models.dos import *

app = create_app()
db.create_all(app=app)
app.app_context().push()