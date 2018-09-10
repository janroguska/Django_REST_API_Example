import os

class userObject:
	username = None
	email = None
	password = None
	password2 = None

def addUser():
	obj = userObject()
	obj.username = input("username: ")
	obj.email = input("email: ")
	obj.password = input("passwd: ")
	obj.password2 = input("repeat passwd: ")
	os.system("curl 127.0.0.1:8000/api/v1/rest-auth/registration/ -d username=\""
		+ obj.username + "\" -d email=\"" + obj.email + "\" -d password1=\""
		+ obj.password + "\" -d password2=\"" + obj.password2 + "\"")
	print ("\n")