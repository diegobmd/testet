from models import FeiraLivre
from db import session

from flask_restful import reqparse
from flask_restful import abort
from flask_restful import Resource
from flask_restful import fields
from flask_restful import marshal_with
from flask_restful import request

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

# FeiraResource
# shows a single feira item and lets you delete a feira item
class FeiraResource(Resource):
    # Get
    @marshal_with(feira_fields)
    def get(self, feira_id):
        feira = db.session.query(FeiraLivre).filter(FeiraLivre.id == feira_id).first()
        if feira is None:
            abort(404, message="Feira {} doesn't exist".format(feira_id))

        return feira

    # Delete
    def delete(self, feira_id):
        feira = session.query(FeiraLivre).filter(FeiraLivre.id == feira_id).first()
        if feira is None:
            abort(404, message="Feira {} doesn't exist".format(id))
        session.delete(feira)
        session.commit()
        return {}, 204

    # Update
    @marshal_with(feira_fields)
    def put(self, feira_id):
        parsed_args = parser.parse_args()
        feira = session.query(FeiraLivre).filter(FeiraLivre.id == feira_id).first()
        feira.task = parsed_args['feira']
        session.add(feira)
        session.commit()
        return feira, 201

# FeiraListResource
# shows a list of all feiras, and lets you POST to add new feiras
class FeiraListResource(Resource):
    @marshal_with(feira_fields)
    def get(self):
        distrito = request.args.get('distrito')
        regiao5 = request.args.get('regiao5')
        nomeFeira = request.args.get('nomeFeira')
        bairro = request.args.get('bairro')

        if distrito is not None:
            feiras = session.query(FeiraLivre).filter(FeiraLivre.distrito == distrito).all()
        elif regiao5 is not None:
            feiras = session.query(FeiraLivre).filter(FeiraLivre.regiao5 == regiao5).all()
        elif nomeFeira is not None:
            feiras = session.query(FeiraLivre).filter(FeiraLivre.nomeFeira == nomeFeira).all()
        elif bairro is not None:
            feiras = session.query(FeiraLivre).filter(FeiraLivre.bairro == bairro).all()
        else:
            feiras = session.query(FeiraLivre).limit(1).all()

        return feiras

    @marshal_with(feira_fields)
    def post(self):
        parsed_args = parser.parse_args()
        feira = FeiraLivre(feira=parsed_args['feira'])
        session.add(feira)
        session.commit()
        return feira, 201
