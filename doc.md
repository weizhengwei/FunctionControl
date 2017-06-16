
验证
verify verification

校验
check

一.功能管理
功能编号 一级功能模块 二级功能模块 更新时间 状态 操作

1.添加：
tb_function_module
/api/functionmodule
{
	"function_type":0,
	"serial_number":"111",
	"function_name":"心电"
}

{
	"function_type":1,
	"serial_number":"111",
	"function_name":"远程音视频"
}

2.获取功能
{
	id
	serial_number
	function_type
	function_name
	create_time
	update_time
	state
}

curl -d "@addfunction.json" localhost:9090/api/function
curl -d "@addfunction.json" localhost:9090/api/function

二.License管理
编号 License号 功能 生成时间 状态 SN 功能生效时间 操作

license_number
functions
create_time
license_state
sn
verify_time
expiration_time




tb_license_module
1.添加：
/api/addlicense
{
	"functions":["1111", "222", "333"],
	"amount":100
}

curl -d "@addlicense.json" localhost:9090/api/license

三。功能配置管理


mysqldump -u root -p med_gwc ＞med_gwc.sql

db = web.database(dbn='mysql', db='test', user='root', pw='123123')

def new_post(title, content):
    db.insert('news', title=title, content=content, posted_on=datetime.datetime.utcnow())

def get_post(id):
    try:
        return db.select('news', where='id=$id', vars=locals())[0]
    except IndexError:
        return None

def get_posts():
    return db.select('news', order = 'id DESC')

def del_post(id):
    db.delete('news', where = 'id = $id', vars = locals())

def update_post(id, title, content):
    db.update('news', where='id = $id', vars=locals(), title=title, content=content)

1./api/function
GET 获取所有测试和非测试功能项
POST 添加功能功能项
curl -d "@addfunction.json" localhost:9090/api/license

2./api/license
GET 获取所有license
POST 添加license
curl -d "@addlicense.json" localhost:9090/api/license

{
	"functions":["1111", "222", "333"],
	"amount":100
}

{
	"functions":[{"1001":"心电图"}, {"1002":"血糖"}, {"1003":"血脂"}],
	"amount":100
}
{
	"functions":[
		{"function_number":"1001","function_name":"心电图"},
		{"function_number":"1002","function_name":"血糖"},
		{"function_number":"1003","function_name":"血脂"}
	],
	"amount":3
}


3./api/verify
根据license校验功能
GET
curl localhost:9090/api/license?license=DFJT-TDRO-Q4I3-W7CU&sn=123456abcdef

POST
curl -d "@verify.json" localhost:9090/api/verify





