from pymongo import MongoClient
from flask_restful import Resource
from flask import request
from repositories.requests import handleRequest
import bcrypt

'''
ARQUIVO QUE GERENCIA AS CLASSES USADAS NAS ROTAS
CHAMA O REPOSITÓRIO, QUE CUIDA DAS VALIDAÇÕES DA REQUEST
'''

'''
CONFIGURAÇÃO DO BANCO
'''
# instanciando mongoClient na porta default
client = MongoClient("localhost", 27017)
# novo database de nome ClassificationDatabase
db = client.ClassificationDatabase
# nova colecttion de nome Users
Users = db.Users
'''
======================
'''

'''
RESOURCES
'''
class Register(Resource):
  def post(self):
    body = request.get_json()
    if body:
      res = handleRequest(Users,body, 'register')
    return res

class Detect(Resource):
  def post(self):
    body = request.get_json()
    if body:
      res = handleRequest(Users,body, 'detect-img')
    return res

class GetUsers(Resource):
  def get(self):
    body = request.get_json()
    if body:
      res = handleRequest(Users,body, 'get-users')
    return res

class Refill(Resource):
  def patch(self):
    body = request.get_json()
    if body:
      res = handleRequest(Users,body, 'refill')
    return res
'''
======================
'''