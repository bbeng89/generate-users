import csv
import random

first_names = []
last_names = []

first_name_csv = 'CSV_Database_of_First_Names.csv'
last_name_csv = 'CSV_Database_of_Last_Names.csv'
departments = ["Accounting", "Purchasing", "Management", "IT", "Logistics", "Marketing", "Sales", "Human Resources", "Customer Service"]

outfile = raw_input("Enter filename: ")
if not outfile.endswith('.csv'):
	outfile = outfile + ".csv"
	
num_users = int(raw_input("Number of users to generate: "))

usernames = []

def random_first_name():
	return first_names[random.randint(1, len(first_names) - 1)][0]

def random_last_name():
	return last_names[random.randint(1, len(last_names) - 1)][0]

def random_phone_number():
	area_code = str(random.randint(1, 9)) + str(random.randint(0, 9)) + str(random.randint(1, 9))
	first_three = str(random.randint(1, 9)) + str(random.randint(0, 9)) + str(random.randint(1, 9))
	last_four = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
	return '(' + area_code + ') ' + first_three + '-' + last_four 

def random_extension():
	return str(random.randint(1, 9)) + str(random.randint(0, 9)) + str(random.randint(1, 9))

def random_department():
	return departments[random.randint(0, len(departments) - 1)]

def get_username(firstname, lastname):
	uname = firstname[0].lower() + lastname[0:5].lower()
	i = 1
	while uname in usernames:
		uname = firstname[0].lower() + lastname[0:5].lower() + str(i)
		i += 1
	return uname

print "Importing first names..."

with open(first_name_csv, 'rU') as fncsv:
	fnreader = csv.reader(fncsv)
	for row in fnreader:
		first_names.append(row)

print "Importing last names..."

with open(last_name_csv, 'rU') as lncsv:
	lnreader = csv.reader(lncsv)
	for row in lnreader:
		last_names.append(row)

print "Generating users..."

with open(outfile, 'wb') as outcsv:
	outwriter = csv.writer(outcsv)
	outwriter.writerow(["Username", "Password", "Email", "Groups", "First Name", "Last Name", "Phone", "Phone Ext", "Department"])
	for i in range(num_users):
		fname = random_first_name()
		lname = random_last_name()
		phone = random_phone_number()
		ext = random_extension()
		dept = random_department()
		uname = get_username(fname, lname)
		usernames.append(uname)
		email = uname + "@testcompany.com"
		groups = dept
		if(dept == "IT"):
			groups = groups + "|" + "Administrators"
		outwriter.writerow([uname, "password", email, groups, fname, lname, phone, ext, dept])

print "Done."

