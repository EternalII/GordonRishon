from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from flaskr.db import get_db

bp = Blueprint('biography', __name__, url_prefix='/biography')

@bp.route('/')
def show_biography():
    return render_template('biography/biography.html')