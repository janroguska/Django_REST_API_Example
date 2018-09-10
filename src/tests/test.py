import os
import add_user, make_queries

def main():
	account = input("Create account? [y/n]")
	if account == "y":
		add_user.addUser()
	make_queries.setUp()

main()