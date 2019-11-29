from flask import Flask
from .views.index import index
from .views.admin import admin

app = Flask(__name__)


app.register_blueprint(index)
app.register_blueprint(admin)