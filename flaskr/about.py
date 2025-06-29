from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from flaskr.db import get_db

bp = Blueprint('about', __name__, url_prefix='/about')

@bp.route('/')
def show_about():
    return render_template('about/about.html')