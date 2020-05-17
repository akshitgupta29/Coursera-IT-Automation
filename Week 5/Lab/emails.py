#!/usr/bin/env python3

import sys
import csv

def populate_dictionary(filename):
	email_dict = {}
	with open(filename) as csvfile:
		lines = csv.reader(csvfile, delimiter = ',')
		for row in lines:
			name = str(row[0].lower())
			email_dict[name] = row[1]
	return email_dict

def find_email(argv):
	try:
		fullname = str(argv[1] + " " + argv[2])
		email_dict = populate_dictionary('/home/student-02-cc873db5fdea/data/user_emails.csv')
		return email_dict.get(fullname.lower())
	except IndexError:
		return "Missing parameters"

def main():
	print(find_email(sys.argv))

if __name__ == "__main__":
	main()
