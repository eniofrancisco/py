import requests
import json

from flask import Flask, request, Response
from flask_restful import Resource, Api
from json import dumps

app = Flask(__name__)
api = Api(app)

def lerArquivo(tipo, teste):
	try:
		if tipo == "certificado":
			if teste == "1A2E3A4E5B6D7B8E9B10A":
				f = open("files/%s_%s.htm" % (tipo, teste), "r")
			else:
				f = open("files/reprovado_001.htm")
		elif tipo == "":
			f = open("files/sucesso.htm", "r")
		else:
			f = open("files/%s_%s.htm" % (tipo, teste), "r")
	except Exception:
		f = open("files/html_404.htm", "r")

	return f.read()

def tipoContent(tipo):
	if tipo == "json":
		return "application/json"
	elif tipo == "html":
		return "text/html"
	elif tipo == "xml":
		return "text/xml"
	else:
		return "text/html"

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
