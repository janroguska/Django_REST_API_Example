import os, sys

class dataObject:
	input_type = None
	data_id = None
	uid = None
	name = None
	age = None
	image = None
	username = None

def setUp():
	obj = dataObject()
	obj.input_type = input("GET, POST, PUT, DELETE: ")
	if (obj.input_type == "GET" or obj.input_type == "POST"
		or obj.input_type == "PUT" or obj.input_type == "DELETE"):
		executeQuery(obj)


def executeQuery(obj):
	obj.username = input("username: ")
	if obj.input_type == "GET":
		call = setGet(obj)
	elif obj.input_type == "POST":
		call = setPost(obj)
	elif obj.input_type == "PUT":
		call = setPut(obj)
	else:
		call = setDelete(obj)
	os.system(call)

def setGet(obj):
	obj.data_id = input("id(optional): ")
	data_id = "" if obj.data_id == "" else obj.data_id + "/"
	return ("curl --user " + obj.username + " -X " + obj.input_type
		+ " http://127.0.0.1:8000/api/v1/users/" + data_id + "; echo")

def setPost(obj):
	obj.uid = input("uid: ")
	obj.name = input("name: ")
	obj.age = input("age: ")
	age = "" if obj.age == "" else ",\"age\":\"" + obj.age+ "\""
	obj.image = input("image: ")
	image = "" if obj.image == "" else ",\"image\":\"" + obj.image + "\""
	return ("curl --user " + obj.username +
		" --header \"Content-Type: application/json\" -X " + obj.input_type
		+ " --data '{\"uid\":\"" + obj.uid
		+ "\",\"name\":\"" + obj.name + "\""
		+ age
		+ image +
		"}' http://127.0.0.1:8000/api/v1/users/; echo")

def setPut(obj):
	obj.data_id = input("id(required): ")
	data_id = "" if obj.data_id == "" else obj.data_id + "/"
	obj.uid = input("uid(required): ")
	obj.name = input("name(required): ")
	obj.age = input("age: ")
	age = "" if obj.age == "" else ", \"age\":\"" + obj.age+ "\""
	obj.image = input("image: ")
	image = "" if obj.image == "" else ", \"image\":\"" + obj.image + "\""
	return ("curl --user " + obj.username +
		" --header \"Content-Type: application/json\" -X " + obj.input_type
		+ " --data '{\"uid\":\"" + obj.uid
		+ "\", \"name\":\"" + obj.name + "\""
		+ age
		+ image +
		"}' http://127.0.0.1:8000/api/v1/users/" + data_id + "; echo")

def setDelete(obj):
	obj.data_id = input("id(required): ")
	data_id = "" if obj.data_id == "" else obj.data_id + "/"
	return ("curl --user " + obj.username + " -X " + obj.input_type
		+ " http://127.0.0.1:8000/api/v1/users/" + data_id + "; echo")
