# Dabloon Bank script
import os
import time

current_amount = []
CC = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def List_options():
	CC()
	print("------Dabloon Bank------")
	print('''
1. Add Dabloons
2. Buy Something
3. Check Balance
	''')
	opt = input("Option: ")
	if opt == '1':
		OPT1()
	if opt == '2':
		OPT2()
	if opt == '3':
		OPT3()
	else:
		OPT4()
    
def check_money(self):
	self = current_amount
	return current_amount

def save_money(self, dabloonstoadd):
	self = current_amount
	with open('save_file.txt', 'r+') as file:
		integer = int(file.readline())
		# sets the file pointer? at the first byte
		# so that the write method will overwrite the first bytes of data
		file.seek(0)
		file.write(str(integer + int(dabloonstoadd)))
		file.close()

def withdraw_money(self, dabloonstosub):
	self = current_amount
	with open('save_file.txt', 'r+') as file:
		interger = int(file.readline())
		file.seek(0)
		file.write(str(interger - int(dabloonstosub)))
		file.close()

def OPT1():
	CC()
	dabloonstoadd = input('Amount to add: ')
	save_money(current_amount, dabloonstoadd)
	print("Dabloons added")
	with open('save_file.txt', 'r+') as file:
		print(file.read())
		file.close()
	time.sleep(2)
	List_options()

def OPT2():
	CC()
	dabloonstosub = input('Amount of money: ')
	withdraw_money(current_amount, dabloonstosub)
	print("Dabloons removed")
	with open('save_file.txt', 'r+') as file:
		print(file.read())
		file.close()
	time.sleep(2)
	List_options()

def OPT3():
	CC()
	with open('save_file.txt', 'r+') as file:
		print(file.read())
		file.close()
	time.sleep(3)
	List_options()
  
def OPT4():
  CC()
  List_options()
  
# Call to
List_options()

# Made by Cooper Ransom 12/3/2022
