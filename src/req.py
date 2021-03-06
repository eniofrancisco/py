import requests
import json
import requests

from flask import Flask, request, Response
from flask_restful import Resource, Api
from json import dumps

app = Flask(__name__)
api = Api(app)

def lerArquivo(api, versao, tipo, teste):
	try:
		sqlinjection = request.args.get('sql')
		print('The sqlinjection value is: {%s}' % sqlinjection)
		if sqlinjection == "select" or sqlinjection == "update" or sqlinjection == "drop" or sqlinjection == "delete" or sqlinjection == "alter" or sqlinjection == "create" or sqlinjection == "drop table" or sqlinjection == "where 1=1" or sqlinjection == "create user":
			f = open("files/%s_%s_sqlinjection.htm" % (api, versao), "r")
		elif tipo == "certificado":
			if teste == "1A2E3A4E5B6D7B8E9B10A":
				f = open("files/%s_%s_%s_%s.htm" % (api, versao, tipo, teste), "r")
			else:
				f = open("files/%s_%s_reprovado_001.htm" % (api, versao), "r")
		else:
			f = open("files/%s_%s_%s_%s.htm" % (api, versao, tipo, teste), "r")
	except Exception:
		f = open("files/%s_%s_html_404.htm" % (api, versao), "r")
	
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
class SimuladorArg4(Resource):
	def get(self, arg1, arg2, arg3, arg4):
		return Response(response=lerArquivo(arg1, arg2, arg3, arg4),content_type=tipoContent(arg4),status=200)
	def post(self, arg1, arg2, arg3, arg4):
		return Response(response=lerArquivo(arg1, arg2, arg3, arg4),content_type=tipoContent(arg4),status=200)
# Add Routes
api.add_resource(SimuladorArg4, '/<arg1>/<arg2>/<arg3>/<arg4>')

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
