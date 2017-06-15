# -*- coding: utf-8 -*-
import web
import json
import model

urls = (
	'/','index',
	'/api/function','function_module',
	'/api/license','license_module',
	'/api/verify', 'verify_module'
	)

app = web.application(urls, globals())
render = web.template.render('templates/')

class index:
	def GET(self):
		#return 'all function control'
		return render.index()

class function_module:
	def GET(self):
		data = model.get_all_function()
		ret_item = {}
		ret = []
		for item in data:
			ret_item['function_number'] = item.get('function_number')
			ret_item['function_type'] = item.get('function_type')
			ret_item['function_name'] = item.get('function_name')
			ret_item['create_time'] = item.get('create_time').strftime( '%y-%m-%d %I:%M:%S')
			ret.append(ret_item)
		return json.dumps(ret, ensure_ascii=False)

	def POST(self):
		data = web.data()
		print data
		if data != None:
			model.add_function(data)
		return 'add function ok'

class license_module:
	def GET(self):
		data = model.get_all_license()
		ret_item = {}
		ret = []
		for item in data:
			ret_item['license_number'] = item.get('license_number')
			ret_item['functions'] = item.get('functions')
			ret_item['license_state'] = item.get('license_state'),
			ret_item['sn'] = item.get('sn'),
			ret_item['verify_time'] = item.get('verify_time'),
			ret_item['verified'] = item.get('verified'),
			ret_item['create_time'] = item.get('create_time').strftime( '%y-%m-%d %I:%M:%S')
			ret.append(ret_item)
		return json.dumps(ret, ensure_ascii=False)

	def POST(self):
		data = web.data()
		print data
		if data != None:
			model.add_license(data)
		return 'add license ok'

class verify_module:
	def GET():
		pass
	def POST():
		pass

if __name__ == '__main__':
	app.run()