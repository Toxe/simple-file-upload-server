from flask import Blueprint

bp = Blueprint("download", __name__)

from app.download import routes
