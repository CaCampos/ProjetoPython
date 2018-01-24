import requests
import json

id = int(input("Digite uma ID: "))


url = "http://politicos.olhoneles.org/api/v0/politicians/{}".format(id)


#Exiba  as informações do político a partir da ID
