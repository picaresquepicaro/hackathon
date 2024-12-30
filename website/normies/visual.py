from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort


bp = Blueprint('visual', __name__)

@bp.route('/')
def index():
    with open("data.geojson", "r") as file:
        data = file.read()
    return render_template('index.html', json=data)


@bp.route("/json")
def json():
    #data = os.path.join(APP_FOLDER, "data.geojson")
    with open("data.geojson", 'r') as file:
        data = file.read()
    data = data    
    return data
