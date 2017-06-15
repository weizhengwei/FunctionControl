# -*- coding: utf-8 -*-
import web
import json
import datetime
import random
seed = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#db = web.database(dbn='mysql', db='test', user='med', pw='Zteict@2016')
db = web.database(dbn='mysql', db='test', user='root', pw='r00t')
t = db.transaction()

def get_todos():
	return db.select('todo', order='id')

def new_todo(text):
	db.insert('todo', title=text)

def del_todo(id):
	db.delete('todo', where='id=$id', vars=locals())


def get_all_function():
	return db.select('tb_function_module', order='id')

def add_function(data):
	data_json = json.loads(data)
	return db.insert('tb_function_module', function_number=data_json.get('function_number'),
		function_type=data_json.get('function_type'), function_name=data_json.get('function_name'),
		create_time=datetime.datetime.utcnow())


def get_all_license():
	return db.select('tb_license_module', order='id')

def add_license(data):
	data_json = json.loads(data)
	funcs = data_json.get('functions')
	amount = data_json.get('amount')
	for i in range(amount):
		license = ''.join(random.choice(seed) for i in range(16))
		db.insert('tb_license_module', license_number=license, functions=funcs,
		create_time=datetime.datetime.utcnow(), expiration_time=datetime.datetime.utcnow())







def test():
	try:
	    db.insert('person', name='foo')
	    db.insert('person', name='bar')
	except:
	    t.rollback()
	    raise
	else:
	    t.commit()










