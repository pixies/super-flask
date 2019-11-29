from flask import Flask
from .views.index import index
from .views.admin import admin
from .views.accounts import new_account

app = Flask(__name__)

app.register_blueprint(index)
app.register_blueprint(admin)
app.register_blueprint(new_account)