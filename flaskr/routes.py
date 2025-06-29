from flask import Blueprint, render_template

bp = Blueprint('routes', __name__)

@bp.route('/')
def home():
    return render_template('about/about.html')  # Or you can create a `home.html`

@bp.route('/about')
def about():
    return render_template('about/about.html')

@bp.route('/map')
def map_page():
    return render_template('map/map.html')

@bp.route('/biography')
def biography():
    return render_template('biography/biography.html')

@bp.route('/contact')
def contact():
    return render_template('contact/contact.html')