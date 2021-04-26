from flask import Blueprint

bp = Blueprint('download_file', __name__)

from app.main import routes