from flask import Flask 
from flask_restful import Api 
from db import db
from purchase_orders.resources import PurchaseOrders,PurchaseOrderById
from purchase_orders_items.resources import PurchaseOrdersItems

def create_app ():
  app = Flask (__name__)
  api = Api(app)
  app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:adm123@localhost:5432/python_course'
  app.config['SQLALCHEMY_MODIFICATIONS']=False
  db.init_app(app)
  api.add_resource(PurchaseOrders,'/purchase_orders')
  api.add_resource(PurchaseOrderById,'/purchase_orders/<int:id>')
  api.add_resource(PurchaseOrdersItems, '/purchase_orders/<int:id>/items')
  @app.before_request
  def create_tables():
    db.create_all()
  return app
  