from dao.hb_dao import HBSquads
from controllers.hb_controller import HbControllers
from controllers.frame_controller import FrameControllers
from controllers.banco_controller import BancoControllers
from controllers.ling_controller import LingControllers
from flask import Flask
from flask_restful import Api

app = Flask(__name__)

api = Api(app)

api.add_resource(HbControllers, '/api/hbsquads', endpoint='hbs') 
api.add_resource(HbControllers, '/api/hbsquads/<int:id>', endpoint='hb') 

api.add_resource(FrameControllers, '/api/frame', endpoint='frs') 
api.add_resource(FrameControllers, '/api/frame/<int:id>', endpoint='fr') 

api.add_resource(LingControllers, '/api/ling', endpoint='lings') 
api.add_resource(LingControllers, '/api/ling/<int:id>', endpoint='ling') 

api.add_resource(BancoControllers, '/api/banco', endpoint='bd') 
api.add_resource(BancoControllers, '/api/banco/<int:id>', endpoint='bds') 

app.run(debug=True)
