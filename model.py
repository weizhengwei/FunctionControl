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

def generate_license():
	license = ''
	s = ''.join(random.choice(seed) for i in range(16))
	for i in range(4):
		k = i*4
		if i < 3:
			tmp = s[k:k+4] + '-'
		else:
			tmp = s[k:k+4]
		license = license + tmp
	return license

def add_license(data):
	data_json = json.loads(data, encoding="utf-8")
	funcs = data_json.get('functions')
	amount = data_json.get('amount')
	json_funcs = json.dumps(funcs, ensure_ascii = False)

	create_time = datetime.datetime.now()
	for i in range(amount):
		license = generate_license()
		db.insert('tb_license_module', license_number=license, functions=json_funcs,
		create_time=create_time, expiration_time=create_time+30*24*60*60)



def verify_license(data):
	data_json = json.loads(data)
	license = data_json.get('license')
	sn = data_json.get('sn')
	return real_verify_license(license, sn)

def real_verify_license(license, sn):
	print license
	print sn
	if license == None or sn == None:
		return 'please add ?license=xxx&sn=xxx'
	license_finded = db.select('tb_license_module', where='license_number=$license', vars=locals())
	if len(license_finded) == 0:
		return 'can not find the license, your license is error'
	
	if license_finded[0].license_state == 1:
		return 'the license has been used'

	db.update('tb_license_module', where='license_number=$license', sn=sn, verified=True, 
		license_state=1, verify_time=datetime.datetime.now(), vars=locals())
	functions = license_finded[0].get('functions')
	print functions
	print type(functions)
	return 'verify ok'


def test():
	try:
	    db.insert('person', name='foo')
	    db.insert('person', name='bar')
	except:
	    t.rollback()
	    raise
	else:
	    t.commit()










