from flask import jsonify
from flask_restful import Resource

purchase_orders = [{
  'id':1,
  'description':'Purchase Order id 1',
  'items':[{
    'id':1,
    'description':'item do pedido 1',
    'price':20.99    
  }]                  
}]

class PurchaseOrders(Resource):
   def get(self):
     return jsonify(purchase_orders)
   