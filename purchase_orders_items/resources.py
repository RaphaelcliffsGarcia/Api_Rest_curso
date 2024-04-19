from flask import jsonify
from flask_restful import Resource,reqparse

purchase_orders = [{
  'id':1,
  'description':'Purchase Order id 1',
  'items':[{
    'id':1,
    'description':'item do pedido 1',
    'price':20.99    
  }]                  
}]

class PurchaseOrdersItems(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument(
    'id',
    type=int,
    required=True,
    help = 'Informe um Id Valido'
  )
  parser.add_argument(
    'description',
    type=str,
    required=True,
    help = 'Informe uma Descrição Valida'
  )
  parser.add_argument(
    'price',
    type=float,
    required=True,
    help = 'Informe uma preço Valido'
  )
  
  
  
  def get (self,id):
    for po in purchase_orders:
      if po ['id'] == id:
        return jsonify(po['items'])
    return jsonify({'message':'Pedido de id {} não encontrado'.format(id)})
    
  def post(self,id):
    data = PurchaseOrdersItems().parser.parse_args()
    for po in purchase_orders:
      if po ['id'] == id:
        po['items'].append({
          'id':data['id'],
          'description':data['description'],
          'price':data['price']
        })
        return jsonify(po)
    
