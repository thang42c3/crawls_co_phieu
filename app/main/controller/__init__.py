from flask import Blueprint

bp = Blueprint('main', __name__)

from app.main.controller import choosing_code_controller, download_file_controller