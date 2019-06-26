from cfgsaver import cfgsaver

pkg_name = 'cfgsaver_test'

def test_save():
	config = [{'name': 'Sophie', 'language': 'Python'}, {'name': 'Hildegard', 'language': 'PHP'}]
	assert cfgsaver.save(pkg_name, config) == True

def test_get():
	obj = cfgsaver.get(pkg_name)
	assert obj[0]['name'] == 'Sophie'


	
##print('hello')