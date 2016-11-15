from flask import Blueprint, render_template

# setup blueprint
# we are using a "divisional structure" so we need to say
# where templates and static files are
# in this case we don't have templates declared because...
# we are using the templates folder in the main app which is default
# (i am making an educated guessing)
cellar_blueprint = Blueprint('cellar', __name__)

# if you compare view.py to other modules or blueprints
# they use @blueprint cos that is their blueprint's name
@cellar_blueprint.route('/')
def hello():
    '''
    A trivial route.
    '''
    return "Hello!"

# Explictly declared available methods
# Route using a noun to make Nils proud
@cellar_blueprint.route('/beer', methods=['GET'])
def browse():
    '''
    This route should show a list of beer.
    '''
    return "List of beer"



