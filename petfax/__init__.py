from flask import Flask 

def create_app(): 
    app = Flask('App')

    @app.route('/')
    def index(): 
        return 'Hello, PetFax!'
    
    #@app.route('/pets')
    #def pets_page(): 
    #    return 'These are our pets up for adoption'

    # register pet blueprint 
    from . import pet
    app.register_blueprint(pet.bp)

    # return the app 
    return app
