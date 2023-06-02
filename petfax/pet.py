import json
from flask import (Blueprint, render_template) 

bp = Blueprint('pet', __name__, url_prefix="/pets")
pets = json.load(open('pets.json'))
#print(pets)

@bp.route('/')
def index(): 
    return render_template ('index.html', pets=pets)

@bp.route('/<int:pet_id')
def show(pet_id):
    return render_template ('pets/show.html', pet=pets[pet_id - 1])
