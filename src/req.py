import requests
import json

from flask import Flask, request, Response
from flask_restful import Resource, Api
from json import dumps

app = Flask(__name__)
api = Api(app)

def lerArquivo(tipo, teste):
	try:
		if tipo == "" 
			f = open("files/sucesso.txt", "r")
		else:
			f = open("files/%s_%s.txt" % (tipo, teste), "r")
	except Exception:
		f = open("files/html_404.txt", "r")

	return f.read()

def tipoContent(tipo):
	if tipo == "json":
		return "application/json"
	elif tipo == "html":
		return "text/html"
	elif tipo == "xml":
		return "text/xml"
	else:
		return "text/plain"

# Define Classes
class Simulador(Resource):
	def get(self, arg1, arg2):
		return Response(response=lerArquivo(arg1, arg2),content_type=tipoContent(arg1),status=200)
	def post(self, arg1, arg2):
		return Response(response=lerArquivo(arg1, arg2),content_type=tipoContent(arg1),status=200)

# Add Routes
api.add_resource(Simulador, '/<arg1>/<arg2>')

# Main
if __name__ == '__main__':
	app.run(host='0.0.0.0',port='5002')
