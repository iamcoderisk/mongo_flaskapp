from flask import Response, Request
from database.model import Bus 
from flask_restful import Resource

class BusesApi(Resource):

    def get(self,id):
        buses  = Bus.objects().get(id=id).to_json()
        return Response(buses, mimetype='application/json', status=200)
    
    def post(self):
        body  = request.get_json()
        bus = Bus(**body).save()
        id = bus.id
        return {'id':str(id)}, 200
        
class BusApi(Resource):
    def put(self,id):
        body = request.get_json()
        Bus.objects.get(id=id).update(**body)
        return  '', 200 
    
    def delete(self,id):
        Bus.objects.get(id=id).delete()
        return '',200
