import requests
import json
import requests

from flask import Flask, request, Response
from flask_restful import Resource, Api
from json import dumps

app = Flask(__name__)
api = Api(app)

def lerArquivo(tipo, teste):
	try:
		sqlinjection = request.args.get('sql')
		print('The sqlinjection value is: {%s}' % sqlinjection)
		if sqlinjection == "select" or sqlinjection == "update" or sqlinjection == "drop" or sqlinjection == "delete" or sqlinjection == "alter" or sqlinjection == "create" or sqlinjection == "drop table" or sqlinjection == "WHERE 1=1" or sqlinjection == "CREATE USER":
			f = open("files/sqlinjection.htm", "r")
		elif tipo == "certificado":
			if teste == "1A2E3A4E5B6D7B8E9B10A":
				f = open("files/%s_%s.htm" % (tipo, teste), "r")
			else:
				f = open("files/reprovado_001.htm")
		else:
			f = open("files/%s_%s.htm" % (tipo, teste), "r")
	except Exception:
		f = open("files/html_404.htm", "r")
	
	return f.read()

def tipoContent(tipo):
	if tipo == "json":
		return "application/json; charset=iso-8859-1"
	elif tipo == "html":
		return "text/html; charset=iso-8859-1"
	elif tipo == "xml":
		return "text/xml; charset=iso-8859-1"
	else:
		return "text/html; charset=iso-8859-1"

# Define Classes
class Simulador(Resource):
	def get(self, arg1, arg2):
		return Response(response=lerArquivo(arg1, arg2),content_type=tipoContent(arg1),status=200)
	def post(self, arg1, arg2):
		return Response(response=lerArquivo(arg1, arg2),content_type=tipoContent(arg1),status=200)
# Add Routes
api.add_resource(Simulador, '/<arg1>/<arg2>')

# Define Classes
class SimuladorTipo(Resource):
	def get(self, arg1):
		return Response(response=lerArquivo(arg1, ""),content_type=tipoContent(arg1),status=200)
	def post(self, arg1):
		return Response(response=lerArquivo(arg1, ""),content_type=tipoContent(arg1),status=200)
# Add Routes
api.add_resource(SimuladorTipo, '/<arg1>')

# Main
if __name__ == '__main__':
	app.run(host='0.0.0.0',port='5002')
