from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from flaskr.db import get_db

bp = Blueprint('map', __name__, url_prefix='/map')

@bp.route('/')
def show_map():
    return render_template('map/map.html')