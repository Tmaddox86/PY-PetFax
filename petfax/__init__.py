from flask import Flask 
from flask_migrate import Migrate

def create_app():  
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:lovingtech@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False             

    from . import models
    models.db.init_app(app)

    migrate = Migrate(app, models.db)

    @app.route('/')
    def index(): 
        return 'Hello, PetFax!'
    
    #@app.route('/pets')
    #def pets_page(): 
    #    return 'These are our pets up for adoption'

    # register pet blueprint 
    from . import pet, fact
    app.register_blueprint(pet.bp)
    app.register_blueprint(fact.bp)

    # return the app 
    return app

               

