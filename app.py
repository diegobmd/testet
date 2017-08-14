import logging.config

from flask import Flask, Blueprint
from flask_restplus import Api, reqparse, abort, Resource, fields, marshal_with
from models import FeiraLivre
from db import session
from sqlalchemy.orm.exc import NoResultFound

app = Flask(__name__)

logging.config.fileConfig('logging.conf')
log = logging.getLogger(__name__)

api = Api(app)

blueprint = Blueprint('api', __name__)
api.init_app(blueprint)
app.register_blueprint(blueprint)

@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    return {'message': message}, 500


@api.errorhandler(NoResultFound)
def database_not_found_error_handler(e):
    log.warning(traceback.format_exc())
    return {'message': 'A database result was required but none was found.'}, 404

feira_fields = {
    'id': fields.Integer,
    'longitude' : fields.Integer,
    'latitude' : fields.Integer,
    'setcens' : fields.Integer,
    'areap' : fields.Integer,
    'codDist' : fields.Integer,
    'distrito' : fields.String(50),
    'codSubPref' : fields.Integer,
    'subPrefe' : fields.String(50),
    'regiao5' : fields.String(10),
    'regiao8' : fields.String(10),
    'nomeFeira' : fields.String(50),
    'registro' : fields.String(6),
    'logradouro' : fields.String(255),
    'numero' : fields.String(50),
    'bairro' : fields.String(50),
    'referencia' : fields.String(255)
}

parser = reqparse.RequestParser()
parser.add_argument('feira')
parser.add_argument('distrito', type=str, location='args')
parser.add_argument('regiao5', type=str, location='args')
parser.add_argument('nomeFeira', type=str, location='args')
parser.add_argument('bairro', type=str, location='args')

# FeiraResource
# shows a single feira item and lets you delete a feira item
@api.route('/feira/<int:feira_id>')
class FeiraResource(Resource):
    # Get
    @marshal_with(feira_fields)
    def get(self, feira_id):
        log.info('Get a feira %s' % (feira_id))

        feira = session.query(FeiraLivre).filter(FeiraLivre.id == feira_id).first()
        if feira is None:
            abort(404, message="Feira {} doesn't exist".format(feira_id))

        return feira

    # Delete
    def delete(self, feira_id):
        log.info('Delete a feira %s' % (feira_id))

        feira = session.query(FeiraLivre).filter(FeiraLivre.id == feira_id).first()
        if feira is None:
            abort(404, message="Feira {} doesn't exist".format(id))
        session.delete(feira)
        session.commit()
        return {}, 204

    # Update
    @marshal_with(feira_fields)
    def put(self, feira_id):
        log.info('Update a feira %s' % (feira_id))

        parsed_args = parser.parse_args()
        feira = session.query(FeiraLivre).filter(FeiraLivre.id == feira_id).first()
        feira.task = parsed_args['feira']
        session.add(feira)
        session.commit()
        return feira, 201

# FeiraListResource
# shows a list of all feiras, and lets you POST to add new feiras
@api.route('/feiras')
class FeiraListResource(Resource):
    @marshal_with(feira_fields)
    def get(self):
        parsed_args = parser.parse_args()

        distrito = parsed_args['distrito']
        regiao5 = parsed_args['regiao5']
        nomeFeira = parsed_args['nomeFeira']
        bairro = parsed_args['bairro']

        log.info('Getting Feiras Params %s %s %s %s' % (distrito, regiao5, nomeFeira, bairro))

        if distrito is not None:
            feiras = session.query(FeiraLivre).filter(FeiraLivre.distrito == distrito).all()
        elif regiao5 is not None:
            feiras = session.query(FeiraLivre).filter(FeiraLivre.regiao5 == regiao5).all()
        elif nomeFeira is not None:
            feiras = session.query(FeiraLivre).filter(FeiraLivre.nomeFeira == nomeFeira).all()
        elif bairro is not None:
            feiras = session.query(FeiraLivre).filter(FeiraLivre.bairro == bairro).all()
        else:
            #feiras = session.query(FeiraLivre).limit(1).all()
            feiras = session.query(FeiraLivre).all()

        return feiras

    @marshal_with(feira_fields)
    def post(self):

        log.info('Creating a new feira')

        parsed_args = parser.parse_args()
        feira = FeiraLivre(feira=parsed_args['feira'])
        session.add(feira)
        session.commit()
        return feira, 201


if __name__ == '__main__':
    app.run(debug=True)